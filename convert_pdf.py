#!/usr/bin/env python3
"""
PDF to Markdown Converter with Image Extraction

This script converts PDF files (e.g., from Confluence exports) into markdown format
that can be easily read and queried by GitHub Copilot. It extracts both text and 
images/diagrams from the PDF.

Usage:
    python convert_pdf.py <pdf_file> [output_dir]

Example:
    python convert_pdf.py architecture.pdf docs/
"""

import sys
import os
from pathlib import Path
from datetime import datetime
import io
try:
    from PyPDF2 import PdfReader
    from PIL import Image
except ImportError as e:
    print(f"Error: Required library is not installed: {e}")
    print("Please install dependencies using: pip install -r requirements.txt")
    sys.exit(1)


def extract_images_from_page(page, page_num, pdf_name, images_dir):
    """
    Extract images from a PDF page and save them.
    
    Args:
        page: PDF page object
        page_num: Page number
        pdf_name: Name of the PDF file (without extension)
        images_dir: Directory to save images
        
    Returns:
        List of image filenames that were saved
    """
    images_saved = []
    
    try:
        if '/XObject' not in page['/Resources']:
            return images_saved
            
        xObject = page['/Resources']['/XObject'].get_object()
        
        for obj_name in xObject:
            obj = xObject[obj_name]
            if obj['/Subtype'] == '/Image':
                try:
                    # Extract image data
                    size = (obj['/Width'], obj['/Height'])
                    data = obj.get_data()
                    
                    # Determine image format
                    if '/Filter' in obj:
                        filter_type = obj['/Filter']
                        if filter_type == '/DCTDecode':
                            ext = 'jpg'
                        elif filter_type == '/JPXDecode':
                            ext = 'jp2'
                        elif filter_type == '/FlateDecode':
                            ext = 'png'
                        else:
                            ext = 'png'
                    else:
                        ext = 'png'
                    
                    # Create filename
                    img_filename = f"{pdf_name}_page{page_num}_{obj_name[1:]}.{ext}"
                    img_path = images_dir / img_filename
                    
                    # Save image
                    if ext in ['jpg', 'jpeg']:
                        # Save JPEG directly
                        with open(img_path, 'wb') as img_file:
                            img_file.write(data)
                    else:
                        # Convert other formats to PNG using PIL
                        try:
                            mode = "RGB" if obj.get('/ColorSpace') == '/DeviceRGB' else "P"
                            if '/ColorSpace' in obj and obj['/ColorSpace'] == '/DeviceGray':
                                mode = "L"
                            
                            img = Image.frombytes(mode, size, data)
                            img.save(img_path, 'PNG')
                        except Exception as pil_error:
                            # If PIL fails, save raw data
                            with open(img_path, 'wb') as img_file:
                                img_file.write(data)
                    
                    images_saved.append(img_filename)
                    print(f"  → Extracted image: {img_filename}")
                    
                except Exception as img_error:
                    print(f"  ⚠ Warning: Could not extract image {obj_name}: {img_error}")
                    
    except Exception as e:
        print(f"  ⚠ Warning: Error processing images on page {page_num}: {e}")
    
    return images_saved


def extract_text_and_images_from_pdf(pdf_path, images_dir):
    """
    Extract text content and images from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        images_dir: Directory to save extracted images
        
    Returns:
        Tuple of (text_content, page_image_map) where page_image_map is a dict
        mapping page numbers to lists of image filenames
    """
    try:
        reader = PdfReader(pdf_path)
        text_content = []
        page_image_map = {}
        pdf_name = Path(pdf_path).stem
        
        # Create images directory if it doesn't exist
        images_dir.mkdir(parents=True, exist_ok=True)
        
        for i, page in enumerate(reader.pages, 1):
            # Extract images from this page
            images = extract_images_from_page(page, i, pdf_name, images_dir)
            if images:
                page_image_map[i] = images
            
            # Extract text
            text = page.extract_text()
            if text.strip():
                page_content = f"## Page {i}\n\n"
                
                # Add image references if any images were found on this page
                if images:
                    page_content += "### Diagrams/Images\n\n"
                    for img in images:
                        # Use relative path from docs/ directory
                        page_content += f"![Page {i} Diagram](images/{img})\n\n"
                    page_content += "### Content\n\n"
                
                page_content += f"{text}\n"
                text_content.append(page_content)
        
        return "\n".join(text_content), page_image_map
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None, None


def convert_pdf_to_markdown(pdf_path, output_dir="docs"):
    """
    Convert a PDF file to markdown format with embedded images.
    
    Args:
        pdf_path: Path to the input PDF file
        output_dir: Directory where the markdown file will be saved
        
    Returns:
        Path to the created markdown file, or None if conversion failed
    """
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        print(f"Error: PDF file '{pdf_path}' not found.")
        return None
    
    if not pdf_path.suffix.lower() == '.pdf':
        print(f"Error: '{pdf_path}' is not a PDF file.")
        return None
    
    # Create output directory structure
    output_dir = Path(output_dir)
    images_dir = output_dir / "images"
    
    # Extract text and images from PDF
    print(f"Processing: {pdf_path}")
    text_content, page_image_map = extract_text_and_images_from_pdf(pdf_path, images_dir)
    
    if text_content is None:
        return None
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create markdown filename
    md_filename = pdf_path.stem + ".md"
    output_path = output_dir / md_filename
    
    # Create markdown content with header
    file_mtime = Path(pdf_path).stat().st_mtime
    formatted_date = datetime.fromtimestamp(file_mtime).strftime('%Y-%m-%d %H:%M:%S')
    
    # Count total images extracted
    total_images = sum(len(imgs) for imgs in page_image_map.values())
    
    markdown_content = f"""# {pdf_path.stem}

> This document was automatically converted from PDF: `{pdf_path.name}`
> 
> Generated on: {formatted_date}
> Images extracted: {total_images}

---

{text_content}
"""
    
    # Write markdown file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"✓ Successfully converted to: {output_path}")
        if total_images > 0:
            print(f"✓ Extracted {total_images} image(s) to: {images_dir}")
        return output_path
    except Exception as e:
        print(f"Error writing markdown file: {e}")
        return None


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage: python convert_pdf.py <pdf_file> [output_dir]")
        print("\nExample:")
        print("  python convert_pdf.py architecture.pdf")
        print("  python convert_pdf.py architecture.pdf docs/")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "docs"
    
    result = convert_pdf_to_markdown(pdf_file, output_dir)
    
    if result:
        print("\n" + "="*60)
        print("PDF conversion complete!")
        print("="*60)
        print(f"\nYou can now ask GitHub Copilot questions about the content in:")
        print(f"  {result}")
        print("\nTip: Open the markdown file in your editor to enable Copilot")
        print("     to answer questions about the architecture documentation.")
        sys.exit(0)
    else:
        print("\nConversion failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()

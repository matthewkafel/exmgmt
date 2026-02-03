#!/usr/bin/env python3
"""
PDF to Markdown Converter

This script converts PDF files (e.g., from Confluence exports) into markdown format
that can be easily read and queried by GitHub Copilot.

Usage:
    python convert_pdf.py <pdf_file> [output_dir]

Example:
    python convert_pdf.py architecture.pdf docs/
"""

import sys
import os
from pathlib import Path
from datetime import datetime
try:
    from PyPDF2 import PdfReader
except ImportError:
    print("Error: PyPDF2 is not installed.")
    print("Please install it using: pip install -r requirements.txt")
    sys.exit(1)


def extract_text_from_pdf(pdf_path):
    """
    Extract text content from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Extracted text as a string
    """
    try:
        reader = PdfReader(pdf_path)
        text_content = []
        
        for i, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            if text.strip():
                text_content.append(f"## Page {i}\n\n{text}\n")
        
        return "\n".join(text_content)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None


def convert_pdf_to_markdown(pdf_path, output_dir="docs"):
    """
    Convert a PDF file to markdown format.
    
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
    
    # Extract text from PDF
    print(f"Processing: {pdf_path}")
    text_content = extract_text_from_pdf(pdf_path)
    
    if text_content is None:
        return None
    
    # Create output directory if it doesn't exist
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create markdown filename
    md_filename = pdf_path.stem + ".md"
    output_path = output_dir / md_filename
    
    # Create markdown content with header
    file_mtime = Path(pdf_path).stat().st_mtime
    formatted_date = datetime.fromtimestamp(file_mtime).strftime('%Y-%m-%d %H:%M:%S')
    
    markdown_content = f"""# {pdf_path.stem}

> This document was automatically converted from PDF: `{pdf_path.name}`
> 
> Generated on: {formatted_date}

---

{text_content}
"""
    
    # Write markdown file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"✓ Successfully converted to: {output_path}")
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

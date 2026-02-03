# exmgmt

Documentation management system with PDF-to-Markdown conversion for GitHub Copilot integration.

> **🚀 New here?** Check out the [Quick Start Guide](QUICKSTART.md) to learn where to upload your PDFs!

## Overview

This repository provides tools to convert PDF documents (such as architecture pages from Confluence) into markdown format that GitHub Copilot can easily read and use to answer questions.

## Quick Start

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/matthewkafel/exmgmt.git
   cd exmgmt
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Step 1: Upload Your PDF

**Place your PDF file in the `pdfs/` directory**. You can do this by:

- **Drag and drop** the file into the `pdfs/` folder in your editor
- **Upload via GitHub**: Navigate to the `pdfs/` folder on GitHub and click "Add file" → "Upload files"
- **Copy manually**: Place the file in `<repo-root>/pdfs/your-file.pdf`

Example:
```
exmgmt/
├── pdfs/
│   ├── architecture.pdf          ← Place your PDFs here
│   └── confluence-export.pdf
```

#### Step 2: Convert PDF to Markdown

```bash
python convert_pdf.py pdfs/<your-file>.pdf
```

**Examples:**

```bash
# Convert a PDF from the pdfs/ directory
python convert_pdf.py pdfs/architecture.pdf

# Convert to a specific output directory
python convert_pdf.py pdfs/confluence-export.pdf docs/architecture/

# Convert multiple PDFs
python convert_pdf.py pdfs/system-design.pdf
python convert_pdf.py pdfs/api-documentation.pdf
```

The converted markdown files will be saved in the `docs/` directory by default.

#### Step 3: Ask Questions with GitHub Copilot

Once you've converted your PDFs to markdown:

1. Open the generated markdown file in `docs/` in your editor (VS Code, etc.)
2. Open GitHub Copilot Chat
3. Ask questions about the content:
   - "What are the main architectural components?"
   - "Explain the authentication flow described in this document"
   - "What are the key design decisions?"
   - "Summarize the infrastructure requirements"

GitHub Copilot will use the markdown content as context to provide accurate answers based on your documentation.

## Complete Example Workflow

```bash
# 1. Upload your PDF to the pdfs/ directory
#    (drag & drop architecture.pdf into pdfs/ folder)

# 2. Convert it to markdown
python convert_pdf.py pdfs/architecture.pdf

# Output: ✓ Successfully converted to: docs/architecture.md

# 3. Open docs/architecture.md in your editor

# 4. Ask Copilot: "What are the main components in this architecture?"
```

## Features

- **PDF Text Extraction**: Extracts text content from PDF files
- **Markdown Conversion**: Converts PDFs to well-formatted markdown
- **Copilot-Friendly**: Output is optimized for GitHub Copilot to understand and query
- **Page Tracking**: Maintains page numbers for reference
- **Automated Workflow**: Simple command-line interface

## Repository Structure

```
exmgmt/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── convert_pdf.py        # PDF to Markdown converter
├── pdfs/                 # 📁 Upload your PDF files here
│   └── README.md         # Upload instructions
├── docs/                 # 📄 Converted markdown files (for Copilot)
│   └── README.md         # Documentation guide
└── .gitignore           # Git ignore rules
```

## How It Works

1. **Input**: You provide a PDF file (e.g., exported from Confluence)
2. **Processing**: The script extracts text from each page
3. **Output**: Creates a markdown file with:
   - Document title
   - Metadata (source file, date)
   - Page-by-page content
4. **Integration**: GitHub Copilot can read and understand the markdown content

## Tips for Best Results

- **Use descriptive filenames**: Name your PDFs clearly (e.g., `api-architecture.pdf`)
- **Keep documents focused**: Smaller, focused documents work better than large ones
- **Review the output**: Check the generated markdown to ensure text was extracted correctly
- **Commit to repository**: Add the markdown files to version control so they're available in your workspace

## Troubleshooting

### "PyPDF2 is not installed"
Run: `pip install -r requirements.txt`

### Text extraction is garbled
Some PDFs (especially scanned documents or those with complex formatting) may not extract cleanly. Try:
- Ensuring the PDF has selectable text (not a scanned image)
- Simplifying the PDF formatting before export
- Using OCR tools for scanned documents before conversion

### Copilot isn't using the document content
Make sure:
- The markdown file is in your workspace
- You have the file open in your editor
- You're asking specific questions related to the content

## Contributing

Feel free to submit issues or pull requests to improve the PDF conversion process.

## License

MIT License - feel free to use and modify for your needs.
# PDFs Directory

## Where to Upload Your PDFs

**Place your PDF files in this directory** (`pdfs/`) before converting them to markdown.

## Steps to Process a PDF

1. **Upload your PDF here**: Place your PDF file in this `pdfs/` directory
   - Example: `pdfs/architecture-diagram.pdf`
   - Example: `pdfs/confluence-export.pdf`

2. **Run the conversion script** from the repository root:
   ```bash
   python convert_pdf.py pdfs/your-file.pdf
   ```

3. **Find the output**: The markdown file will be created in the `docs/` directory
   - Input: `pdfs/architecture-diagram.pdf`
   - Output: `docs/architecture-diagram.md`

4. **Use with Copilot**: Open the markdown file and ask questions!

## Example Workflow

```bash
# 1. Place your PDF in this directory (you can drag & drop or upload via GitHub web interface)
# Your file: pdfs/system-architecture.pdf

# 2. Convert it from the repository root
python convert_pdf.py pdfs/system-architecture.pdf

# 3. Open the result
# File created: docs/system-architecture.md

# 4. Ask GitHub Copilot questions about it!
```

## Note

- PDF files in this directory are **not committed to git** (they're in .gitignore)
- Only the converted markdown files are tracked in version control
- This keeps the repository lean while preserving the documentation content

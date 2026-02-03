# Quick Start Guide

## Where to Upload Your PDF

**Answer: Upload to the `pdfs/` directory**

You can upload your PDF in three ways:

### Option 1: Via GitHub Web Interface (Easiest)
1. Go to https://github.com/matthewkafel/exmgmt/tree/main/pdfs
2. Click "Add file" → "Upload files"
3. Drag and drop your PDF or click to browse
4. Commit the upload

### Option 2: In Your Local Repository
1. Navigate to the repository folder on your computer
2. Place the PDF in the `pdfs/` folder:
   ```
   exmgmt/pdfs/your-document.pdf
   ```

### Option 3: Using Git Commands
```bash
# Copy your PDF to the pdfs directory
cp /path/to/your/document.pdf exmgmt/pdfs/

# The PDF won't be committed (it's in .gitignore)
# You'll convert it to markdown next
```

## What Happens Next?

After uploading your PDF to `pdfs/`:

1. **Convert it to markdown:**
   ```bash
   python convert_pdf.py pdfs/your-document.pdf
   ```

2. **Find the output:**
   - Your markdown file will be in `docs/your-document.md`

3. **Use with Copilot:**
   - Open `docs/your-document.md` in your editor
   - Ask Copilot questions about the content

## Important Notes

- ✅ PDFs go in `pdfs/` directory
- ✅ Markdown files are created in `docs/` directory
- ✅ PDFs are NOT committed to git (saves space)
- ✅ Markdown files ARE committed (for Copilot to read)

## Example

```bash
# 1. You upload: pdfs/architecture.pdf
# 2. You run: python convert_pdf.py pdfs/architecture.pdf
# 3. You get: docs/architecture.md
# 4. You open docs/architecture.md and ask Copilot questions!
```

Need help? Check the main [README.md](../README.md) for detailed instructions.

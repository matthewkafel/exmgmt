# Documentation

This directory contains processed documentation files converted from PDFs.

## How to add documentation

1. **Place your PDF** in the `pdfs/` directory (one level up from here)
2. **Run the conversion script** from the repository root:
   ```bash
   python convert_pdf.py pdfs/your-file.pdf
   ```
3. The markdown version will be automatically saved in this `docs/` directory
4. Commit the markdown file to the repository
5. GitHub Copilot can now answer questions about the content

## Using with GitHub Copilot

Once the markdown files are in this directory:

1. Open any markdown file in your editor
2. Use GitHub Copilot Chat to ask questions about the content
3. Examples:
   - "What are the main components described in this architecture?"
   - "Explain the authentication flow"
   - "What databases are mentioned in this document?"

Copilot will use the content in these files as context for answering your questions.

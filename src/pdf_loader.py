import fitz  # pymupdf


def load_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        Extracted text as a string.
    """
    document = fitz.open(pdf_path)
    text = ""
    for page in document:
        text += page.get_text()
    document.close()
    return text


def load_document(file_path: str) -> str:
    """
    Load text from either a TXT or PDF file.

    Args:
        file_path: Path to the file.

    Returns:
        Extracted text as a string.
    """
    if file_path.endswith(".pdf"):
        return load_pdf(file_path)
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
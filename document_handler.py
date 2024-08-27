from docx import Document
import PyPDF2

def extract_text_from_pdf(file_path):
    """
    Extracts and returns the text from a PDF file.
    
    Parameters:
    file_path (str): The path to the PDF file.
    
    Returns:
    str: The extracted text.
    """
    pdf_text = []
    
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            pdf_text.append(page.extract_text())
    
    return '\n'.join(pdf_text)


def extract_text_from_docx(file_path):
    """
    Extracts and returns the text from a .docx file.
    
    Parameters:
    file_path (str): The path to the .docx file.
    
    Returns:
    str: The extracted text.
    """
    doc = Document(file_path)
    full_text = []

    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)

    return '\n'.join(full_text)

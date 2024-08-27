from docx import Document
import PyPDF2
import os


def extract_text_from_pdf(file_path):
    """
    Extracts and returns the text from a PDF file.

    Parameters:
    file_path (str): The path to the PDF file.

    Returns:
    str: The extracted text.
    """
    pdf_text = []

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            pdf_text.append(page.extract_text())

    return "\n".join(pdf_text)


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

    return "\n".join(full_text)


def extract_text_from_txt(file_path):
    """
    Extracts and returns the text from a plain text (.txt) file.

    Parameters:
    file_path (str): The path to the .txt file.

    Returns:
    str: The extracted text.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."
    except Exception as e:
        return f"An error occurred: {e}"


def extract_text(file_path):
    """
    Extracts and returns the text from a file based on its extension (.pdf, .docx, .txt).

    Parameters:
    file_path (str): The path to the file.

    Returns:
    str: The extracted text, or an error message if the file type is unsupported or an error occurs.
    """
    # Determine the file extension
    _, file_extension = os.path.splitext(file_path)

    # Call the appropriate function based on the file extension
    if file_extension.lower() == ".pdf":
        return extract_text_from_pdf(file_path)
    elif file_extension.lower() == ".docx":
        return extract_text_from_docx(file_path)
    elif file_extension.lower() == ".txt":
        return extract_text_from_txt(file_path)
    else:
        return f"Error: Unsupported file type '{file_extension}'"


def create_txt_file_and_write_text_chunk(text_chunk, filename):
    """
    Creates a .txt file and writes the given text chunk to it.

    Parameters:
    text_chunk (str): The text chunk to write to the file.
    filename (str): The name of the file to create.

    Returns:
    str: The path to the created file.
    """
    try:
        for text in text_chunk:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(text)
        return f"File created successfully: {filename}"
    except Exception as e:
        return f"An error occurred: {e}"

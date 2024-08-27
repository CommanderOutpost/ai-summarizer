def split_text(text, max_length, tolerance=5):
    """
    Splits text into chunks with a specified maximum length.
    
    Parameters:
    text (str): The input text to be split.
    max_length (int): The maximum length of each chunk.
    tolerance (int): The allowed excess length beyond max_length without splitting. Default is 5.
    
    Returns:
    list: A list of text chunks.
    """
    if len(text) <= max_length + tolerance:
        return [text]
    
    chunks = []
    while len(text) > max_length + tolerance:
        split_index = max_length
        chunks.append(text[:split_index])
        text = text[split_index:]
    
    chunks.append(text)  # Add the remaining text as the last chunk
    return chunks

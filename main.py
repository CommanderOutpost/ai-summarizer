from document_handler import extract_text, create_txt_file_and_write_text_chunk
from text_handler import split_text
from summarizer import summarize_text
from quizzer import create_quiz, answer_quiz

text = extract_text("./test_files/ELCT 304 CIRCUIT DESIGN AND TESTING CHAPTER FIVE.docx")
print(text)
print()
splitted_text = split_text(text, 4000)
print(splitted_text)
print()
summarized_text_chunks = summarize_text(splitted_text)
print(summarized_text_chunks)
print()
quiz_array = create_quiz(summarized_text_chunks)
print(quiz_array)
print()
answer_array = answer_quiz(summarized_text_chunks, quiz_array)
print(answer_array)
print()
summary_file_path = create_txt_file_and_write_text_chunk(summarized_text_chunks, "summary.txt")
print(summary_file_path)
print()
quiz_file_path = create_txt_file_and_write_text_chunk(quiz_array, "quiz.txt")
print(quiz_file_path)
print()
answer_file_path = create_txt_file_and_write_text_chunk(answer_array, "answer.txt")
print(answer_file_path)
print()

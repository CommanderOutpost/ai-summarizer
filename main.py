from document_handler import extract_text, create_txt_file_and_write_text_chunk, create_zip_with_files
from text_handler import split_text
from summarizer import summarize_text
from quizzer import create_quiz, answer_quiz

text = extract_text("./test_files/ELCT 304 CIRCUIT DESIGN AND TESTING CHAPTER ONE.docx")
splitted_text = split_text(text, 4000)
summarized_text_chunks = summarize_text(splitted_text)
quiz_array = create_quiz(summarized_text_chunks)
answer_array = answer_quiz(summarized_text_chunks, quiz_array)
summary_file_path = create_txt_file_and_write_text_chunk(summarized_text_chunks, "summary.txt")
quiz_file_path = create_txt_file_and_write_text_chunk(quiz_array, "quiz.txt")
answer_file_path = create_txt_file_and_write_text_chunk(answer_array, "answer.txt")
create_zip_with_files(["summary.txt", "quiz.txt", "answer.txt"], "output", "output")
print("Process completed successfully!")
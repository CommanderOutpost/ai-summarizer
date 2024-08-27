from openai import OpenAI
import os, dotenv

dotenv.load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def create_quiz(summary_chunks, model="gpt-4o-mini"):
    """
    Uses OpenAI's language model to create quiz for given text.
    """

    quiz_array = []

    system_prompt = """You are a master quiz creator, you will be given text and your job would be to create a quiz for the text, you will not provide the answer for the text."""

    for i, chunk in enumerate(summary_chunks):

        prompt = f"The text to create a quiz for is:\n{chunk}\n\n Your quiz:"
        quiz = (
            openai_client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
                ],
            )
            .choices[0]
            .message.content
        )

        quiz_array.append(quiz)

    return quiz_array


def answer_quiz(summary_chunks, quiz_array, model="gpt-4o-mini"):
    """
    Uses OpenAI's language model to answer quiz given the original text.
    """

    answer_array = []

    system_prompt = """You are a master quiz solver, you will be given a quiz and the material where it was gotten from and you will return only the answers of that quiz."""

    for i, chunk in enumerate(summary_chunks):

        prompt = f"The text where the quiz was gotten from is:\n{chunk}\n\nThe quiz is:\n{quiz_array[i]}\n\n The answers:"
        answers = (
            openai_client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
                ],
            )
            .choices[0]
            .message.content
        )

        answer_array.append(answers)

    return answer_array
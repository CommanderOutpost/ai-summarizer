from openai import OpenAI
import os, dotenv

dotenv.load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_text(text_chunks, model="gpt-4o-mini"):
    """
    Uses OpenAI's language model to summarize text.
    """
    
    summary_array = []

    system_prompt = """You are a master notes summarizer. You will be given text and your job would be to provide an understanding text that summarizes the given text. You will also be given the
    previous text that you summarized before and the text that was summarized."""
    
    for i, chunk in enumerate(text_chunks):
        previous_text = text_chunks[i - 1] if i > 0 else "There is no previous text."
        previous_summary = summary_array[i - 1] if i > 0 else "There is no previous summary."
        prompt = f"The previous text was:\n{previous_text}\n\nThe previous summary was:\n{previous_summary}\n\nThe text to summarize is:\n{chunk}\n\n Your summary:"
        explanation = openai_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
        ).choices[0].message.content

        summary_array.append(explanation)
    

    return summary_array

from groq import Groq

from src.utils.config import (
    GROQ_API_KEY
)


def generate_llm_insights(prompt):

    client = Groq(
        api_key=GROQ_API_KEY
    )

    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.5
    )

    insights = (
        response
        .choices[0]
        .message.content
    )

    return insights
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

st.title("JANVIQ AI")
st.subheader("IAM Knowledge Assistant")


def search_knowledge(question):

    with open("knowledge.txt", "r", encoding="utf-8") as f:
        knowledge = f.read()

    question_words = question.lower().split()

    results = []

    for line in knowledge.split("\n"):

        score = 0

        for word in question_words:

            if word in line.lower():
                score += 1

        if score > 0:
            results.append((score, line))

    results.sort(reverse=True)

    context = "\n".join([r[1] for r in results[:20]])

    return context


question = st.text_input("Ask your question")

if question:

    with st.spinner("Searching OIM Knowledge Base..."):

        context = search_knowledge(question)

    with st.spinner("Generating Answer..."):

        prompt = f"""
You are an Oracle Identity Manager expert.

Use the following OIM documentation context to answer the user's question.

Context:
{context}

Question:
{question}

Give a professional and accurate answer based on the documentation.
"""

        response = client.responses.create(
            model="gpt-5.5",
            input=prompt
        )

        st.write(response.output_text)
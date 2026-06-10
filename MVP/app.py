import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from citation_search import search_knowledge_with_citation
import os


# Load environment variables
load_dotenv()


# OpenAI Client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# UI
st.title("🚀 JANVIQ AI")
st.subheader("Enterprise IAM Knowledge Assistant")


question = st.text_input(
    "Ask your IAM question"
)


if question:

    with st.spinner("Searching verified knowledge..."):

        results = search_knowledge_with_citation(
            question
        )


    if not results:

        st.warning(
            "No relevant documentation found."
        )

    else:

        # Build context for GPT
        context = ""

        for item in results:

            context += f"""
Document: {item['document']}
Page: {item['page']}

Content:
{item['content']}

----------------------
"""


        with st.spinner("Generating expert answer..."):

            prompt = f"""
You are JANVIQ AI, an enterprise IAM expert.

Use only the documentation provided below.

Documentation:
{context}


User Question:
{question}


Instructions:
- Give a professional IAM answer.
- Do not make up information.
- Use the documentation evidence.
- Keep the answer clear and structured.
"""


            response = client.responses.create(
                model="gpt-5.5",
                input=prompt
            )


        # AI Answer
        st.markdown(
            "## 🤖 JANVIQ AI Answer"
        )

        st.write(
            response.output_text
        )


        # Citations
        st.markdown(
            "## 📚 Sources"
        )


        for item in results:

            st.write(
                f"📄 {item['document']} | Page {item['page']}"
            )
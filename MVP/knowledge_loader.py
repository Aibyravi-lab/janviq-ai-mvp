from pypdf import PdfReader
import os

knowledge = ""

folder_path = "KnowledgeBase"

for file in os.listdir(folder_path):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(folder_path, file)

        try:

            reader = PdfReader(pdf_path)

            for page in reader.pages:

                text = page.extract_text()

                if text:
                    knowledge += text + "\n"

        except:
            pass

with open("knowledge.txt", "w", encoding="utf-8") as f:
    f.write(knowledge)

print("Knowledge Base Created")
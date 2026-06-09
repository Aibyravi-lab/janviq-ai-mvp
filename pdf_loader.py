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

            print(f"Loaded: {file}")

        except Exception as e:
            print(f"Error reading {file}: {e}")

print("\n\nTOTAL TEXT LOADED")
print(len(knowledge))
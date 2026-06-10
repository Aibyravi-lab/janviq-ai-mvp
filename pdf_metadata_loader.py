from pypdf import PdfReader
import os
import json


knowledge_chunks = []

folder_path = "KnowledgeBase"


for file in os.listdir(folder_path):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(folder_path, file)

        try:
            reader = PdfReader(pdf_path)

            print(f"Processing: {file}")

            for page_number, page in enumerate(reader.pages, start=1):

                text = page.extract_text()

                if text:

                    chunk = {
                        "document": file,
                        "page": page_number,
                        "content": text.strip()
                    }

                    knowledge_chunks.append(chunk)

            print(f"Completed: {file}")

        except Exception as e:
            print(f"Error reading {file}: {e}")


with open(
    "knowledge_chunks.json",
    "w",
    encoding="utf-8"
) as output_file:

    json.dump(
        knowledge_chunks,
        output_file,
        indent=4,
        ensure_ascii=False
    )


print("\nJANVIQ AI v0.2 Metadata Extraction Complete")
print(f"Total chunks created: {len(knowledge_chunks)}")
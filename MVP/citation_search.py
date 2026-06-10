import json


STOP_WORDS = {
    "what", "is", "are", "the",
    "a", "an", "of", "to",
    "in", "on", "for", "how",
    "does", "do"
}


JUNK_CONTENT = [
    "table of contents",
    "list of figures",
    "list of tables",
    "preface",
    "index"
]


def search_knowledge_with_citation(question):

    with open(
        "knowledge_chunks.json",
        "r",
        encoding="utf-8"
    ) as file:

        knowledge_chunks = json.load(file)


    # Clean question
    question_words = []

    for word in question.lower().split():

        if word not in STOP_WORDS:
            question_words.append(word)


    results = []


    for chunk in knowledge_chunks:

        content = chunk["content"].lower()

        # Ignore junk pages
        skip = False

        for junk in JUNK_CONTENT:

            if junk in content:
                skip = True
                break


        if skip:
            continue


        score = 0


        # Frequency-based scoring
        for word in question_words:

            score += content.count(word)


        # Exact phrase bonus
        cleaned_question = " ".join(question_words)

        if cleaned_question in content:
            score += 10


        # OIM relevance bonus
        if "oim" in question.lower():

            if (
                "oracle identity manager" in content
                or "oim" in content
            ):
                score += 2


        if score > 0:

            results.append({
                "score": score,
                "document": chunk["document"],
                "page": chunk["page"],
                "content": chunk["content"]
            })


    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    return results[:5]
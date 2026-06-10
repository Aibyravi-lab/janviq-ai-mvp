from citation_search import search_knowledge_with_citation


question = input("Ask Question: ")


results = search_knowledge_with_citation(question)


print("\nJANVIQ AI Citation Results\n")


for item in results:

    print("----------------------------------")

    print("Score:", item["score"])

    print("Document:", item["document"])

    print("Page:", item["page"])

    print("\nContent:")

    print(item["content"][:300])

    print("\n")
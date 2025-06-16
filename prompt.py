import elasticsearch

URL = 'http://localhost:9200'

es = elasticsearch.Elasticsearch(URL)
query = {
    "query": {
        "bool": {
            "must": [
                {
                    "multi_match": {
                        "query": "How do copy a file to a Docker container?",
                        "type": "best_fields",
                        "fields": [
                            "question^4",
                            "text",
                        ],
                    },
                },
                {"term": {"course": "machine-learning-zoomcamp"}},
            ],
        }
    },
    "size": 3,
}

response = es.search(index="hw1_index", body=query)

context_template = """
Q: {question}
A: {text}
""".strip()

context_entries = []
hits = response["hits"]["hits"]
for hit in hits:
    question = hit["_source"]["question"]
    text = hit["_source"]["text"]
    context_entries.append(context_template.format(question=question, text=text))

context = "\n\n".join(context_entries)

prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
""".strip()

question = "How do copy a file to a Docker container?"
prompt = prompt_template.format(question=question, context=context)

print(f"Q5 - Length of the resulting prompt: {len(prompt)}")

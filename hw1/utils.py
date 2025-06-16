import elasticsearch

URL = 'http://localhost:9200'

def get_elasticsearch_client():
    return elasticsearch.Elasticsearch(URL)

def search_docker_questions(size=3):
    """Search for Docker container questions in machine-learning-zoomcamp"""
    es = get_elasticsearch_client()
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
        "size": size,
    }
    return es.search(index="hw1_index", body=query)

def build_context_from_hits(hits):
    """Build context string from search hits"""
    context_template = """
Q: {question}
A: {text}
""".strip()
    
    context_entries = []
    for hit in hits:
        question = hit["_source"]["question"]
        text = hit["_source"]["text"]
        context_entries.append(context_template.format(question=question, text=text))
    
    return "\n\n".join(context_entries)

def build_prompt(context, question="How do copy a file to a Docker container?"):
    """Build the full prompt using context and question"""
    prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
""".strip()
    
    return prompt_template.format(question=question, context=context)
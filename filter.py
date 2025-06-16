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

print("Q4 - Top 3 results:")
hits = response["hits"]["hits"]
for idx, hit in enumerate(hits, 1):
    q = hit["_source"].get("question")
    print(f"{idx}. {q}")

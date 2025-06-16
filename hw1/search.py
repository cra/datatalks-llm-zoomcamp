import elasticsearch

URL = 'http://localhost:9200'

es = elasticsearch.Elasticsearch(URL)
query = {
    "query": {
        "multi_match": {
            "query": "How do execute a command on a Kubernetes pod?",
            "type": "best_fields",
            "fields": ["question^4", "text"],
        }
    }
}

response = es.search(index="hw1_index", body=query)

for hit in response["hits"]["hits"]:
    print(f"Score: {hit['_score']}, Content: {hit['_source']['text']}")

import requests
import elasticsearch

URL = 'http://localhost:9200'

# create index
es = elasticsearch.Elasticsearch(URL)
# mapping = {"mappings": {"properties": {"course": {"type": "keyword"}}}}
# es.indices.create(index="hw1_index", body=mapping)

# load data
docs_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main/01-intro/documents.json?raw=1'
docs_response = requests.get(docs_url)
documents_raw = docs_response.json()

documents = []

for course in documents_raw:
    course_name = course['course']

    for doc in course['documents']:
        doc['course'] = course_name
        documents.append(doc)

# index data
for doc in documents:
    es.index(index="hw1_index", document=doc)

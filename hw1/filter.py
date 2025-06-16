from utils import search_docker_questions

response = search_docker_questions()
hits = response["hits"]["hits"]

print("Q4 - Top 3 results:")
for idx, hit in enumerate(hits, 1):
    q = hit["_source"].get("question")
    print(f"{idx}. {q}")

if len(hits) >= 3:
    print(f"\nThe 3rd question is: {hits[2]['_source']['question']}")
else:
    print(f"\nOnly {len(hits)} results found")
from utils import search_docker_questions, build_context_from_hits, build_prompt

response = search_docker_questions()
hits = response["hits"]["hits"]
context = build_context_from_hits(hits)
prompt = build_prompt(context)

print(f"Q5 - Length of the resulting prompt: {len(prompt)}")
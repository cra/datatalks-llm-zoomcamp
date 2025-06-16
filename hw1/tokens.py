import tiktoken
from utils import search_docker_questions, build_context_from_hits, build_prompt

response = search_docker_questions()
hits = response["hits"]["hits"]
context = build_context_from_hits(hits)
prompt = build_prompt(context)

encoding = tiktoken.encoding_for_model("gpt-4o")
tokens = encoding.encode(prompt)

print(f"Q6 - Number of tokens in the prompt: {len(tokens)}")
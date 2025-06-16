Create dir with correct permissions
```bash
mkdir elastic_data
chown -R 1000:1000 !$
chmod -R 770 !$
```

run elasticsearch in docker 
```bash
docker run -d --name es01 \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    -v $(pwd)/elastic_data:/usr/share/elasticsearch/data \
    docker.elastic.co/elasticsearch/elasticsearch:8.17.6
```

Run homework 1 scripts:
```bash
uv run hw1/get_data.py
uv run hw1/search.py      # q3
uv run hw1/filter.py      # q4  
uv run hw1/prompt.py      # q5
uv run hw1/tokens.py      # q6
```

Put elasticsearch to sleep
```bash
docker stop es01
```


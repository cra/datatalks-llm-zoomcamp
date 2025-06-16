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

Run python script:
```bash
uv run get_data.py
uv run search.py  # q3
uv run filter.py  # q4
```


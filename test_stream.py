import requests

url = "http://127.0.0.1:8000/chat-stream"

with requests.post(url, json={"message": "hello"}, stream=True) as r:
    print("STATUS:", r.status_code)
    print("HEADERS:", r.headers)

    for chunk in r.iter_content(chunk_size=1):
        if chunk:
            print(chunk.decode(errors="ignore"), end="", flush=True)
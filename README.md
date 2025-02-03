# vllm-client



## Running locally

Client can be run locally with poetry.

```
poetry install
```

## Sources
[https://dzone.com/articles/building-a-dynamic-chat-application-setting-up-cha](Setting up a chatbot with FastAPI)




## Available endpoints

From logs while starting vllm service:
```
INFO 02-03 05:14:27 launcher.py:19] Available routes are:
INFO 02-03 05:14:27 launcher.py:27] Route: /openapi.json, Methods: HEAD, GET
INFO 02-03 05:14:27 launcher.py:27] Route: /docs, Methods: HEAD, GET
INFO 02-03 05:14:27 launcher.py:27] Route: /docs/oauth2-redirect, Methods: HEAD, GET
INFO 02-03 05:14:27 launcher.py:27] Route: /redoc, Methods: HEAD, GET
INFO 02-03 05:14:27 launcher.py:27] Route: /health, Methods: GET
INFO 02-03 05:14:27 launcher.py:27] Route: /ping, Methods: GET, POST
INFO 02-03 05:14:27 launcher.py:27] Route: /tokenize, Methods: POST
INFO 02-03 05:14:27 launcher.py:27] Route: /detokenize, Methods: POST
INFO 02-03 05:14:27 launcher.py:27] Route: /v1/models, Methods: GET
INFO 02-03 05:14:27 launcher.py:27] Route: /version, Methods: GET
INFO 02-03 05:14:27 launcher.py:27] Route: /v1/chat/completions, Methods: POST
INFO 02-03 05:14:27 launcher.py:27] Route: /v1/completions, Methods: POST
INFO 02-03 05:14:27 launcher.py:27] Route: /v1/embeddings, Methods: POST
INFO 02-03 05:14:27 launcher.py:27] Route: /pooling, Methods: POST
INFO 02-03 05:14:27 launcher.py:27] Route: /score, Methods: POST
INFO 02-03 05:14:27 launcher.py:27] Route: /v1/score, Methods: POST
INFO 02-03 05:14:27 launcher.py:27] Route: /rerank, Methods: POST
INFO 02-03 05:14:27 launcher.py:27] Route: /v1/rerank, Methods: POST
INFO 02-03 05:14:27 launcher.py:27] Route: /v2/rerank, Methods: POST
INFO 02-03 05:14:27 launcher.py:27] Route: /invocations, Methods: POST

```

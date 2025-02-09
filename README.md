# vllm-client



## Running locally

Client can be run locally with poetry.

```
poetry install
poetry run python <script>
```

<br>

## Sources

### Writing a chat application

[Setting up a chatbot with FastAPI](https://dzone.com/articles/building-a-dynamic-chat-application-setting-up-cha)

https://stocktistics.com/stocksaavy

https://github.com/troyscribner/stocknews

https://github.com/troyscribner/stocknews/blob/main/dashboard/pages/stocks/chatbox.py

https://www.dash-mantine-components.com/getting-started



### vLLM server

https://docs.vllm.ai/en/latest/getting_started/quickstart.html

[Enable reasoning with openai clients](https://docs.vllm.ai/en/latest/features/reasoning_outputs.html)

https://ploomber.io/blog/vllm-deploy/



### Communication with vLLM server - OpenAI API

https://platform.openai.com/docs/quickstart?language=python&example=completions

https://github.com/openai/openai-python/tree/main

https://stackoverflow.com/questions/76305207/openai-api-asynchronous-api-calls

https://docs.vllm.ai/en/stable/getting_started/examples/api_client.html

<br>
<br>

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

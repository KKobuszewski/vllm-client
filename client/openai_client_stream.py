"""
Sources: https://docs.vllm.ai/en/v0.5.3/getting_started/examples/openai_completion_client.html
"""

from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://10.0.1.3:8000/v1"

client = OpenAI(
    api_key=openai_api_key,      # defaults to os.environ.get("OPENAI_API_KEY")
    base_url=openai_api_base,
)

models = client.models.list()
print(models)
model = models.data[0].id

print('model:', model)

# Completion API
stream = False
completion = client.completions.create(
    model=model,
    prompt="Tienanmen masacre",
    echo=False,
    n=2,
    stream=stream,
    logprobs=3)

print("Completion results:")
if stream:
    for c in completion:
        print(c)
        print(c.choices[0].text)
else:
    print(completion)
    print(completion.choices[0].text)



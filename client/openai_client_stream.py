"""
Sources: https://docs.vllm.ai/en/v0.5.3/getting_started/examples/openai_completion_client.html
"""

from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

client = OpenAI(
    api_key=openai_api_key,      # defaults to os.environ.get("OPENAI_API_KEY")
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id

# Completion API
stream = False
completion = client.completions.create(
    model=model,
    prompt="A robot may not injure a human being",
    echo=False,
    n=2,
    stream=stream,
    logprobs=3)

print("Completion results:")
if stream:
    for c in completion:
        print(c)
else:
    print(completion)

import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI((
    api_key=openai_api_key,      # defaults to os.environ.get("OPENAI_API_KEY")
    base_url=openai_api_base,
)


async def main():
    stream = await client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")


asyncio.run(main())


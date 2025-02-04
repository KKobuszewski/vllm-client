
import asyncio
from openai import AsyncOpenAI


# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://10.0.1.3:8000/v1"

client = AsyncOpenAI(
    api_key=openai_api_key,      # defaults to os.environ.get("OPENAI_API_KEY")
    base_url=openai_api_base,
)

async def get_models_async(client: AsyncOpenAI) -> list[str]:
    models = await client.models.list()
    return [m.id for m in models.data]

models = asyncio.run(get_models_async(client))
model = models[0]
print(f'model: {model}\n')

async def main(prompt="Say this is a test"):
    stream = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    print('prompt:\n"""')
    print(prompt)
    print('"""\n')
    print('response:\n"""')
    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
    print('\n"""\n')


asyncio.run(main())

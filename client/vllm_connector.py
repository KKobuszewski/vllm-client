import asyncio
from openai import OpenAI, AsyncOpenAI



def get_models(client: AsyncOpenAI) -> list[str]:
    models = client.models.list()
    return [m.id for m in models.data]

# TODO: decorator for asyncio.run?
async def get_models_async(client: AsyncOpenAI) -> list[str]:
    models = await client.models.list()
    return [m.id for m in models.data]



class vllmConnector:
    def __init__(self, api_url: str, api_key: str = "EMPTY"):
        self.vllm_api_key  = api_key
        self.vllm_api_url = api_url
        
        self.openai_client = OpenAI(
            api_key=self.vllm_api_key,      # defaults to os.environ.get("OPENAI_API_KEY")
            base_url=self.vllm_api_url,
        )
        
        self.models = get_models(self.openai_client)
        self.model = self.models[0]
    
    def ask(self, prompt: str):
        stream = self.openai_client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )
        
        response = [ chunk.choices[0].delta.content or "" for chunk in stream]
        
        return response


class vllmAsyncConnector:
    def __init__(self, api_url: str, api_key: str = "EMPTY"):
        self.vllm_api_key  = api_key
        self.vllm_api_url = api_url
        
        self.openai_client = AsyncOpenAI(
            api_key=self.vllm_api_key,      # defaults to os.environ.get("OPENAI_API_KEY")
            base_url=self.vllm_api_url,
        )
        
        self.models = asyncio.run( get_models_async(self.openai_client) )
        self.model = self.models[0]
    
    async def ask(self, prompt: str):
        stream = await self.openai_client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )
        
        response = []
        async for chunk in stream:
            response.append( chunk.choices[0].delta.content or "" )
        
        return response
    
    #@property
    #def models(self):
        #return self.models

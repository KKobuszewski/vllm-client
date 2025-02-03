"""
Example Python client for `vllm.entrypoints.api_server`

Source: https://docs.vllm.ai/en/stable/getting_started/examples/api_client.html

NOTE: The API server is used only for demonstration and simple performance
benchmarks. It is not intended for production use.
For production use, `vllm serve` and the OpenAI client API is recommended.
"""

import argparse
import json
from typing import Iterable, List

import requests


def clear_line(n: int = 1) -> None:
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for _ in range(n):
        print(LINE_UP, end=LINE_CLEAR, flush=True)


def post_http_request(prompt: str,
                      api_url: str,
                      n: int = 1,
                      temperature: float = 0.5,
                      stream: bool = False) -> requests.Response:
    headers = {"User-Agent": "Test Client"}
    pload = {
        #"prompt": prompt,
        "messages": [{
            "role": "user",
            "name": "string",
            "content": prompt
        }],
        "model":"deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
        "n": n,
        "use_beam_search": False,
        "temperature": temperature,
        "max_tokens": 16,
        "max_completion_tokens": 16,
        "stream": stream,
    }
    if n > 1:
        pload["use_beam_search"] = True
    response = requests.post(api_url,
                             headers=headers,
                             json=pload,
                             stream=stream)
    return response


def get_streaming_response(response: requests.Response) -> Iterable[List[str]]:
    for chunk in response.iter_lines(chunk_size=8192,
                                     decode_unicode=False,
                                     delimiter=b"\0"):
        if chunk:
            data = json.loads(chunk.decode("utf-8"))
            output = data["text"]
            yield output


def get_response(response: requests.Response) -> List[str]:
    data = json.loads(response.content)
    try:
        error_code = int(data['code']) # if there's correct response this will generate KeyError
        for key, val in data.items():
            if key == 'message':
                print('message :',type(val))
                print(val)
                #for k, v in json.loads(val.replace('[','"').replace(']','"')).items():
                #    print(k,v)
                print()
            else:
                print(key,':',val)
        raise Exception('BadRequestError')
    except KeyError:
        output = data["choices"]
        return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--prompt", type=str, default="Say this is a test")
    parser.add_argument("--stream", action="store_true")
    args = parser.parse_args()
    prompt = args.prompt
    api_url = f"http://{args.host}:{args.port}/v1/chat/completions"
    n = args.n
    stream = args.stream

    print(f"Prompt: {prompt!r}\n", flush=True)
    print(f"Requesting on {api_url}\nstream: {args.stream}\n")
    response = post_http_request(prompt, api_url, n, stream)
    
    if stream:
        num_printed_lines = 0
        for h in get_streaming_response(response):
            clear_line(num_printed_lines)
            num_printed_lines = 0
            for i, line in enumerate(h):
                num_printed_lines += 1
                print(f"Beam candidate {i}: {line!r}", flush=True)
    else:
        output = get_response(response)
        for i, line in enumerate(output):
            line = line['message']
            print(f"Beam candidate {i}: {line!r}", flush=True)

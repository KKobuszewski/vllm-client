payload = {
    "messages": [{
        "role": "user",
        "name": "string",
        "content": "string"
    }],
    "model": "string",
    "frequency_penalty": 0,
    "logit_bias": {
        "property1": 0,
        "property2": 0
    },
    "logprobs": False,
    "top_logprobs": 0,
    "max_tokens": 0,
    "max_completion_tokens": 0,
    "n": 1,
    "presence_penalty": 0,
    "response_format": {
        "type": "text",
        "json_schema": {}
    },
    "seed": -9223372036854776000,
    "stop": "string",
    "stream": True,
    "stream_options": {
        "include_usage": True,
        "continuous_usage_stats": False
    },
    "temperature": 0,
    "top_p": 0,
    "tools": [ {} ],
    "tool_choice": "none",
    "parallel_tool_calls": False,
    "user": "string",
    "best_of": 0,
    "use_beam_search": False,
    "top_k": 0,
    "min_p": 0,
    "repetition_penalty": 0,
    "length_penalty": 1,
    "stop_token_ids": [ 0 ],
    "include_stop_str_in_output": False,
    "ignore_eos": False,
    "min_tokens": 0,
    "skip_special_tokens": True,
    "spaces_between_special_tokens": True,
    "truncate_prompt_tokens": 1,
    "prompt_logprobs": 0,
    "echo": False,
    "add_generation_prompt": True,
    "continue_final_message": False,
    "add_special_tokens": False,
    "documents": [ {} ],
    "chat_template": "string",
    "chat_template_kwargs": {},
    "guided_json": "string",
    "guided_regex": "string",
    "guided_choice": [ "string" ],
    "guided_grammar": "string",
    "guided_decoding_backend": "string",
    "guided_whitespace_pattern": "string",
    "priority": 0,
    "request_id": "string",
    "logits_processors": [ "string" ]
}


if __name__ == '__main__':
    for msg in payload['messages']:
        print(msg['content'])

# source: https://hub.docker.com/r/vllm/vllm-openai/tags

# BUILDING IMAGE
# docker build --no-cache -t vllm-deepseek-server .

# RUNNING IMAGE
# docker run -p 8000:8000 --volume=/home/kkobuszewski/projects/LMMs:/root/.cache/huggingface --runtime nvidia --gpus all --ipc=host vllm-deepseek-server:latest
# docker run -p 8000:8000 --volume=/opt:/usr/src/app my_image --runtime nvidia --gpus all --ipc=host vllm-deepseek-server:latest
# docker run -it -p 8000:8000 --runtime nvidia --gpus all --ipc=host --entrypoint=/bin/bash vllm-deepseek-server:latest

FROM vllm/vllm-openai:v0.7.0

ENTRYPOINT ["vllm"]
CMD ["serve", "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",  "--tensor-parallel-size", "1",  "--max-model-len", "32768", "--enforce-eager"]

# NOTE:
# "--max-model-len", should be less than 79424
# The model's max seq len (131072) is larger than the maximum number of tokens
# that can be stored in KV cache (79424).
# Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine.




# NOTE:
# Here read about running vllm with many GPUs
# https://github.com/vllm-project/vllm/issues/7107

# NOTE:
# vLLM stores its models in the Hugging Face cache directory by default, 
# which is typically located at ~/.cache/huggingface. 
# You can change this location by setting the HF_HOME environment variable
# to your desired path. Would you like more details on how to configure this?



# Command to run basic image
# docker run --runtime nvidia --gpus all \
#     -v ~/.cache/huggingface:/root/.cache/huggingface \
#     -p 8000:8000 \
#     --env "HUGGING_FACE_HUB_TOKEN=<secret>" \
#     vllm/vllm-openai:latest \
#     --model mistralai/Mistral-7B-v0.1

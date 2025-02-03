# source: https://hub.docker.com/r/vllm/vllm-openai/tags

# docker build --no-cache -t vllm-deepseek-server .
# docker run --runtime nvidia --gpus all -p 8000:8000 --ipc=host vllm-deepseek-server:latest

FROM vllm/vllm-openai:v0.7.0

ENTRYPOINT ["vllm"]
CMD ["serve", "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",  "--tensor-parallel-size", "1",  "--max-model-len", "32768", "--enforce-eager"]

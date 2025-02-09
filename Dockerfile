# docker build -t vllm-client .
# docker build --no-cache -t vllm-client . 
# docker run --rm -it --entrypoint /bin/bash vllm-client
# docker run -d -p 8080:8050 vllm-client
# docker run -p$HOST_PORT:$DOCKER_PORT my_container

# one can predownload this image to avoid repeated downloads from dockerhub,
# cause at some point fees apply
#FROM python310 
FROM python@sha256:7a08d7bfedcbf05d15b2bff8f0c86db6dd06bcbaa74c915d2d5585dbd5ba65b0

# RUN apt-get update -y \
#     && apt-get -y install curl gnupg \
#     && echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
#     && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - \
#     && apt-get update -y \
#     && apt-get install google-cloud-cli -y --no-install-recommends \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*


# INSTALL DEPENDENCIES OF app.py IN THE IMAGE
WORKDIR /app
COPY app.py poetry.lock poetry.toml pyproject.toml ./

ENV POETRY_LOCATION=/opt/poetry
RUN python3 -m venv $POETRY_LOCATION \
    && $POETRY_LOCATION/bin/pip install --no-cache-dir --upgrade pip \
    && $POETRY_LOCATION/bin/pip install --no-cache-dir poetry==1.8.3 \
    && $POETRY_LOCATION/bin/poetry install --only=main \
    && rm -rf .poetry_cache

RUN mkdir -p ./dashboard
WORKDIR /app/dashboard
COPY ./dashboard/*.py ./
WORKDIR /app
RUN mkdir -p ./client
WORKDIR /app/client
COPY ./client/*.py ./
WORKDIR /app


# RUN app.py
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app"
EXPOSE 8050
ENTRYPOINT [ "python" ]
CMD ["app.py"]

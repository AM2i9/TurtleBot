# syntax=docker/dockerfile:1

FROM python:3.9.5-slim

# Set pip to have no saved cache
ENV PIP_NO_CACHE_DIR=false \
    POETRY_VIRTUALENVS_CREATE=false

# Install poetry
RUN pip install -U poetry

WORKDIR /bot

# Install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

# Copy rest of source code
COPY . .

ENTRYPOINT ["python3"]
CMD ["-m", "turtlebot"]
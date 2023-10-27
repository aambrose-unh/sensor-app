FROM python:3.10

ENV PATH="/root/.local/bin:$PATH"
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.5.1 && \
    apt-get update

COPY . .

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

EXPOSE 8000

#It is the command that will start and run the FastAPI application container
CMD ["uvicorn", "sensor_app_api.main:app", "--host", "0.0.0.0"]

FROM python:3.10

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.5.1 && \
    poetry config virtualenvs.create false

COPY . .

RUN poetry install

EXPOSE 8000
#It is the command that will start and run the FastAPI application container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
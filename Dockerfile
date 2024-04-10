FROM python:3.12.3-slim

RUN pip install poetry==1.8.2

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install

RUN apt-get update \
    && apt-get install -y \
    wkhtmltopdf

COPY markdown_to_pdf ./markdown_to_pdf

ENTRYPOINT ["poetry", "run", "python", "-m", "markdown_to_pdf.main"]
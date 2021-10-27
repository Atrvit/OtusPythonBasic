# docker build -t otus-homework-03:latest . && docker run -p 8000:8000 otus-homework-03:latest
FROM python:3.9-buster

ENV HOME=/root
ENV WORKDIR=/usr/src/app/

WORKDIR ${WORKDIR}

RUN python3 -m pip install --upgrade pip && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/1.1.2/get-poetry.py | python3
ENV PATH="${HOME}/.poetry/bin:${PATH}"


COPY poetry.lock pyproject.toml ${WORKDIR}

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

COPY main.py ${WORKDIR}

EXPOSE 8000

CMD ["uvicorn", "--host=0.0.0.0", "--port=8000", "main:app"]

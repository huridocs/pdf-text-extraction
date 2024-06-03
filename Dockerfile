FROM python:3.11-slim-bullseye

RUN apt-get update && apt-get -y -q --no-install-recommends install libgomp1 git pdftohtml

RUN mkdir -p /app/src

RUN addgroup --system python && adduser --system --group python
RUN chown -R python:python /app
USER python

ENV VIRTUAL_ENV=/app/.venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip --default-timeout=1000 install -r requirements.txt

WORKDIR /app

COPY ./src/. ./src


ENV PYTHONPATH "${PYTHONPATH}:/app/src"
ENV TRANSFORMERS_VERBOSITY=error
ENV TRANSFORMERS_NO_ADVISORY_WARNINGS=1


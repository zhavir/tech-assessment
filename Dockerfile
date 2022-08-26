FROM python:3.10 as base
RUN apt-get update -y && apt-get install -y libpq-dev gcc curl && rm -rf /var/lib/apt/lists/*
RUN groupadd -g 999 app
RUN useradd -m -r -u 999 -g app app
WORKDIR /src
RUN chown app /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY src/app /src/app

FROM base AS development
COPY requirements-dev.txt /src/
RUN pip install -r /src/requirements-dev.txt
COPY src/tests /src/tests
USER app
ENTRYPOINT ["pytest"]

FROM base AS production
EXPOSE 9001
USER app
ENV PYTHONPATH "${PYTHONPATH}:/"
ENTRYPOINT ["python", "app/main.py"]
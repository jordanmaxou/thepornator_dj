########################################################################################
FROM python:3.11-buster AS builder-base
RUN pip install poetry==1.8.4

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /home

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

########################################################################################
FROM python:3.11-slim-buster AS production

ENV SOURCE_VIRTUAL_ENV=/home/.venv \
    TARGET_VIRTUAL_ENV=/usr/local/bin/.venv \
    PATH="/usr/local/bin/.venv/bin:$PATH"

COPY --from=builder-base ${SOURCE_VIRTUAL_ENV} ${TARGET_VIRTUAL_ENV}

COPY entrypoint.sh /usr/sbin/entrypoint.sh

WORKDIR /home
COPY . .

ENTRYPOINT ["/usr/sbin/entrypoint.sh"]
CMD ["app"]

########################################################################################
FROM production AS development
CMD ["noop"]

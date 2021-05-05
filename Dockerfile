FROM python:3.9-slim as develop

RUN mkdir /workarea

COPY ./pyproject.toml ./poetry.lock[t] /workarea
WORKDIR /workarea

RUN python3.9 -m pip install --upgrade pip && \
    python3.9 -m pip install poetry \
    || exit 1

RUN poetry config virtualenvs.create false && poetry install

COPY . /staging
RUN cp -r /staging/* /workarea
RUN rm -rf /staging

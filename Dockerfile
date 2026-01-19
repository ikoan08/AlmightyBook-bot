# Stage 1: Builder
FROM python:3.12-slim-bookworm AS builder

# uvをマルチステージビルドでコピー
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /build

# pyproject.tomlとuv.lockをコピーして依存関係をインストール
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Stage 2: Runtime
FROM python:3.12-slim-bookworm AS runtime

RUN apt-get update && apt-get install -y --no-install-recommends \
    locales \
    && sed -i '/ja_JP.UTF-8/s/^# //g' /etc/locale.gen \
    && locale-gen \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV LANG=ja_JP.UTF-8 \
    LANGUAGE=ja_JP:ja \
    LC_ALL=ja_JP.UTF-8 \
    TZ=Asia/Tokyo \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/build/.venv/bin:$PATH"

RUN useradd --create-home --shell /bin/bash botuser

COPY --from=builder /build/.venv /build/.venv

WORKDIR /app
COPY --chown=botuser:botuser opt/ /app/

USER botuser

CMD ["python", "main.py"]

# AGENTS.md

## Cursor Cloud specific instructions

### Overview

This is a Django 5.0 e-commerce monolith ("Sales / LuxNexus") with a SQLite database. Single service — everything runs from `python3 manage.py runserver`.

### Key caveats

- The custom `User` model uses **email** as `USERNAME_FIELD` (no `username` field). To create users programmatically use `User.objects.create_superuser(email=..., password=..., name=...)`.
- `psycopg2` is in `requirements.txt` but the project uses **SQLite** — PostgreSQL is not needed at runtime. Building `psycopg2` requires system packages `libpq-dev` and `python3-dev`.
- `python` is not on PATH; use `python3` instead.
- pip installs to `~/.local` by default; ensure `~/.local/bin` is on PATH when running Django management commands via `django-admin`.

### Running the dev server

```bash
python3 manage.py runserver 0.0.0.0:8000
```

### Running checks and tests

```bash
python3 manage.py check      # Django system checks
python3 manage.py test        # Runs test suite (currently empty)
```

### Database migrations

```bash
python3 manage.py migrate
```

### Project structure

See `sales/settings.py` for Django config. Apps: `store` (core), `cart`, `api`. Templates in `templates/`, static assets in `static/`.

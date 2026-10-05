# Running and deploying the portfolio

## Local development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 127.0.0.1:8001
```

Open `http://127.0.0.1:8001/`. The development server reloads when Python files change.

## Pre-release checks

```bash
python manage.py check
python manage.py test
```

Review desktop and mobile layouts and verify project search, filters, Show more, empty results, project details, profile links, mobile navigation, and résumé downloading.

## Production setup

The following describes a future deployment; no public hosting service has been provisioned.

1. Choose a host supporting Python and Django, and install the project dependencies.
2. Set `DJANGO_DEBUG=0`, `DJANGO_SECRET_KEY` to a private stable value, and `DJANGO_ALLOWED_HOSTS` to the actual hostnames separated by commas.
3. Install and configure a production WSGI or ASGI server. The repository does not currently pin a production server dependency.
4. Run migrations and collect static assets:

   ```bash
   python manage.py migrate --noinput
   python manage.py collectstatic --noinput
   python manage.py check --deploy
   ```

5. Serve `staticfiles/` at `/static/` through the hosting platform or reverse proxy. Route dynamic requests to `config.wsgi:application` or `config.asgi:application`.
6. Configure HTTPS and platform-specific proxy settings. Review deployment-check output and configure secure cookies and redirects as appropriate to that hosting environment.
7. Verify the home page, static assets, résumé attachment, and navigation using the public URL.

Do not use Django's development server for public production traffic. GitHub Pages does not run a Django backend; this repository requires a Python-capable host for the current implementation.

## Publishing source changes

```bash
git status
git add <changed-files>
git commit -m "Describe the change"
git push origin main
```

Keep `.env`, `.venv/`, `db.sqlite3`, `staticfiles/`, temporary artifacts, and secrets out of commits. Pushing source changes updates the GitHub repository; deployment automation has not been configured.

## Updating content

Update `portfolio/data.py` and the page template, replace the original résumé asset when needed, and rerun the checks. Keep downloadable résumé details and displayed project information aligned.

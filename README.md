# Phyo Thet Paing — Django Portfolio

A responsive personal portfolio built from `PHYO_THETPAING_2026_09_19.pdf`, using Python/Django, HTML, CSS, and JavaScript. Includes the original résumé photo and PDF, all 41 résumé projects, project search, category filters, progressive browsing, expandable details, experience, skills, education, and email contact.

## Run locally

Python 3.12 or newer is required. From this directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 127.0.0.1:8001
```

Open http://127.0.0.1:8001/. Port 8001 is used because 8000 was occupied during development.

## Update the portfolio

- Edit `portfolio/data.py` for project, experience, skill, and education content.
- Edit `portfolio/templates/portfolio/home.html` for introductory text, contact details, and section structure.
- Edit `portfolio/static/portfolio/style.css` for colors, spacing, and responsive layouts.
- Edit `portfolio/static/portfolio/app.js` for filters, navigation, and clipboard behavior.
- Replace `portfolio/static/portfolio/assets/portrait.jpg` to update your photo.
- Replace `portfolio/static/portfolio/assets/resume.pdf` to update the downloadable CV.

Project illustrations are CSS graphics, not screenshots of client systems. Content is summarized from the provided résumé. The ambiguous phone number in the source was omitted; contact uses the source email. Email links open the visitor's email application, and the copy button copies the address. There is no message submission form or email delivery service.

The fonts load from Google Fonts when online, with local system font fallbacks. No frontend build tools are needed.

## Verify

```bash
python manage.py check
python manage.py test
```

Desktop and mobile browser checks covered 1440, 1024, 768, 390, and 320-pixel widths, project search, empty results, category filters, progressive loading, expanded details, mobile navigation, and PDF downloading. All 41 projects remain available; JavaScript shows nine initially and reveals more on request. Without JavaScript, the full project list remains visible.

## Deployment configuration

For a public deployment, configure `DJANGO_DEBUG=0`, a private `DJANGO_SECRET_KEY`, and `DJANGO_ALLOWED_HOSTS` (comma-separated domain names). Run `python manage.py collectstatic` and configure your hosting platform to serve `staticfiles/`. Use a production WSGI/ASGI server rather than Django's development server. This project has been built and verified locally; it has not been deployed publicly.

## Project documentation

- [Skills and capabilities](skills.md): professional expertise and implementation skills.
- [Requirements](requirement.md): website scope, behavior, dependencies, and acceptance criteria.
- [Business brief](business.md): audiences, positioning, visitor journeys, and success criteria.
- [Architecture](architecture.md): request flow, content storage, integrations, and file responsibilities.
- [Deployment and operations](deployment.md): local setup, production configuration, and Git publishing.

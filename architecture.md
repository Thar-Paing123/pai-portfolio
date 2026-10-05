# Application architecture

## Request flow

1. Django routes `/` to `portfolio.views.home`.
2. The view loads skills, projects, experience, and education from `portfolio/data.py`.
3. Django renders `portfolio/templates/portfolio/home.html` with that content.
4. CSS defines the visual presentation. JavaScript enhances navigation and project browsing in the visitor's browser.
5. `/resume/` returns the bundled PDF with `FileResponse` and an attachment filename.

## File map

| Location | Responsibility |
| --- | --- |
| `manage.py` | Django command entry point |
| `config/settings.py` | Application settings and environment configuration |
| `config/urls.py` | Home, résumé, and default Django admin routes |
| `config/wsgi.py`, `config/asgi.py` | Server entry points |
| `portfolio/data.py` | Résumé-derived portfolio content |
| `portfolio/views.py` | Home rendering and PDF download |
| `portfolio/templates/portfolio/home.html` | Page structure and content presentation |
| `portfolio/static/portfolio/style.css` | Responsive styling and CSS illustrations |
| `portfolio/static/portfolio/app.js` | Search, filters, progressive browsing, navigation, clipboard feedback |
| `portfolio/static/portfolio/assets/` | Photo, original résumé PDF, and favicon |
| `portfolio/tests.py` | Rendered content and download tests |

## Data and integrations

Portfolio data is versioned Python content. No custom database models or admin editing interface are implemented. SQLite is configured for Django's built-in applications.

GitHub and LinkedIn are external links rather than API integrations. Email contact opens the visitor's email application. Clipboard access has success and failure feedback. Google Fonts is an optional external asset dependency with system-font fallbacks.

## Progressive enhancement

The server renders all 41 projects. JavaScript limits the initial visible matching set to nine, combines category selection and text search, and exposes further matches through Show more. If JavaScript is unavailable, the full archive and native project details remain readable.

## Configuration

`DJANGO_DEBUG`, `DJANGO_SECRET_KEY`, and `DJANGO_ALLOWED_HOSTS` control environment-specific settings. A generated development key is used when no key is supplied; production must use a stable private key. Collected static assets are written to `staticfiles/`.

See [deployment](deployment.md) for operating instructions and [requirements](requirement.md) for expected behavior.

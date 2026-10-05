# Portfolio requirements

## Purpose and scope

Present Phyo Thet Paing's experience as an Odoo Technical Lead and AI Engineer to recruiters, hiring managers, potential clients, and engineering collaborators. Use the supplied résumé as the source of professional content.

## Functional requirements

| ID | Requirement | Acceptance criteria |
| --- | --- | --- |
| FR-01 | Introduce the owner | Show name, professional role, introductory text, photo, and Bangkok location. |
| FR-02 | Present every résumé project | Include all 41 projects, retaining the source roles, team sizes where supplied, and implementation scope. |
| FR-03 | Browse project categories | Support All projects, AI & automation, ERP solutions, and E-commerce. Indicate the selected filter. |
| FR-04 | Search projects | Search project text, including name, technology, modules, and details. Combine search with the selected category. |
| FR-05 | Manage long project lists | With JavaScript enabled, show up to nine matching projects initially and reveal nine more per request. Display visible and matching counts. |
| FR-06 | Handle empty results | Show an explanatory message and a control that resets both search and category. |
| FR-07 | Show project details | Allow visitors to expand each project's role and implementation description. |
| FR-08 | Present career information | Show work history, professional skills, education, and languages. |
| FR-09 | Download the résumé | `/resume/` returns the bundled original PDF as a downloadable attachment. |
| FR-10 | Provide contact options | Provide an email link, copy-email feedback, GitHub profile, and LinkedIn profile. External profile links open in a new tab. |
| FR-11 | Support mobile navigation | Provide a toggle with an expanded state; close it after selecting a section or pressing Escape. |

## Quality requirements

- Support desktop and mobile layouts without horizontal page overflow. Verification has covered widths of 320, 390, 768, 1024, and 1440 pixels.
- Use semantic HTML, accessible names, visible keyboard focus, live feedback for search results, and reduced-motion preferences.
- Keep all project content readable without JavaScript. Enhanced search and filters require JavaScript.
- Use system font fallbacks when Google Fonts cannot load.
- Keep the virtual environment, local SQLite database, generated static files, temporary artifacts, and environment files out of Git.
- Configure the secret key, allowed hosts, and debug mode for deployment through environment variables.

## Dependencies

Use Python 3.12 or newer and install the pinned Django dependency from [requirements.txt](requirements.txt). The UI uses HTML, CSS, and plain JavaScript with no frontend build step. SQLite supports the default Django application configuration; portfolio content is maintained in Python rather than database records.

## Validation

Run `python manage.py check` and `python manage.py test`. Browser verification should cover search, combined filters, reset behavior, progressive browsing, project details, profile links, mobile navigation, keyboard interaction, and PDF downloading. Automated Django tests currently cover rendered core content and PDF integrity; browser checks were performed separately during implementation.

## Outside current scope

A contact submission service, CMS, account registration, visitor analytics, live GitHub repository synchronization, and public website hosting are not implemented. GitHub publication makes the source available; it does not host the Django server.

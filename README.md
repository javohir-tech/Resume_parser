# ResumeParser

ResumeParser is a web app for creating, editing, and tailoring resumes. Start from scratch or import a PDF or DOCX file, customize the design, and download the finished resume as a PDF.

## Features

- Extract text from PDF and DOCX files and use AI to fill in resume sections.
- Edit personal details, work experience, education, skills, and languages.
- Choose from five templates (Classic, Modern, Minimal, Professional, and Sidebar) and customize fonts and colors.
- Generate a tailored copy of a resume and a cover letter from a job description.
- Sign in with a one-time Telegram code.
- Use the app in Uzbek, English, or Russian.

## Project layout

| Directory | Contents |
| --- | --- |
| [client/](client/README.md) | Nuxt 4, Vue 3, and TypeScript frontend with the resume editor, templates, and translations |
| [server/](server/README.md) | FastAPI backend with PostgreSQL, Alembic migrations, a Telegram bot, AI services, and PDF export |

## Run locally

1. Follow the [server guide](server/README.md) to configure PostgreSQL, set environment variables, apply migrations, and start the API.
2. Start the Telegram bot in a separate terminal to receive sign-in codes.
3. Follow the [client guide](client/README.md) to install the frontend dependencies and start Nuxt.
4. Open the [web app](http://localhost:3000). API documentation is available in [Swagger UI](http://localhost:8000/docs).

## Import limits

By default, uploads are limited to 10 MB and PDFs to 10 pages. Files must contain extractable text. Image-only scans require OCR before upload.

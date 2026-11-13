# ResumeParser Server

The backend exposes the FastAPI API for authentication, user accounts, and resumes. It stores data in PostgreSQL, runs database migrations with Alembic, parses uploaded documents, and renders PDF downloads with Playwright. An aiogram bot runs as a separate process and issues sign-in codes.

## Install dependencies

Use Python 3.14 and a running PostgreSQL instance. Create an empty database named `resume_parser` and use a database account that can create tables in it.

Run these Windows PowerShell commands from `server/`.

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requierments.txt fastapi-filter==3.0.0
.\.venv\Scripts\python.exe -m playwright install chromium
```

The dependency file is named `requierments.txt`. The API also imports `fastapi-filter`, which is installed explicitly because it is missing from that file. Chromium is used for PDF export.

## Configure the environment

Create `server/.env` and replace the example values with your own database credentials, bot token, signing secret, and AI settings.

```dotenv
DATABASE_URL=postgresql+asyncpg://postgres:YOUR_DB_PASSWORD@localhost:5432/resume_parser
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
JWT_SECRET=YOUR_RANDOM_SIGNING_SECRET
JWT_ALGORITHM=HS256
DEBUG=true

AI_PROVIDER=openai
AI_BASE_URL=https://api.openai.com/v1
AI_MODEL=YOUR_MODEL_NAME
AI_API_KEY=YOUR_AI_API_KEY
```

Set `AI_PROVIDER` to `openai`, `deepseek`, or `gemini`. Use the matching OpenAI-compatible base URL, API key, and a model that supports JSON object responses. Resume import and job matching send input text to the configured provider.

## Start the API

Run migrations and start the development server from `server/`.

```powershell
.\.venv\Scripts\python.exe -m alembic upgrade head
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host localhost --port 8000
```

Open [Swagger UI](http://localhost:8000/docs) to explore the API. The default CORS configuration allows the Nuxt app at `http://localhost:3000`.

## Start the Telegram bot

Run the bot from `server/` in a separate terminal.

```powershell
.\.venv\Scripts\python.exe run_polling.py
```

Send `/start` to the bot configured by `BOT_TOKEN` and share your contact when prompted. Send `/login` to get a six-digit code and enter it on the [local sign-in page](http://localhost:3000/login). To use the bot's **Login** button, set `FRONTEND_URL` in [app/bot/handlers.py](app/bot/handlers.py) to the sign-in page URL that users can open.

## API overview

| Endpoint | Purpose |
| --- | --- |
| `POST /api/auth/telegram/verify` | Verify a Telegram sign-in code |
| `GET /api/users/me` | Read the signed-in user's profile |
| `GET /api/resume/my/resumes` | List the signed-in user's resumes |
| `POST /api/resume/parse` | Extract and parse a PDF or DOCX upload |
| `POST /api/resume/import` | Save a parsed resume |
| `POST /api/resume/job-match` | Tailor a resume and generate a cover letter |
| `POST /api/resume/{resume_id}/download` | Render and download a resume as a PDF |

The default upload limit is 10 MB, with up to 10 PDF pages and 40,000 characters of extracted text. Limits and timeouts are defined in [app/core/config.py](app/core/config.py).

## Source layout

| Directory | Contents |
| --- | --- |
| `app/api/` | Authentication, user, and resume routes |
| `app/bot/` | Telegram bot handlers |
| `app/core/` | Settings, authentication helpers, and exception handling |
| `app/db/` and `app/models/` | Database sessions and SQLAlchemy models |
| `app/schemas/` | Request and response models |
| `app/services/` | Document reading, AI processing, and PDF rendering |
| `alembic/` | PostgreSQL migrations |

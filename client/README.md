# ResumeParser Client

The frontend uses Nuxt 4, Vue 3, TypeScript, Nuxt UI, Tailwind CSS, and Pinia. It provides the resume editor, template previews, job matching form, account settings, and translated pages.

## Local development

Use Node.js 24.12 or later in the 24.x series and npm. Start the [FastAPI server and Telegram bot](../server/README.md) to use the authenticated features.

Run these commands from this directory.

```powershell
npm ci
npm run dev -- --host localhost --port 3000
```

Open the [local app](http://localhost:3000). The API client points to `http://localhost:8000` in [app/shared/api/client.ts](app/shared/api/client.ts). Keep the frontend origin at `http://localhost:3000` for the backend's default CORS configuration.

## Contact form configuration

To forward contact form messages to Telegram, create `client/.env` with these server-side Nuxt settings.

```dotenv
NUXT_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
NUXT_CHAT_ID=YOUR_TELEGRAM_CHAT_ID
```

The Nuxt server uses these values for the contact form. The Telegram sign-in bot uses the backend's `BOT_TOKEN` setting.

## Pages

| Path | Purpose |
| --- | --- |
| `/login` | Enter a one-time Telegram code |
| `/resume` | List, create, and import resumes |
| `/resume/<id>` | Edit a resume and customize its design |
| `/resume/<id>/view` | Preview and download a resume |
| `/job-match` | Tailor a resume to a job description |
| `/settings` | Manage account, appearance, and devices |

Uzbek is the default locale. English and Russian routes use the `/en` and `/ru` prefixes. Translation files are in [i18n/locales/](i18n/locales/).

## Source layout

| Directory | Contents |
| --- | --- |
| `app/pages/` | Routes and page views |
| `app/features/` | Resume editing, import, authentication, and other user actions |
| `app/entities/` | Domain models, stores, and resume templates |
| `app/widgets/` | Page sections and editor panels |
| `app/shared/` | Shared utilities and the API client |
| `server/api/` | Nuxt server endpoints, including the contact form |

## Production build

Build the app and preview the result locally from `client/`.

```powershell
npm run build
npm run preview
```

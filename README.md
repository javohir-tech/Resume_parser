# ResumeParser

ResumeParser — rezyume yaratish, tahrirlash va uni ish e’loniga moslashtirish uchun veb ilova. Rezyumeni PDF yoki DOCX faylidan import qilish, qo‘lda yaratish va tayyor nusxasini PDF formatida yuklab olish mumkin.

## Imkoniyatlar

- PDF va DOCX hujjatlaridan matn ajratish va AI yordamida rezyume bo‘limlarini to‘ldirish.
- Ish tajribasi, ta’lim, ko‘nikmalar va tillarni tahrirlash.
- Classic, Modern, Minimal, Professional va Sidebar shablonlaridan foydalanish, shrift va ranglarni o‘zgartirish.
- Ish e’loni matni asosida rezyumening moslashtirilgan nusxasi va motivatsion xat yaratish.
- Rezyumeni ko‘rib chiqish va PDF formatida yuklab olish.
- Telegram orqali bir martalik kod bilan kirish.
- O‘zbek, ingliz va rus tillaridagi interfeys.

## Texnologiyalar

| Qism | Texnologiyalar |
| --- | --- |
| Frontend | Nuxt 4, Vue 3, TypeScript, Nuxt UI, Tailwind CSS, Pinia |
| Backend | FastAPI, Pydantic, SQLAlchemy, asyncpg |
| Ma’lumotlar bazasi | PostgreSQL, Alembic migratsiyalari |
| Telegram bot | aiogram |
| Hujjatlar | pypdf, python-docx, Playwright va Chromium |
| AI | OpenAI SDK orqali mos API, provayder sifatida OpenAI, DeepSeek yoki Gemini |

## Mahalliy ishga tushirish

Quyidagi buyruqlar Windows PowerShell uchun. Python 3.14, Node.js 24.12 yoki yangiroq 24.x versiyasi, npm va PostgreSQL kerak. PostgreSQL’da `resume_parser` nomli baza yarating va foydalanuvchiga shu bazada jadval yaratish huquqini bering.

### 1. Backend

Loyiha ildizidan quyidagi buyruqlarni bajaring.

```powershell
cd server
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requierments.txt fastapi-filter==3.0.0
.\.venv\Scripts\python.exe -m playwright install chromium
```

`server/.env` faylini quyidagi namuna asosida yarating. Baza foydalanuvchisi, paroli, bot tokeni, JWT kaliti va AI sozlamalarini o‘zingizning qiymatlaringiz bilan almashtiring.

```dotenv
DATABASE_URL=postgresql+asyncpg://postgres:YOUR_DB_PASSWORD@localhost:5432/resume_parser
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
JWT_SECRET=YOUR_RANDOM_SECRET
JWT_ALGORITHM=HS256
DEBUG=true

AI_PROVIDER=openai
AI_BASE_URL=https://api.openai.com/v1
AI_MODEL=YOUR_MODEL_NAME
AI_API_KEY=YOUR_AI_API_KEY
```

`AI_PROVIDER` uchun `openai`, `deepseek` yoki `gemini` qiymatini tanlang. API manzili, kaliti va model nomi tanlangan provayderga tegishli bo‘lishi kerak. Model JSON obyekt qaytarish rejimini qo‘llashi kerak.

`server/` papkasida migratsiyalarni qo‘llang va API’ni ishga tushiring.

```powershell
.\.venv\Scripts\python.exe -m alembic upgrade head
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host localhost --port 8000
```

API hujjatlari [Swagger UI](http://localhost:8000/docs) orqali ochiladi.

### 2. Telegram bot

Yangi terminalda loyiha ildizidan botni alohida ishga tushiring.

```powershell
cd server
.\.venv\Scripts\python.exe run_polling.py
```

`BOT_TOKEN` bilan bog‘langan botga `/start` yuboring. Birinchi kirishda kontaktingizni ulashing. Keyin `/login` orqali olti xonali kod oling va uni [kirish sahifasiga](http://localhost:3000/login) kiriting. Mahalliy muhitda kodni qo‘lda kiritish mumkin.

### 3. Frontend

Yana bir terminalda loyiha ildizidan Nuxt ilovasini ishga tushiring.

```powershell
cd client
npm ci
npm run dev -- --host localhost --port 3000
```

Ilovani [localhost:3000](http://localhost:3000) manzilida oching. Kontakt formasidan Telegram orqali xabar yuborish funksiyasi uchun `client/.env` fayliga `NUXT_BOT_TOKEN` va `NUXT_CHAT_ID` qiymatlarini qo‘shing.

## Loyiha tuzilmasi

```text
ResumeParser/
├── client/
│   ├── app/              # Sahifalar, rezyume muharriri va shablonlar
│   ├── i18n/locales/     # O‘zbek, ingliz va rus tillaridagi tarjimalar
│   └── server/api/       # Kontakt formasidan Telegram’ga xabar yuborish
└── server/
    ├── app/api/          # Kirish, profil va rezyume endpointlari
    ├── app/bot/          # Telegram bot buyruqlari
    ├── app/models/       # Ma’lumotlar bazasi modellari
    ├── app/services/     # Import, AI tahlili va PDF eksporti
    ├── alembic/          # PostgreSQL migratsiyalari
    └── run_polling.py    # Botni ishga tushirish
```

## Import cheklovlari

Standart sozlamada PDF va DOCX fayllarining hajmi 10 MB gacha, PDF esa 10 sahifagacha bo‘lishi mumkin. Faylda ajratib olinadigan matn bo‘lishi kerak. Faqat skanerlangan rasmlardan iborat PDF uchun OCR qo‘llanmaydi.

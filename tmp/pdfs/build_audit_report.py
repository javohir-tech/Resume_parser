from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    KeepTogether,
)


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'output' / 'pdf' / 'ResumeParser_tahlil_va_roadmap.pdf'
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(TTFont('Audit', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('AuditBold', 'C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFont(TTFont('AuditItalic', 'C:/Windows/Fonts/ariali.ttf'))
pdfmetrics.registerFont(TTFont('AuditMono', 'C:/Windows/Fonts/consola.ttf'))
pdfmetrics.registerFontFamily('Audit', normal='Audit', bold='AuditBold', italic='AuditItalic', boldItalic='AuditBold')

NAVY = colors.HexColor('#15323B')
GREEN = colors.HexColor('#008565')
INK = colors.HexColor('#243F47')
MUTED = colors.HexColor('#60777E')
LINE = colors.HexColor('#DCE6E7')
PALE = colors.HexColor('#EEF6F2')
LIGHT = colors.HexColor('#F4F7F8')
AMBER = colors.HexColor('#95620C')
PAGE_W, PAGE_H = A4
WIDTH = PAGE_W - 96

styles = {
    'body': ParagraphStyle('Body', fontName='Audit', fontSize=10.1, leading=14.5, textColor=INK, spaceAfter=8),
    'small': ParagraphStyle('Small', fontName='Audit', fontSize=8.7, leading=12.2, textColor=MUTED, spaceAfter=7),
    'note': ParagraphStyle('Note', fontName='Audit', fontSize=9.3, leading=13.4, textColor=INK, spaceAfter=0),
    'title': ParagraphStyle('Title', fontName='AuditBold', fontSize=25, leading=29, textColor=NAVY, spaceAfter=10),
    'cover': ParagraphStyle('Cover', fontName='AuditBold', fontSize=34, leading=39, textColor=NAVY, spaceAfter=8),
    'subtitle': ParagraphStyle('Subtitle', fontName='Audit', fontSize=17, leading=23, textColor=MUTED, spaceAfter=18),
    'h2': ParagraphStyle('H2', fontName='AuditBold', fontSize=12.2, leading=16, textColor=NAVY, spaceBefore=9, spaceAfter=5, keepWithNext=True),
    'h3': ParagraphStyle('H3', fontName='AuditBold', fontSize=10.6, leading=14.2, textColor=GREEN, spaceBefore=8, spaceAfter=4, keepWithNext=True),
    'kicker': ParagraphStyle('Kicker', fontName='AuditBold', fontSize=8.4, leading=12, textColor=GREEN, spaceAfter=9),
    'source': ParagraphStyle('Source', fontName='AuditMono', fontSize=7.25, leading=9.7, textColor=MUTED, spaceAfter=9, splitLongWords=True),
    'cell': ParagraphStyle('Cell', fontName='Audit', fontSize=9.05, leading=12.5, textColor=INK),
    'head': ParagraphStyle('Head', fontName='AuditBold', fontSize=8.7, leading=12, textColor=colors.white),
    'metric': ParagraphStyle('Metric', fontName='AuditBold', fontSize=25, leading=30, textColor=GREEN, alignment=TA_CENTER),
    'metric_label': ParagraphStyle('MetricLabel', fontName='Audit', fontSize=8.5, leading=12, textColor=INK, alignment=TA_CENTER),
    'bullet': ParagraphStyle('Bullet', fontName='Audit', fontSize=9.8, leading=14, textColor=INK, leftIndent=11, firstLineIndent=-9, spaceAfter=4),
}

story = []

def p(text, kind='body'):
    return Paragraph(text, styles[kind])

def add(text, kind='body'):
    story.append(p(text, kind))

def gap(height=6):
    story.append(Spacer(1, height))

def bullets(items):
    for item in items:
        story.append(p('- ' + item, 'bullet'))

def source(*paths):
    add('<br/>'.join(escape(path) for path in paths), 'source')

def callout(title, text, bg=PALE):
    content = [p(title, 'h3'), p(text, 'note')]
    table = Table([[content]], colWidths=[WIDTH])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('BOX', (0, 0), (-1, -1), .5, LINE),
        ('LINEBEFORE', (0, 0), (0, -1), 3, GREEN),
        ('LEFTPADDING', (0, 0), (-1, -1), 13),
        ('RIGHTPADDING', (0, 0), (-1, -1), 13),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.extend([table, Spacer(1, 9)])

def table(headers, rows, widths):
    cells = [[p(str(value), 'head') for value in headers]]
    cells += [[p(str(value), 'cell') for value in row] for row in rows]
    result = Table(cells, colWidths=[WIDTH * w for w in widths], repeatRows=1, hAlign='LEFT')
    result.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT]),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 9),
        ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LINEBELOW', (0, 0), (-1, 0), .7, NAVY),
        ('LINEBELOW', (0, 1), (-1, -1), .35, LINE),
    ]))
    story.extend([result, Spacer(1, 10)])

def page(section, title, intro=None):
    if story:
        story.append(PageBreak())
    add(section.upper(), 'kicker')
    add(title, 'title')
    if intro:
        add(intro)

def finding(number, title, observation, action, refs):
    block = [p(f'{number:02d}. {title}', 'h2'), p(observation), p('<b>Tavsiya:</b> ' + action), p('<br/>'.join(escape(r) for r in refs), 'source')]
    story.append(KeepTogether(block))

def stage(number, title, duration, tasks, criteria):
    add(f'{number:02d} / {title}', 'h2')
    add('Taxminiy hajm: ' + duration + ' ish kuni.', 'small')
    bullets(tasks)
    add('Tugallanish mezonlari', 'h3')
    bullets(criteria)
    gap(9)


# 1. Executive assessment
add('TEXNIK AUDIT + AMALIY ROADMAP  |  12 NOYABR 2026', 'kicker')
add('ResumeParser', 'cover')
add('Arxitektura, kod sifati<br/>va keyingi qadamlar', 'subtitle')
add('Loyihada asosiy foydalanuvchi jarayonlari shakllangan. Keyingi ishlar to‘lov va CRM bilan birga ma’lumotlar xavfsizligi, saqlash ishonchliligi va production tayyorgarligini qamrab oladi.')
metrics = []
for value, label in [('80-85%', 'Asosiy foydalanuvchi<br/>funksiyalari qamrovi'), ('55-65%', 'To‘lov + CRM bilan<br/>umumiy tayyorlik'), ('6/10', 'Arxitektura va<br/>kod tozaligi bahosi')]:
    metrics.append([p(value, 'metric'), p(label, 'metric_label')])
metric_table = Table([metrics], colWidths=[WIDTH / 3] * 3)
metric_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), PALE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING', (0, 0), (-1, -1), 12), ('BOTTOMPADDING', (0, 0), (-1, -1), 13),
    ('LINEAFTER', (0, 0), (1, 0), .7, colors.white),
]))
story.extend([metric_table, Spacer(1, 15)])
table(['Yo‘nalish', 'Baho', 'Asosiy sabab'], [
    ['Frontend arxitekturasi', '7/10', 'Qatlamlar va funksiyalar ajratilgan'],
    ['Backend arxitekturasi', '6/10', 'Routerlarda biznes mantiq ko‘p'],
    ['Ma’lumotlar modeli', '6/10', 'Ayrim bog‘lanishlarda jiddiy xato bor'],
    ['Kod tozaligi', '6/10', 'Takrorlanish va nomlash izchilligi muammolari'],
    ['Testlar va avtomatik tekshiruv', '4/10', 'Testlar qisman eskirgan, qamrov tor'],
    ['Production tayyorgarligi', '4/10', 'Ruxsatlar, konfiguratsiya va limitlar tugallanmagan'],
], [.39, .13, .48])
add('Bahoning chegarasi', 'h2')
add('CRM ichki admin panel sifatida talqin qilindi: foydalanuvchilar, tariflar, to‘lovlar, AI sarfi va murojaatlar. Tasdiqlangan texnik topshiriq bo‘lmagani uchun foizlar qolgan ish hajmi bo‘yicha taxminiy muhandislik bahosi; ular test coverage yoki production kafolati emas.', 'small')
add('Hisobot tarkibi: 2-6-betlarda audit va dalillar; 7-10-betlarda bosqichlar, taxminiy muddatlar, vazifalar va qabul mezonlari.', 'small')

# 2. Architecture and quality
page('01 / Arxitektura', 'Mavjud asosni rivojlantirish', 'Frontend FSD yondashuviga yaqin, backend esa qatlamli monolit shaklida qurilgan. Mavjud tuzilmani modullar va umumiy qoidalar bilan mustahkamlash tavsiya etiladi.')
add('Amalda yozilgan funksiyalar', 'h2')
add('Telegram orqali kirish, profil va qurilmalar; rezyume yaratish, tahrirlash, o‘chirish, qidirish va sahifalash; PDF/DOCX import; vakansiyaga moslashtirish, AI nusxa va cover letter; beshta shablon, rang/shrift va PDF yuklash; o‘zbek, rus va ingliz tillari.')
add('Frontend: 7/10', 'h2')
add('<b>pages → widgets → features → entities → shared</b> ajratilishi tushunarli. Funksiyalarda API, model va UI bo‘laklari bor. Rezyume shablonlarining umumiy kontrakti yangi shablon qo‘shishni yengillashtiradi. Lekin ayrim importlar qatlam chegarasini buzadi: entities/user komponenti features/user qatlamiga bog‘langan.')
source('client/app/entities/user/ui/user_session_card.vue:3', 'client/app/entities/resume/models/template-contract.ts:3')
add('Backend: 6/10', 'h2')
add('AI mijoz, hujjat o‘qish va PDF yaratish alohida xizmatlarda. Rezyume routeri esa 1174 qator bo‘lib, SQL so‘rovlari, egalik nazorati, AI jarayoni, nusxa yaratish va tranzaksiyalarni bir joyda bajaradi. Umumiy egalik tekshiruvi va biznes operatsiyalarini servisga chiqarish xatolarni kamaytiradi.')
source('server/app/api/resume.py:133')
callout('Tavsiya etiladigan yo‘nalish', 'Router so‘rov va javobni boshqaradi; service biznes qoidasi va tranzaksiyani bajaradi; AI, PDF va to‘lov provayderlari alohida adapterlarda ishlaydi. Auth, resumes, billing va admin modullari bir backend ichida aniq chegaralarga ega bo‘ladi.')
add('Yaxshi ishlangan qismlar', 'h2')
bullets([
    'PDF/DOCX formatlari, fayl hajmi, PDF sahifalari va ochilgan DOCX hajmi tekshiriladi.',
    'AI javobi JSON sxemasi bilan tekshiriladi; timeout va provayder xatolari boshqariladi.',
    'PDF yaratishda JavaScript va tashqi tarmoq so‘rovlari bloklangan.',
    'Autosave navbati, beshta shablon va uch tildagi interfeys uchun asos mavjud.',
])
add('Kod tozaligi: 6/10', 'h2')
add('Autosave mantiqi uch joyda takrorlangan. orginal, desing, AvtoSave va Requset kabi nomlar izchil emas. Job-match rollback va Telegram kodini yangilash execute chaqiriqlarida await yetishmaydi. Git ichida 46 ta __pycache__ fayli bor. Formatter, lint, umumiy nomlash qoidasi va kichik refaktor kerak.')
source('server/app/api/resume.py:290; server/app/bot/handlers.py:186')
add('Manba yo‘llari C:/Users/ASUS/Desktop/ResumeParser loyiha ildiziga nisbatan berilgan. Kod auditi ushbu chatda ko‘rilgan ishchi nusxaga asoslangan.', 'small')

# 3. Critical findings
page('02 / Kritik topilmalar', 'Avval tuzatiladigan 4 holat', 'Bu muammolar foydalanuvchi ma’lumoti, saqlash va hisobga kirish ishonchliligiga ta’sir qiladi. To‘lov va CRM ustidagi ishlar shu asos mustahkamlangach davom ettiriladi.')
finding(1, 'Rezyume dizaynida egalik tekshiruvi yo‘q',
    'design_edit foydalanuvchini autentifikatsiyadan o‘tkazadi, lekin rezyume shu foydalanuvchiga tegishli ekanini tekshirmaydi. So‘rov faqat rezyume ID’si bo‘yicha bajariladi. Login qilgan boshqa foydalanuvchi ma’lum ID bilan dizaynni o‘zgartira oladi.',
    'Barcha o‘zgartirish operatsiyalari uchun yagona egalik tekshiruvini qo‘llash va boshqa foydalanuvchi bilan kirish testini qo‘shish.',
    ['server/app/api/resume.py:601'])
finding(2, 'Bir nechta rezyumeli profil o‘chmaydi',
    'User.resumes ro‘yxat o‘rniga Mapped["Resume"] sifatida belgilangan. Xotiradagi sun’iy bazada ikki rezyumeli foydalanuvchini o‘chirish foreign-key xatosiga olib keldi.',
    'Bog‘lanishni Mapped[list["Resume"]] ko‘rinishiga keltirish. Profil, asl rezyume, AI nusxalari va ichki bo‘limlar o‘chirilishini bitta to‘liq jarayon sifatida tekshirish.',
    ['server/app/models/user.py:57; server/app/api/users.py:69'])
finding(3, 'Forma tez yopilsa tahrir saqlanmaydi',
    'Ta’lim va tajriba formalarining autosave timeri komponent yo‘qolganda bekor qilinadi. Qayta ochilganda mahalliy tahrir saqlangan holat deb olinadi. Tekshiruvda serverga 0 ta so‘rov ketgan bo‘lsa ham keyingi flush() muvaffaqiyat qaytardi.',
    'Yopilishdan oldin saqlashni tugatish yoki autosave holatini formadan uzoqroq yashaydigan qatlamga ko‘chirish. Sekin tarmoq va tez almashish holatlarini tekshirish.',
    ['client/app/features/resume/edit-resume/models/useEducationAvtoSave.ts:168'])
finding(4, 'Sessiya va token jarayoni to‘liq emas',
    'Sessiya o‘chirilganda refresh-token bekor qilinadi, ammo access-token qolgan muddati davomida, maksimal bir kungacha ishlashi mumkin. verify() sessiya holatini tekshirmaydi. Frontend /refresh o‘rniga 401 javobida login sahifasiga yuboradi.',
    'Sessiya holatini tekshirish, token yangilashni API mijoziga ulash va parallel 401 javoblari uchun yagona refresh jarayonini tashkil qilish.',
    ['server/app/core/security.py:52; client/app/shared/api/client.ts:11'])

# 4. Remaining correctness findings
page('03 / Ishonchlilik', 'Ma’lumot va interfeys izchilligi', 'Quyidagi holatlar kundalik foydalanishda noto‘g‘ri natija, ko‘rinmaydigan ma’lumot yoki tushunarsiz xato holatini keltirib chiqarishi mumkin.')
finding(5, 'AI keshi eskirgan natijani qaytaradi',
    'Hash hisoblashga ism, kontaktlar, ta’lim, tillar va ayrim tajriba maydonlari kiritilmagan. Bu ma’lumotlar o‘zgarsa ham oldingi AI nusxa qaytishi mumkin. Sun’iy ma’lumotlar bilan hash o‘zgarmasligi tasdiqlandi.',
    'AI’ga yuborilayotgan to‘liq ma’lumot, asl rezyume ID’si, prompt versiyasi va modelni hashga kiritish. Parallel bir xil so‘rovlar takror nusxa yaratmasligini tekshirish.',
    ['server/app/services/resume_input_hash.py:8; server/app/api/resume.py:212'])
finding(6, 'Pagination: server 9, interfeys 10 hisoblaydi',
    'Backend bir sahifaga 9 ta rezyume qaytaradi, UPagination esa standart 10 tadan hisoblaydi. 20 ta rezyumeda uchinchi sahifa kerak bo‘lsa ham UI ikki sahifa ko‘rsatadi. Qidiruv yoki filtr o‘zgarganda sahifa 1 ga qaytarilmagan.',
    'Page size qiymatini ikki tomonda tenglashtirish; filtrda sahifani qayta boshlash; o‘chirishdan keyin count, ro‘yxat va sahifani yangilash.',
    ['server/app/api/resume.py:482; client/app/pages/job-match.vue:143'])
finding(7, 'Server validatsiyasi yetarli emas',
    'ResumeJobMatch sxemasi bo‘sh vakansiya, 100 ming belgili matn va noto‘g‘ri UUID’ni qabul qildi. Dizayn sxemasi ham mavjud bo‘lmagan shablon nomini qabul qiladi. Frontenddagi cheklovni to‘g‘ridan-to‘g‘ri API chaqirig‘i chetlab o‘tishi mumkin.',
    'UUID turlari, min/max uzunliklar, shablon/font uchun ruxsat etilgan qiymatlar va import sxemalarida bazaga mos chegaralarni joriy qilish.',
    ['server/app/schemas/resume_schemas.py:6; server/app/schemas/resume_schemas.py:166'])
finding(8, 'Dizaynni saqlash xatosi ko‘rsatilmaydi',
    'Dizayn autosave catch qismida xato holati va xabar o‘rnatilmagan. Navigatsiya to‘xtashi mumkin, lekin foydalanuvchi sababini tushunmaydi. Mavjud testlardan biri aynan shu holatda yiqildi.',
    'Saqlanmoqda, saqlandi va saqlanmadi holatlarini ko‘rsatish; xatoda tahrirni saqlab qolish va qayta urinish imkonini berish.',
    ['client/app/features/resume/design-edit/models/useEditDesign.ts:98'])

# 5. Product scope and launch gaps
page('04 / Qolgan mahsulot ishlari', 'To‘lov tizimi, CRM va deploy')
add('To‘lov tizimi: taxminan 5-10%', 'h2')
add('free/pro maydoni va narxlar interfeysi mavjud. Billing sahifasi hozircha sarlavhadan iborat. To‘lovga tayyorlash provayder tugmasini ulashdan tashqari quyidagi server qoidalarini talab qiladi:')
bullets([
    'To‘lov yaratish, webhook/callbackni tasdiqlash va takror callbackni xavfsiz qayta ishlash.',
    'Obuna muddati, holati, to‘lovlar tarixi va bekor qilish jarayoni.',
    'PDF va premium imkoniyatlarga server darajasida ruxsat.',
    'AI foydalanish hisoblagichi, tarif limitlari va parallel so‘rovlarda to‘g‘ri hisob.',
])
add('Narxlar matnidagi oyiga 5 ta AI va 1 ta moslashtirish limitlari backendda amalga oshirilmagan.', 'small')
source('client/app/pages/settings/billing.vue:1; server/app/models/user.py:17')
add('CRM: funksional qismi boshlanmagan', 'h2')
add('admin papkasi bo‘sh. Minimal CRM tarkibi: foydalanuvchilarni qidirish va boshqarish, to‘lov/obunalar, AI sarfi, murojaatlar, administrator rollari va amallar jurnali. Interfeys bilan birga himoyalangan backend endpointlari ham yaratiladi. To‘liq savdo pipeline’i yoki tashkilotlar boshqaruvi ushbu bahoga kiritilmagan.')
add('Production uchun qolgan sozlamalar', 'h2')
bullets([
    'localhost API manzili va CORS qiymatlarini muhit konfiguratsiyasiga chiqarish.',
    'Doimiy SQL echo loglarini cheklash; foydalanuvchi ma’lumotlari va tokenlarni logga chiqarmaslik.',
    'requirements ro‘yxatiga ishlatilayotgan fastapi_filter paketini kiritish.',
    'Ishga tushirish qo‘llanmasi, CI, lint/typecheck va qayta tiklash tartibini tayyorlash.',
])
source('client/app/shared/api/client.ts:2; server/app/main.py:18', 'server/app/db/session.py:4; server/requierments.txt')
callout('Landing matnlari va haqiqiy imkoniyatlar', 'Sayt hh.uz/LinkedIn linkidan import va 6 ta shablonni va’da qiladi. Kodda PDF/DOCX import va 5 ta shablon bor. Link import scope’ga kirsa alohida vazifa sifatida baholanadi; aks holda marketing matnlari amaldagi imkoniyatlarga moslashtiriladi.')
source('client/i18n/locales/en.json:184; client/app/entities/resume/models/types.ts:82')

# 6. Evidence and readiness
page('05 / Tekshiruvlar', 'Bahoni qo‘llab-quvvatlovchi dalillar', 'Auditda sahifalar, API’lar, modellar, migratsiyalar, AI/PDF xizmatlari va mavjud testlar ko‘rib chiqildi. Quyidagi natijalar avvalgi kod tahlili davomida olingan.')
table(['Tekshiruv', 'Natija'], [
    ['Production build', '<b>O‘tdi.</b> Ayrim warninglar mavjud.'],
    ['Frontend testlari', '<b>27 tadan 13 tasi o‘tdi, 14 tasi yiqildi.</b>'],
    ['13 ta yiqilgan test sababi', 'Mocklarda eski API funksiya nomlari qolgan. Ular faqat xotirada moslashtirilganda 13/13 o‘tdi; repo testlari o‘zgartirilmadi.'],
    ['Qolgan 1 ta frontend test', 'Dizayn saqlash xatosining foydalanuvchiga ko‘rsatilmasligi bilan bog‘liq.'],
    ['Backend PDF testlari', '<b>2/2 o‘tdi.</b>'],
    ['Python sintaksisi', '<b>46 fayl</b> tekshiruvdan o‘tdi.'],
    ['UZ/RU/EN tarjimalari', 'Kalitlar mos. Statik chaqiriqlarda yetishmayotgan kalit topilmadi.'],
], [.35, .65])
add('Alohida tasdiqlangan holatlar', 'h2')
bullets([
    'Ikki rezyumeli foydalanuvchini sun’iy bazada o‘chirish foreign-key xatosiga olib keldi.',
    'Ism, email, ta’lim va til o‘zgartirilganda AI hash bir xil qoldi.',
    'Vakansiya sxemasi 0 va 100 000 belgili matnni hamda noto‘g‘ri UUID’ni qabul qildi.',
    'Ta’lim va tajriba autosave tekshiruvida yopish/ochishdan keyin 0 ta saqlash so‘rovi qayd etildi.',
])
callout('Tayyorlikni qanday talqin qilish kerak', '80-85% - asosiy foydalanuvchi funksiyalarining kodda mavjudligi bo‘yicha taxmin. 55-65% - to‘lov, minimal CRM va production ishlari qo‘shilgan umumiy baho. Bu ko‘rsatkichlar har bir funksiya real muhitda to‘liq sinovdan o‘tganini anglatmaydi.')
add('Sinov chegaralari', 'h2')
add('Haqiqiy AI provayderi va production PostgreSQL bilan to‘liq end-to-end sinov o‘tkazilmagan. Test coverage foizi o‘lchanmagan. Audit davomida ilovaning manba kodi o‘zgartirilmagan. Quyidagi roadmap shu topilmalarni yakunlangan va tekshiriladigan ishlarga aylantiradi.', 'small')

# 7. Roadmap overview
page('06 / Roadmap', 'Ketma-ketlik va taxminiy muddat', 'Baho: loyiha bilan tanish bitta full-stack dasturchi to‘liq ish vaqtida ishlaydi. Minimal CRM va dastlab bitta asosiy to‘lov provayderi nazarda tutilgan.')
table(['Bosqich', 'Natija', 'Ish kuni', 'Bog‘liqlik'], [
    ['00 / Kritik tuzatishlar', 'Egalik, o‘chirish, saqlash va sessiyalar ishonchli', '4-6', 'Darhol'],
    ['01 / Texnik asos', 'Servislar, kontraktlar, validatsiya va CI', '2-3', '00'],
    ['02 / To‘lov va tariflar', 'To‘lovdan server ruxsatigacha to‘liq jarayon', '7-10', '00, 01'],
    ['03 / CRM', 'Rollarga asoslangan operatsion boshqaruv', '5-7', '01; billing qismi uchun 02'],
    ['04 / Integratsion QA', 'Muhim jarayonlar staging’da tekshirilgan', '4-6', '02, 03'],
    ['05 / Ishga tushirish', 'Monitoring, zaxira va qaytish rejasi bilan release', '2-3', '04'],
], [.25, .43, .12, .20])
callout('Rejalashtirish oralig‘i', 'Jami 24-35 ish kuni. Taxminan 20% zaxira bilan 29-42 ish kuni, ya’ni 5 kunlik ish haftasida 6-9 hafta. Bu bajarish kafolati emas; provayder tasdig‘i, hisob ochish va tashqi kutish vaqti kiritilmagan. Ikkinchi to‘lov provayderi va kengroq CRM alohida baholanadi.')
add('Dastlabki 10 ish kuniga taklif', 'h2')
table(['Kun', 'Asosiy e’tibor', 'Ko‘rinadigan natija'], [
    ['1-2', 'Egalik tekshiruvi va profil o‘chirish', 'Ikki foydalanuvchi va ko‘p rezyumeli o‘chirish testlari'],
    ['3-4', 'Autosave, xato holatlari va navigatsiya', 'Tez yopish, sekin tarmoq va retry’da tahrir saqlanadi'],
    ['5-6', 'Sessiya, refresh va server validatsiyasi', 'Bekor qilingan sessiya va yaroqsiz so‘rovlar rad etiladi'],
    ['7-8', 'Pagination, AI hash, dependency va CI', 'Ro‘yxat to‘liq; testlar/build avtomatik ishlaydi'],
    ['9-10', 'Billing modeli va provider sandbox boshlanishi', 'Tarif qoidalari va to‘lov holatlari tasdiqlangan'],
], [.12, .41, .47])
add('Jadval ish tartibini ko‘rsatadi. Bosqichning qabul mezoni bajarilmasa, keyingi bosqichga o‘tish sanasi shunga mos suriladi.', 'small')

# 8. Roadmap phases 0 and 1
page('07 / Roadmap tafsiloti', '00-01. Barqaror asos')
stage(0, 'Kritik xatolarni yopish', '4-6', [
    'Resume va uning ichki obyektlari uchun yagona ownership tekshiruvi; barcha write endpointlarini ko‘rib chiqish.',
    'User.resumes bog‘lanishini va profil/asl rezyume/AI nusxalari o‘chirish zanjirini tuzatish.',
    'Ta’lim va tajriba formasini yopishda pending autosave’ni yo‘qotmaslik; dizayn xatosini aniq ko‘rsatish.',
    'Access-tokenni sessiyaga bog‘lash, revoke nazorati va frontend refresh mexanizmini tugatish.',
    'Job-match UUID va matn chegaralarini serverda tekshirish; yetishmayotgan await chaqiriqlarini to‘g‘rilash.',
], [
    'A foydalanuvchi B foydalanuvchining hech bir rezyume qismini o‘zgartira olmaydi; bazadagi qiymat o‘zgarmaydi.',
    'Bir nechta asl rezyume va AI nusxalari bor profil to‘liq o‘chadi; yetim yozuv qolmaydi.',
    'Tez yopish/ochish, sekin tarmoq va xatodan keyingi retry’da oxirgi tahrir saqlanadi.',
    'Revoke qilingan sessiya himoyalangan so‘rovlarni bajara olmaydi; token muddati tugaganda refresh ishlaydi.',
])
stage(1, 'Arxitektura va tekshiruvlarni tartibga keltirish', '2-3', [
    'Resume routeridan biznes operatsiyalarini servisga chiqarish; umumiy response va error kontraktlarini belgilash.',
    'Autosave uchun umumiy mexanizmni ajratish; ishlayotgan xatti-harakatni mavjud va yangi regressiya testlari bilan saqlash.',
    'Page size, filtr reset va o‘chirishdan keyingi ro‘yxatni yangilash; AI hash tarkibini to‘ldirish.',
    'Eskirgan test mocklarini tuzatish, lint/typecheck/test/build buyruqlarini CI’ga ulash.',
    'Dependency ro‘yxati, .env.example, README va .gitignore’ni to‘ldirish; cache fayllarini Git kuzatuvidan chiqarish.',
], [
    'Toza muhitda hujjatdagi buyruqlar bilan frontend/backend ishga tushadi.',
    '0, 1, 9, 10, 18, 19 va 20 ta rezyumeda barcha yozuvlarga yetib boriladi; filtr sahifani 1 ga qaytaradi.',
    'Resume kirishi o‘zgarsa AI keshi yangilanadi; CI’da test, typecheck va build o‘tadi.',
])

# 9. Roadmap phases 2 and 3
page('08 / Roadmap tafsiloti', '02-03. To‘lov va CRM')
stage(2, 'Billing va tarif ruxsatlari', '7-10', [
    'Free/Pro qoidalarini aniq belgilash: AI turlari, limit davri, PDF, premium shablonlar va obuna muddati.',
    'Payment, Subscription, WebhookEvent va UsageEvent yozuvlarini, holat almashish qoidalari bilan yaratish.',
    'Provider sandbox’da to‘lov yaratish, imzo/haqiqiylikni tekshirish va takror callbackni bir marta hisoblash.',
    'Tarif huquqlarini serverda tekshirish; parallel AI so‘rovlarida limitni atomar band qilish va muvaffaqiyatsiz operatsiya hisobini belgilash.',
    'Billing UI: joriy tarif, qolgan limitlar, to‘lov holati, tarix va bekor qilish tartibi.',
], [
    'Muvaffaqiyatli, rad etilgan, bekor qilingan va takror webhook holatlari testdan o‘tadi.',
    'Bitta to‘lov yoki callback tarifni ikki marta uzaytirmaydi; frontenddagi soxta success ruxsat bermaydi.',
    'Free limitlari parallel so‘rovlar bilan oshirilmaydi; Pro muddati tugaganda ruxsat qayta hisoblanadi.',
    'To‘lovdan keyin UI va serverdagi obuna holati mos keladi; kerakli tranzaksiyalar jurnalga yoziladi.',
])
stage(3, 'Minimal operatsion CRM', '5-7', [
    'Administrator, support va faqat ko‘rish rollari uchun server ruxsatlari; admin sessiyasi himoyasi.',
    'Foydalanuvchilar qidiruvi, profil tafsiloti va bloklash/ochish; sabab hamda amal muallifini qayd qilish.',
    'To‘lov va obunalar ro‘yxati; tarifni qo‘lda o‘zgartirish uchun aniq sabab va audit yozuvi.',
    'AI so‘rovlari soni, xatolar, token/cost ma’lumotlari mavjud bo‘lsa sarf ko‘rinishi; murojaatlar holati.',
    'Sahifalash, filtrlash va amallar jurnalini o‘z ichiga olgan admin interfeys.',
], [
    'Oddiy foydalanuvchi admin endpointlariga kira olmaydi; rollar ruxsat matritsasiga mos ishlaydi.',
    'Muhim o‘zgartirishlarda kim, qachon, nimani va nima sababdan o‘zgartirgani saqlanadi.',
    'CRMdagi to‘lov, obuna va foydalanish sonlari backend yozuvlari bilan mos keladi.',
])

# 10. Roadmap phases 4 and 5
page('09 / Roadmap tafsiloti', '04-05. QA va ishga tushirish')
stage(4, 'Integratsion test va staging', '4-6', [
    'Alohida PostgreSQL test bazasida migratsiyalar, CRUD, egalik, cascade delete va sessiya testlari.',
    'Login → import/manual yaratish → tahrir → job-match → AI nusxa → PDF oqimini end-to-end tekshirish.',
    'AI timeout/noto‘g‘ri JSON, buzilgan fayl, offline holati va parallel so‘rovlarni tekshirish.',
    'Beshta shablonda ko‘p sahifali PDF, mobil ko‘rinish va uch tilni ko‘rib chiqish; landing matnlarini yangilash.',
], [
    'Muhim regressiya va integratsion testlar o‘tadi; ochiq kritik ruxsat yoki ma’lumot yo‘qotish xatosi qolmaydi.',
    'To‘lov sandbox’i, quota, CRM ruxsatlari va PDF matn qatlami staging’da tasdiqlanadi.',
    'Joriy hujjatlar va UI haqiqiy imkoniyatlarni tasvirlaydi; cheklovlar tushunarli ko‘rsatiladi.',
])
stage(5, 'Production release', '2-3', [
    'HTTPS, domen, CORS, cookie, runtime konfiguratsiyasi va provayder production kalitlarini sozlash.',
    'Health-check, xato/latency monitoringi, AI xarajati va PDF resurslari bo‘yicha kuzatuvni ulash.',
    'Zaxira nusxa yaratish va tiklashni amalda tekshirish; migratsiya va rollback tartibini yozish.',
    'Cheklangan pilot guruh bilan chiqarish; webhook, to‘lov, saqlash va xatolarni kuzatish.',
], [
    'Production health-check o‘tadi; muhim xato va limitlar uchun xabar kelishi sinovdan o‘tadi.',
    'Zaxiradan tiklash hamda oldingi release’ga qaytish jarayoni bajarib ko‘rilgan.',
    'Pilotda bloklovchi muammo qolmasa, foydalanuvchilarni bosqichma-bosqich kengaytirish tasdiqlanadi.',
])
callout('Release qarori uchun yakuniy mezon', 'Egalik va sessiya nazorati ishlaydi; saqlanmagan tahrir yo‘qolmaydi; to‘lov va limitlar serverda hisoblanadi; CRM rollari tekshirilgan; asosiy end-to-end oqimlar o‘tgan; backup, monitoring va rollback tayyor.')
add('Keyingi amaliy vazifa', 'h2')
add('00-bosqichdan boshlash: design ownership, User.resumes va autosave muammolarini tuzatish, so‘ng ularni takror yuz bermaydigan regressiya testlari bilan yopish. Har bosqichning natijasi keyingi ish uchun tekshirilgan asos bo‘ladi.', 'small')


SECTIONS = [
    'UMUMIY BAHO', 'ARXITEKTURA', 'KRITIK TOPILMALAR', 'ISHONCHLILIK',
    'QOLGAN ISHLAR', 'TEKSHIRUVLAR', 'ROADMAP', 'BOSQICHLAR 00-01',
    'BOSQICHLAR 02-03', 'BOSQICHLAR 04-05',
]

def draw_page(canvas, document):
    page_num = document.page
    canvas.saveState()
    canvas.setFillColor(GREEN)
    canvas.rect(0, PAGE_H - 6, PAGE_W, 6, fill=1, stroke=0)
    canvas.setFont('AuditBold', 9)
    canvas.setFillColor(NAVY)
    canvas.drawString(48, PAGE_H - 32, 'ResumeParser')
    canvas.setFont('Audit', 8)
    canvas.setFillColor(MUTED)
    label = SECTIONS[page_num - 1] if page_num <= len(SECTIONS) else 'DAVOMI'
    canvas.drawRightString(PAGE_W - 48, PAGE_H - 32, label)
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(.5)
    canvas.line(48, 42, PAGE_W - 48, 42)
    canvas.setFont('Audit', 7.8)
    canvas.drawString(48, 28, '12.11.2026  /  Kod auditi va tavsiya etilgan ish rejasi')
    canvas.drawRightString(PAGE_W - 48, 28, f'{page_num:02d} / 10')
    canvas.restoreState()

doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=A4, rightMargin=48, leftMargin=48,
    topMargin=58, bottomMargin=55, title='ResumeParser - loyiha tahlili va roadmap',
    author='Codex', subject='Arxitektura, kod sifati, tayyorlik va bosqichli ish rejasi',
    pageCompression=1,
)
doc.build(story, onFirstPage=draw_page, onLaterPages=draw_page)
print(OUTPUT)


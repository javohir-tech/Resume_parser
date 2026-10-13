from pathlib import Path
from html import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output/pdf/vue-boglanishlar-qollanma.pdf'
for name, file in [('Body','arial.ttf'),('Bold','arialbd.ttf'),('Mono','consola.ttf')]:
    pdfmetrics.registerFont(TTFont(name, 'C:/Windows/Fonts/' + file))
styles = {
    'title': ParagraphStyle('title', fontName='Bold', fontSize=26, leading=32, textColor=HexColor('#153B50'), spaceAfter=18),
    'h': ParagraphStyle('h', fontName='Bold', fontSize=14, leading=19, textColor=HexColor('#007F83'), spaceBefore=11, spaceAfter=7),
    'p': ParagraphStyle('p', fontName='Body', fontSize=10.5, leading=14.5, spaceAfter=8),
    'small': ParagraphStyle('small', fontName='Body', fontSize=9, leading=13, spaceAfter=7),
    'code': ParagraphStyle('code', fontName='Mono', fontSize=8.6, leading=11, backColor=HexColor('#EEF3F6'), borderPadding=10, spaceBefore=5, spaceAfter=11),
    'note': ParagraphStyle('note', fontName='Body', fontSize=10.5, leading=15.5, textColor=HexColor('#153B50'), backColor=HexColor('#E5F4F2'), borderPadding=10, spaceBefore=9, spaceAfter=15),
}
story=[]
def p(t, kind='p'): story.append(Paragraph(t, styles[kind]))
def h(t): p(t,'h')
def code(t): story.append(Preformatted(t.strip('\n'), styles['code']))
def page(n,t):
    if story: story.append(PageBreak())
    p('VUE 3  /  AMALIY QO‘LLANMA  /  '+n, 'small')
    p(t,'title')
def note(t): p(t,'note')
def source(label,url): p(f'Manba: <link href="{url}" color="#007F83">{label}</link>', 'small')

page('01','“Bog‘lash” degani nima?')
p('Vue’da bog‘lash deganda bir qiymatni uni ko‘rsatadigan joyga yoki bir hodisani unga javob beradigan funksiyaga ulash tushuniladi. Siz aloqani kodda yozasiz; Vue esa tegishli o‘zgarishlarni interfeysga yetkazadi.')
h('Avval uchta narsani ajratamiz')
p('<b>Holat (state)</b> - dastur eslab turadigan qiymat. Masalan: sarlavha, yangi experience ID si yoki forma ochiqmi degan boolean.')
p('<b>Ko‘rinish (UI)</b> - foydalanuvchi ko‘radigan sarlavha, tugma va forma.')
p('<b>Hodisa (event)</b> - nimadir sodir bo‘lgani haqidagi xabar. Masalan: tugma bosildi yoki formani yopish so‘raldi.')
code('const isOpen = ref(false)\n\n// Template ichida:\n<UCollapsible :open="isOpen" />')
p('Bu misolda isOpen - holat, UCollapsible - uni ko‘rsatadigan komponent, :open esa ular orasidagi aloqa. isOpen true bo‘lsa, komponentga open=true uzatiladi.')
note('Bog‘lash ma’lumotlar bazasiga saqlash degani emas. U komponentlar va interfeys orasida qiymat yoki hodisa qanday uzatilishini belgilaydi.')
h('Sizning komponentlaringiz')
code('ExperienceSection.vue          Parent (ota komponent)\n        |\n        +-- ResumeEditorSection.vue    Child (bola)\n                    |\n                    +-- UCollapsible   Ichki child')
p('Parent va child nisbiy tushunchalar: ResumeEditorSection o‘z parentiga nisbatan child, UCollapsible uchun esa parent hisoblanadi.')
p('Keyingi sahifalarda avval oddiy misollarni ko‘ramiz, so‘ng yangi experience qo‘shilganda uning formasi qanday ochilishini bosqichma-bosqich tahlil qilamiz.')
p('Misollar Vue 3 va &lt;script setup lang="ts"&gt; uchun. Oddiy Vue loyihasida ref, watch va toRef vue paketidan import qilinadi; Nuxt ularni odatda avtomatik import qiladi.', 'small')

page('02','Reaktivlik va template yozuvlari')
h('ref: Vue kuzata oladigan qiymat')
code("import { ref } from 'vue'\n\nconst title = ref('Ish tajribasi')\n\n// Script ichida qiymatni o‘zgartirish:\ntitle.value = 'Yangi tajriba'")
p('ref qiymatni reaktiv qobiq ichida saqlaydi. Shu qiymat template ichida ishlatilgan bo‘lsa, o‘zgarganida Vue kerakli ko‘rinishni yangilaydi. Oddiy let o‘zgaruvchini almashtirishning o‘zi bunday yangilanishni ta’minlamaydi.')
code('<h2>{{ title }}</h2>\n<MySection :section_header="title" />')
p('Bu yerda {{ title }} qiymatni matn sifatida chiqaradi. :section_header="title" esa qiymatni komponentning propiga beradi. Template ichida yuqoridagi ref avtomatik ochiladi, shuning uchun title.value yozish shart emas.')
h('Bir xil ko‘rinadigan, ammo turlicha ishlaydigan yozuvlar')
code('<MySection section_header="title" />\n<MySection :section_header="title" />')
p('Birinchi qatorda childga aynan “title” matni keladi. Ikkinchi qatorda title o‘zgaruvchisining qiymati, masalan “Yangi tajriba”, keladi. Ikki nuqta - v-bind ning qisqa yozilishi.')
code('<button :disabled="isCreating" @click="save">\n    Saqlash\n</button>')
p('<b>:disabled</b> - tugma xususiyatini qiymatga bog‘laydi. <b>@click</b> - bosilish hodisasini save funksiyasiga bog‘laydi. @ belgisi v-on ning qisqa yozilishi.')
note('“:” bilan qiymat berasiz. “@” bilan hodisani tinglaysiz. “v-model” bilan qiymat va uni yangilash hodisasini birga ulaysiz.')
h('Yangilanish qachon ko‘rinadi?')
p('Reaktiv qiymat scriptda yangilanadi, DOM yangilanishlari esa Vue tomonidan navbatga yig‘iladi. O‘zgargan elementga focus berish yoki uning o‘lchamini olish kerak bo‘lsa, nextTick kerak bo‘lishi mumkin. Faqat open holatini almashtirish uchun uni qo‘shish shart emas.')

page('03','Props: qiymat parentdan childga')
p('Prop - child tashqaridan qabul qiladigan parametr. defineProps child qaysi parametrlarni kutishini e’lon qiladi. Haqiqiy qiymatni parent template orqali beradi.')
h('Parent: qiymatni saqlaydi va uzatadi')
code("const heading = ref('Ish tajribasi')\n\n// Template:\n<ResumeEditorSection :section_header=\"heading\" />")
h('Child: qiymatni qabul qiladi va ko‘rsatadi')
code('const props = defineProps<{\n    section_header: string\n}>()\n\n// Template:\n<h2>{{ props.section_header }}</h2>')
code('heading  -->  section_header  -->  ekrandagi sarlavha')
p('heading va section_header nomlari bir xil bo‘lishi shart emas. Chapdagi section_header - childdagi prop nomi; o‘ngdagi heading - parentdagi ifoda.')
p('Parent heading ni o‘zgartirsa, child yangi prop qiymatini oladi. Child props.section_header ga qiymat tayinlamaydi: yangilash kerak bo‘lsa, parentga hodisa yuboradi.')
h('Sizdagi last_item_id')
code('// Parent:\nconst last_item_id = ref<string | null>(null)\n\n// Parent template:\n<ResumeEditorSection :last_item_id="last_item_id" />\n\n// Childdagi props turi ichida:\nlast_item_id?: string | null')
p('Bu aloqada yangi ID parentdan childga keladi. Ammo propning o‘zi openedForms ga hech narsa qo‘shmaydi. ID kelganda nima qilish kerakligini watch bilan alohida belgilaysiz.')
note('“?” prop uzatilmasligi ham mumkinligini bildiradi. Boshqa sectionlar last_item_id bermasa, optional prop mos keladi. Callback null va undefined holatlarini tekshirishi kerak.')
p('Object va array props ichki ma’lumotlari umumiy reference orqali o‘zgarishi mumkin. Tushunarli ma’lumot oqimi uchun ularni yangilash mas’uliyatini ham aniq saqlang.', 'small')
source('Vue: Props','https://vuejs.org/guide/components/props.html')

page('04','Emit: child parentga xabar beradi')
p('emit - komponent hodisasini chiqarish. Parent shu hodisani tinglab, o‘z funksiyasini ishga tushiradi. defineEmits esa qanday hodisalar va argumentlar mavjudligini e’lon qiladi.')
h('Childdagi tugma')
code("const emit = defineEmits<{\n    add: []\n    delete: [id: string]\n}>()\n\n// Template:\n<button @click=\"emit('add')\">Qo‘shish</button>")
h('Parentdagi tinglovchi')
code('<ResumeEditorSection @add="handleAddSection" />')
code('Tugma bosildi -> emit("add") -> handleAddSection()')
p('add: [] hodisa qo‘shimcha argument yubormasligini bildiradi. delete: [id: string] esa o‘chirish hodisasi string ID yuborishini bildiradi.')
code('// Child:\nemit("delete", "exp-42")\n\n// Parent template:\n<ResumeEditorSection @delete="deleteExperience" />\n\n// Natija: deleteExperience("exp-42") chaqiriladi.')
h('$event nimani anglatadi?')
code('<ResumeEditorSection\n    @delete="deleteExperience($event)"\n/>')
p('Bu misolda $event - child yuborgan "exp-42" qiymati. Oddiy HTML click hodisasida esa u brauzerning hodisa obyekti bo‘ladi. Qiymat turi qaysi hodisa tinglanayotganiga bog‘liq.')
note('emit ma’lumotni saqlamaydi va server so‘rovini o‘zi bajarmaydi. Parentning hodisa handleri bajaradigan ishni siz belgilaysiz.')
h('Asinxron create haqida')
p('Parentdagi handleAddSection async bo‘lishi mumkin. Child emit chaqiruvini await qilish orqali parent yaratgan ID ni ololmaydi. Sizdagi yechim: parent so‘rov tugashini kutadi, so‘ng ID ni last_item_id propida qaytaradi.')
p('Komponent hodisalari DOM hodisalari kabi barcha ajdod komponentlarga avtomatik ko‘tarilmaydi. Yuqoriroqqa uzatish kerak bo‘lsa, tegishli komponent uni qayta chiqarishi mumkin.', 'small')
source('Vue: Component Events','https://vuejs.org/guide/components/events.html')

page('05','v-model va defineModel')
p('Bir qiymatni parent ham, child ham o‘zgartirishi kerak bo‘lsa, v-model qulay. Masalan, parent formani ochadi, childdagi yopish tugmasi esa uni yopadi.')
h('Parent tomoni')
code('const isOpen = ref(false)\n\n// Template:\n<MyForm v-model:open="isOpen" />')
h('Child tomoni')
code("const open = defineModel<boolean>('open', {\n    required: true\n})\n\nfunction closeForm() {\n    open.value = false\n}\n\n// Template:\n<button @click=\"closeForm\">Yopish</button>")
p('Parent isOpen ni o‘zgartirsa, child yangi qiymatni oladi. Child open.value ga yozsa, model yangilash hodisasi chiqadi va parentdagi isOpen yangilanadi.')
h('Qisqa yozuvning ochilgan ko‘rinishi')
code('<MyForm\n    :open="isOpen"\n    @update:open="isOpen = $event"\n/>')
p('Demak, ikki tomonlama aloqa ikkita yo‘ldan iborat: qiymat prop orqali pastga, yangi qiymat esa update:open hodisasi orqali yuqoriga boradi. defineModel shu prop va hodisa uchun qulay ref beradi.')
note('Childdagi defineModel ning o‘zi parent o‘zgaruvchisini ulab qo‘ymaydi. Parent ham v-model ishlatishi yoki update hodisasini qo‘lda tinglashi kerak.')
h('Nomli va nomsiz model')
code("defineModel<string>()         // modelValue\ndefineModel<boolean>('open')  // open\n\n<MyInput v-model=\"name\" />\n<MyForm v-model:open=\"isOpen\" />")
p('defineModel Vue 3.4+ da mavjud. Misollardagi required: true parent model qiymatini berishini talab qiladi. Default berilib, parent qiymati undefined qolsa, boshlang‘ich qiymatlar farq qilishi mumkin.', 'small')
source('Vue: Component v-model','https://vuejs.org/guide/components/v-model.html')

page('06','watch: o‘zgarishga javob berish')
p('Prop ID ni yetkazadi; watch esa shu ID o‘zgarganda qo‘shimcha harakat bajaradi. Sizda bu harakat - tegishli formani ochish.')
code('watch(\n    () => props.last_item_id,\n    (id) => {\n        if (!id) return\n        open.value = true\n        handleOpenForm(id)\n    }\n)')
h('Nega () => props.last_item_id?')
p('Bu funksiya getter deb ataladi: chaqirilganda joriy prop qiymatini qaytaradi. Vue uning ichida qaysi reaktiv qiymat o‘qilganini kuzatadi. Qiymat o‘zgarsa, callbackni ishga tushiradi.')
code('// Noto‘g‘ri: string / null qiymat uzatilmoqda\nwatch(props.last_item_id, callback)\n\n// To‘g‘ri: qiymatni o‘qiydigan funksiya uzatilmoqda\nwatch(() => props.last_item_id, callback)')
p('Birinchi variant taxminan watch("exp-42", callback) deyishga o‘xshaydi. Bu matn o‘zining qayerdan kelganini bildirmaydi. TypeScript uni kuzatish manbasi sifatida qabul qilmaydi.')
h('ref uchun esa getter shart emas')
code('const lastId = ref<string | null>(null)\nwatch(lastId, (id) => { /* ... */ })\n\n// Prop uchun muqobil:\nconst propId = toRef(props, "last_item_id")\nwatch(propId, (id) => { /* ... */ })')
p('ref o‘zi reaktiv manba. lastId.value esa uning hozirgi qiymati. Shu sabab refni kuzatishda watch(lastId, ...) ishlatiladi.')
note('Oddiy watch boshlang‘ich qiymat uchun callbackni darhol ishlatmaydi. Agar mount paytida kelgan ID ni ham ochish kerak bo‘lsa, uchinchi argument sifatida { immediate: true } bering.')
p('Bir xil string ID yana tayinlansa, qiymat o‘zgarmagani uchun callback qayta ishlamaydi. Yangi experience uchun yangi ID keladigan jarayonda bu muammo emas. Bu holatga deep: true kerak emas.')
source('Vue: Watchers','https://vuejs.org/guide/essentials/watchers.html')

page('07','Sizdagi experience qanday ochiladi?')
p('Quyidagi oqim loyiha kodidagi ExperienceSection, ResumeEditorSection va useExperience asosida tushuntirilgan. Namunalardagi o‘zgarishlar tavsiya sifatida berilgan.')
h('1. Parent yangi elementni yaratadi')
code('const last_item_id = ref<string | null>(null)\n\nconst handleAddSection = async () => {\n    const id = await createExperience(resumeStore.resume.id)\n    if (id) last_item_id.value = id\n}\n\n// Parent template qismi:\n<ResumeEditorSection\n    @add="handleAddSection"\n    :last_item_id="last_item_id"\n/>')
p('Child emit("add") chiqaradi. createExperience server javobini olgach, experience ro‘yxatiga element qo‘shadi va ID qaytaradi. So‘rov muvaffaqiyatsiz bo‘lsa null qaytadi; if tekshiruvi sabab yangi ID uzatilmaydi.')
h('2. Child ID ni ochiq formalar to‘plamiga yozadi')
code('const openedForms = ref<Set<string>>(new Set())\n\nconst handleOpenForm = (id: string) => {\n    openedForms.value.clear()\n    openedForms.value.add(id)\n}')
p('Set takrorlanmaydigan ID lar to‘plami. clear() oldingi barcha ID larni olib tashlaydi, add(id) esa yangi ID ni kiritadi. Shunday qilib, bir vaqtning o‘zida bitta ichki forma ochiq turadi.')
h('3. Template Set dan ochiqlikni hisoblaydi')
code('<UCollapsible :open="openedForms.has(item.id)" />')
p('Agar item.id to‘plamda bo‘lsa, has true qaytaradi. Vue ref ichidagi Set o‘zgarishini kuzatadi va open qiymatini yangilaydi. Bir nechta forma ochiq qolsin desangiz, handleOpenForm ichidagi clear() ni olib tashlash yetarli.')
note('Tashqi section va ichki forma ikki alohida holat: open tashqi sectionni boshqaradi, openedForms esa ichki formalarni. Watch ichidagi open.value = true tashqi section ham ochiq bo‘lishini ta’minlaydi.')

page('08','Teskari aloqa va amaliy tekshiruv')
h('Foydalanuvchi collapsible ni o‘zi ochsa-chi?')
code('<UCollapsible\n    :open="openedForms.has(item.id)"\n    @update:open="\n        $event\n            ? handleOpenForm(item.id)\n            : openedForms.delete(item.id)\n    "\n/>')
p('Bu yerda :open joriy holatni beradi. @update:open esa komponent yuborgan yangi boolean qiymatni qabul qiladi. true kelsa ID qo‘shiladi; false kelsa ID o‘chiriladi. Keyingi renderda has(item.id) yangilangan qiymatni qaytaradi.')
p('openedForms.has(item.id) funksiya natijasi bo‘lgani uchun unga qiymat tayinlab bo‘lmaydi. Shu sabab v-model:open="openedForms.has(item.id)" o‘rniga yuqoridagi prop va hodisa juftligi mos keladi.')
h('Sizdagi add_pending haqida')
code('// Childda mavjud:\nconst add_pending = defineModel<boolean>("add_pending", {\n    default: false\n})\n\n// Parent hozir qiymatni shunday uzatadi:\n<ResumeEditorSection :add_pending="isCreating" />')
p('Bu ulanishda parent qiymatni beradi, ammo update:add_pending hodisasini tinglamaydi. Child add_pending ga yozsa, parentdagi isCreating shu yozuv bilan yangilanmaydi. Child faqat loading/disabled uchun o‘qisa, oddiy prop yetarli. Ikki tomondan boshqarish talab qilinsagina v-model tanlang.')
h('O‘zingizni tekshiring')
p('<b>1.</b> Childga faqat sarlavha kerak. Nima ishlatasiz?<br/><b>2.</b> Child o‘chirish tugmasi bosilganini bildirishi kerak. Nima ishlatasiz?<br/><b>3.</b> Parent ham, child ham open ni yangilaydi. Nima ishlatasiz?<br/><b>4.</b> Yangi ID kelganda Set ga qo‘shish kerak. Nima ishlatasiz?')
p('<b>Javoblar:</b> 1 - props. 2 - emit va parentdagi @delete. 3 - v-model va defineModel. 4 - getter bilan watch.', 'small')
note('Qiymat qayerda saqlanadi? Uni kim o‘zgartiradi? O‘zgarganda kimga xabar kerak? Shu uch savol qaysi bog‘lanishni tanlashni aniqlaydi.')
p('Asos: suhbatdagi savollar va loyiha fayllari (2026-10-13). Rasmiy Vue havolalari tegishli mavzu sahifalarida berilgan. Qo‘llanma loyiha kodini o‘zgartirmaydi.', 'small')

def footer(c,doc):
    c.setStrokeColor(HexColor('#D4E2E8')); c.line(46,44,549,44)
    c.setFont('Body',8); c.setFillColor(HexColor('#59717D'))
    c.drawString(46,30,'Vue’da bog‘lanishlar | ResumeParser misolida')
    c.drawRightString(549,30,str(doc.page))
doc=SimpleDocTemplate(str(OUT), pagesize=(595.28,841.89), rightMargin=46,leftMargin=46,topMargin=42,bottomMargin=58, title='Vue’da bog‘lanishlar: props, emit, v-model va watch',author='Codex')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)


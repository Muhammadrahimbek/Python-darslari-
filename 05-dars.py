#05-dars, String/Matn
#05/10/2022
#M.Rahimov

# STRING (matn) — Pythondagi eng mashxur ma'lumot turlaridan biri. Avvalgi darsda ko'rganimizdek, o'zgaruvchiga matn yuklash uchun matn qo'shtirnoq (" ") yoki birtirnoq (' ') ichida yozilishi kerak.

#ism='Muhammadrahimbek'
#shahar='Кукон'
#viloyat="Фаргона"
#print(ism,shahar,viloyat)

# Pythonda matnlar Unicode jadvalidagi istalgan belgilaridan iborat bo'lishi mumkin (jumladan o'zbek, arab, hind, xitoy alifbosidagi harflar yoki turli emoji-smayliklar).
#matn='Men yangi 💻 sotib oldim'
#print(matn)

# STRING USTIDA AMALLAR
# Matnlarni qo'shish operatori (+)

#ism='Muhammadrahimbek'
#print('Mening ismim '+ism)

#ism='Muhammadrahimbek'
#familiya='Rahimov'
#print(ism+familiya)

#ism='Muhammadrahimbek'
#familiya='Rahimov'
#print(ism+familiya)
#print(ism+' '+familiya)

# f-string
# Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni birlashtirish uchun f-string usulidan f"{matn1} {matn2}" ham foydalansak bo'ladi:
#ism='Muhammadrahimbek'
#familiya='Rahimov'
#ism_sharif=f'{ism} {familiya}, {ism} {familiya}'
#print(ism_sharif)
#print('Mening ismim',f'{ism}')
#print(f'Salom mening ismim {ism}, {ism} {familiya}')

# Maxsus belgilar
# Matnga bo'shliq qo'shish uchun \t belgisidan, yangi qatordan boshlash uchun \n belgisidan foydalanamiz
#print('Hello World!')
#print('Hello \tWorld!')
#print('Hello \nWorld!')

# STRING METODLARI
# Pythonda string ustida amalga oshirish mumkin bo'lgan tayyor amallar to'plami mavjud. Bunday amallar to'plami metodlar deb ataladi.
# Metodlarni qo'llash uchun metod nomi matndan so'ng .metod_nomi() ko'rinishida yoziladi. Keling shunday metodlarning ba'zilari bilan tanishaylik

# upper() metodi matndagi har bir harfni katta harfga o'zgartiradi.
#ism='muhammadrahimbek'
#familiya='rahimov'
#ism_sharif=f'{ism} {familiya}'.upper()
#print(ism_sharif.upper())

# lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.
#ism='muhammadrahimbek'
#familiya='rahimov'
#ism_sharif=f'{ism} {familiya}'.upper()
#print(ism_sharif.lower())

# title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi.
#ism='muhammadrahimbek'
#familiya='rahimov'
#ism_sharif=f'{ism} {familiya}'.upper()
#print(ism_sharif.title())

# capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.
#ism='muhammadrahimbek'
#familiya='rahimov'
#ism_sharif=f'{ism} {familiya}'.upper()
#print(ism_sharif.capitalize())

# lstrip() — matn boshidagi bo'shliqni olib tashlaydi
#meva='     olma    '
#print(meva)
#print('Men '+meva+" yaxshi ko'raman")
#print('Men '+meva.lstrip()+" yaxshi ko'raman")

# rstrip() — matn oxiridagi bo'shliqni olib tashlaydi
#print('Men '+meva.rstrip()+" yaxshi ko'raman")

# strip() — matn boshi va oxiridagi bo'shliqni olib tashlaydi
#print('Men '+meva.strip()+" yaxshi ko'raman")

# INPUT — FOYDALANUVCHI BILAN MULOQOT
# Shu paytgacha biz o'zgaruvchilarning qiymatini dasturning ichida berayotgan edik. Keling endi qiymatni o'zimiz emas, balki dastur foydalanuvchilariga kiritish imkonini beramiz.
# Buning uchun input() funktsyasidan foydalanamiz.

#ism=input('Ismingiz nima')
#print("Assalomu aleykum"+ism)


# AMALIYOT

#kocha="Bog'bon"
#mahalla="Sog'bon"
#tuman="Bodomzor"
#viloyat="Samarqand"
#Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
#print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

#Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
#print(f"{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati")

#manzil=f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
#print(manzil)
#print(manzil.upper())
#rint(manzil.lower())
#print(manzil.title())
#print(manzil.capitalize())











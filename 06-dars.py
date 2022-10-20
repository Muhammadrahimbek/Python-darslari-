#06-dars, SONLAR
#06/10/2022
#M.Rahimov

# INTEGERS — BUTUN SONLAR
# Butun sonlarni ham o'zgaruvchida saqlash, ularning ustida qo'shish (+), ayirish (-), ko'paytirish(*), bo'lish (/) kabi arifmetik amalarni bajarish mumkin:
#a=20
#b=10
#c=a+b
#print(c)

# FLOATS — O'NLIK SONLAR
# Pythonda o'nlik sonlar floating point numbers yoki qisqa qilib floats deyiladi. "Floating point numbers" atamasini o'zbek tiliga "suzuvchi nuqtali sonlar" deb tarjima qilish mumkin. Ingliz tilida o'nlik sonlarni yozishda vergul (,) emas nuqta (.) belgisi ishlatiladi, va bu nuqta sonning katta kichikligiga qarab joyi o'zgargani uchun "floating" (suzuvchi) deyiladi.
#pi=3.14159
#radius=5
#diametr=2*radius
#print("Aylana uzunligi, ", pi*diametr, " ga teng")

# BUTUN SONDAN O'NLIK SONGA
# Avval aytganimizdek ikki butun sonni bo'lish (/) natijasida o'nlik son hosil bo'ladi (natija butun bo'lsa ham)
#a=50
#b=5
#c=a/b
#print(c)
# Natija butun son bo'lishi uchu (//) dan foydalanish kerak
#c=a//b
#print(c)
# Shuningdek butun va o'nlik sonlar o'rtasidagi har qanday arifmetik amallarning natijasi ham o'nlik son bo'ladi.
#a=5
#b=3.0
#print(a+b)
#print(a*b)
#print(a-b)
#print(a/b)

# type() orqali variable ni turini bilsa bo'ladi
#print(type(a))
#print(type(pi))

# UZUN SONLARNI KIRITISH
# Uzun sonlarni kiritishda, qulaylik uchun, raqamlarni pastki chiziq (_) yordamida guruhlash mumkin. Python - son tarkibidagi pastki chiziqlarni (_) inobatga olmasdan, uzun sonligicha qabul qiladi.
#aholi_soni=7_594_354_600
#print(aholi_soni)

# BIR NECHTA O'ZGARUVCHIGA QIYMAT BERISH
# Birdaniga bir nechta o'zgaruvchiga qiymat berish uchun o'zgaruvchilar va ularga mos qiymatlar vergul (,) bilan ajratiladi:
#x, y, z = 10, 5.5, 20
#a=x*y-z
#print(a)

# KONSTANTA
# Aksar dasturlash tillarida konstant qiymatlar tushunchasi bor. Konstantlar o'zgarmas bo'ladi (misol uchun ning qiymati konstant, o'zgarmas qiymat). Pythonda konstant tushunchasi yo'q, shuning uchun dasturchilar bunday o'zgaruvchilarning nomini katta harflar bilan yozadilar (ogohlantirish sifatida). Bu albatta qat'iy qonun emas, lekin kelajakda o'zgaruvchilar orasida konstant qiymatlarni ajratish uchun yaxshi usul
#PI=3.14159
#radius=20
#diametr=2*radius
#print("Aylana uzunligi=",PI*diametr)

# O'ZGARUVCHI TURINI ALMASHTIRISH
# Keling quyidagi misolni ko'raylik, maqsadimiz ism va yosh degan ikki o'zgaruvchini yangi xabar degan o'zgaruvchiga yuklab, "Jobir 16 yoshda" degan matnni konsolga chiqarish:
#ism='Jobir'
#yosh=36
#xabar=ism +' '+ yosh+ ' yoshda'
#print(xabar)
# Afsuski, kutilgan natija o'rniga xatolik chiqdi. Agar xatoni ingliz tilidan tarjima qilsak, matn (str) va son (int) ni jamlab bo'lmaydi degan ma'no chiqadi.
# Demak Pythonda matn (string) va son (int, float) turidagi o'zgaruvchilarni jamlab bo'lmas ekan. Xo'sh, bunga yechim bormi? Albatta.
# Pythonda bir turdagi o'zgaruvchini boshqa turga o'tkazish mumkin, bu ingliz tilida typecasting detiladi. Buning uchun Pythonda mahsus funktsiyalar bor, keling ular bilan tanishamiz:
    # str()— int yoki float turidagi sonlarni matnga o'zgartiradi
    # int()— matn yoki float ko'rinishidagi qiymatlarni butun songa o'zgartiradi. Bunda matn butun son ko'rinishida bo'lishi kerak
    # float()— matn yoki int ko'rinishidagi qiymatlarni o'nlik songa o'zgartiradi
#xabar=ism +' '+ str(yosh)+ ' yoshda'
#print(xabar)

# INPUT() VA SONLAR
# Avvalgi darsimizda foydalanuvchidan ma'lumot olish uchun input() funktsyasidan foydalanishni o'rgandik. Kelin endi shu funktsiya yordamida foydalanuvchidan son olishni ko'raylik. Quyidagi kod foydalanuvchining tug'ilgan yilini so'raydi va uning yoshini hisoblab beradi
#t_yil=input("Tug'ilgan yilingizni kiriting ")
#yosh=2022-t_yil
#print("Siz",yosh,"yoshda ekansiz")
# Gap shundaki, input() funktsiyasi har qanday kiritilgan qiymatni matn (string) ko'rinishida qabul qiladi (garchi biz son kiritgan bo'lsak ham). Keling, konsolda t_yil degan o'zgaruvchining turini tekshirib ko'ramiz.
#yosh=2022-int(t_yil)
#print("Siz",yosh,"yoshda ekansiz")

# AMALIYOT

# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
#a=int(input("Istalgan son kiriting "))
#print(a, "ning kvadrati",a**2, "ga teng")
#print(a, "ning kubi", a**3, "ga teng")

#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
#yosh=int(input("Yoshingiz nechida? "))
#t_yil=2022-yosh
#print("Siz", t_yil, "yilda tug'ilgansiz")

#Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
#a=float(input("Birinchi sonni kiriting: "))
#b=float(input("Ikkinchi sonni kiriting: "))
#print(a, "+", b, "=",a+b)
#print(a, "-", b, "=",a-b)
#print(a, "*", b, "=",a*b)
#print(a, "/", b, "=",a/b)
#10-dars, IF-ELSE
#11/10/2022
#M.Rahimov

# TARMOQLANISH
# Shu vaqtgacha yozgan dasturlarimizga e'tibor bersangiz, dasturimiz yuqoridan pastga qarab qatorma-qator bajarilib keldi. Bu chiziqli dastur deyiladi. Voqelikda esa aksar dasturlar ma'lum bir shart bajarilishi (yoki bajarilmaganiga) ko'ra kodning bir qismidan boshqa qismiga "sakrab" o'tishi tabiiy hol. Dasturlashda bu tarmoqlanish deb ataladi
# if OPERATORI
# if so'zi ingliz tilidan "agar" deb tarjima qilinadi va deyarli barcha dasturlash tillarida shartlarni yozish uchun foydalaniladi.

#avtolar=['audi', 'bmw','mersedes','volvo','hyundai']
#for avto in avtolar:
#    if avto == 'bmw':
#        print(avto.upper())
#    else:
#        print(avto.title())
        
# 1-qatorda biz for tsiklini boshladik: avto ichidagi har bir avto uchun.
# 2-qatorda shart yozdik: agar avto bmw ga teng bo'lsa (bu yerda == belgisi tenglikni tekshirish belgisi hisoblanadi va "avto bmw ga tengmi?" deb o'qiladi).
# 3-qator yuqoridagi shartning badani hisoblanadi va faqatgina shart bajarilgandagina ishga tushadi va avto nomini hamma harflarini katta bilan yozadi (.upper() metodi).
# 4-qatorda yana bir yangi operator, else bilan tanishamiz. "Else" ingliz tilidan "aks holda" deb tarjima qilinadi va if sharti bajarilmaganda else qismi ichidagi kod bajariladi.
# 5-qator esa else (aks holda, ya'ni 2- qatordagi shart bajarilmaganda) ishga tushadi va avto nomining faqat birinchi harfini katta bilan yozadi (.title() metodi)
# Shart "badani" shartdan biroz o'ngga surib yoziladi (huddi for tsikli kabi). if/else dan keyin kelgan va o'ngga surib yozilgan har bir qator if/else shartining badani hisoblanadi.        

# TRUE/FALSE   
# Yuqorida shartni tekshirish uchun == operatoridan foydalandik. Bu operatorni oddiy tilga tarjima qilsak "tengmi?" degan ma'noni beradi.
# Agar shartning ikki tarafidagi qiymatlar teng bo'lsa ifoda TRUE qiymatini qaytaradi ("True" so'zi ingliz tilidan "haqiqiy" yoki "to'g'ri" deb tarjima qilinadi).
# Aksincha, qiymatlar tenglik qanoatlantirilmasa, ifoda FALSE qiymatini qaytaradi ("False" so'zini ingliz tilidan "yolg'on" deb tarjima qilsak bo'ladi).
# Quyidagi misollarga e'tibor bering. Biz ism degan o'zgaruvchi yaratdik, va unga 'Ali' matnini yukladik. Keling endi == yordamida ism ning qiymatini tekshirib ko'ramiz:
# Konsolga yozib tekshiramiz
#ism='Ali'
# Ko'rib turganingizdek avval ism=='Ali' (ism 'Ali' ga tengmi?) deb so'raganimizda, ifoda TRUE (Ha) degan javobni qaytardi, keyin esa ism=='Vali' (ism 'Vali' ga tengmi?) deb so'raganimizda esa, ifoda FALSE (Yo'q) deb qiymat qaytardi.
# Demak, if/else bog'lamasida, if ning badani ifoda True bo'lganda, else ning badani esa ifoda False bo'lganda bajariladi.

# MATNLARNI SOLISHTIRISH
# Aksar tizimlar foydalanuvchi kiritgan matnni ma'lum bir ko'rinishga keltirib oladi. Buning sababi, kompyuter uchun 'Ali', 'ALI', va 'ali' bu uchta turli hil ism. Ularni solishtirish uchun esa bir ko'rinishga keltirib olish kerak.
# Tasavvur qiling siz yangi email manzil ochmoqchisiz, va o'zingizga yangi foydalanuvchi ismini tanlashingiz kerak. Kompyuter siz kiritgan foydalanuvchi ismini tizimdagi mavjud foydalanuvchilar bilan solishtiradi va agar ism band bo'lsa sizga boshqa ism tanlashni aytadi. Solishtirish jarayonida esa, siz tanlagan ismni kichik harflarga o'tkazib, boshqa ismlar bilan solishtiradi.
# Xo'sh, turli ko'rinishda yozilgan matnlarni qanday qilib solishtiramiz? Juda oddiy. Matnlarni solishtirishdan avval .lower() metodi yordamida kichik harflar ko'rinishiga keltirib olamiz:

#ism=input("Ismingiz nima?\n>>>")
#if ism.lower()=="ali":
#    print("Hush kelibsiz!")
#else:
#    print(f"Uzr {ism.title()}, biz Alini kutyapmiz")

# QIYMATLARNING TENG EMASLIGINI TEKSHIRISH
# Agar ikki qiymatning teng emasligini tekshirish talab qilinsa, != operatoridan foydalanilamiz.
#ism=input("Ismingiz nima?\n>>> ")
#if ism.lower() != 'ali':
#    print(f"Uzr, {ism.title()}, biz Alini kutyapmiz")
#else:
#    print("Salom, Ali")

# SONLARNI SOLISHTIRISH
# Sonlarni solishtirishda yuqoridagi teng (==) va teng emas (!=) shartlariga qo'shimcha ravishda quyidagi mantiqiy shartlar ham qo'shiladi:
    # Kichik: a<b
    # Kichik yoki teng: a<=b
    # Katta: a>b
    # Katta yoki teng: a>=b

#javob=float(input("12x6 nechiga teng?\n>>> "))
#if javob != 72 :
#    print("Javob xato!")

#yosh=int(input("Yoshingiz nechida?\n>>> "))
#if yosh >= 18 :
#    print("Xush kelibsiz!")
#else:
#    print("Kirish mumkin emas!")

#login=input("Yangi login tanlang: ")
#if len(login)<=5 :
#    print("Login 5 harfdan ko'proq bo'lishi lozim!")

#yil=int(input("Tug'ilgan yilingizni kiriting: "))
#if 2020-yil<18 :
#    print(f"Sizning yoshingiz {2020-yil}da ekan.")
#    print("Kirish mumkin emas!")
#else:
#    print("Xush kelibsiz!")

# BIR QATOR if/else
# Qisqa kodlar uchun shart va uning badanini 1 qatorga jamlab yozishimiz ham mumkin:
         
#yosh=int(input("Yoshingiz nechchida?>>>"))
#if yosh>65 : print("Siz COVID-19 risk guruxida ekansiz!")

#x, y = 80, 70
#print("x>y") if x>y else print("x<y")



# AMALIYOT
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car == "gm":
#        print(car.upper())
#    else:
#        print(car.title())

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car !="gm":
#        print(car.title())
#    else:
#        print(car.upper())

#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
#login=input("Login ismingizni kiriting:>>>")
#if login.lower() == "admin":
#    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
#else:
#    print(f"Xush kelibsiz, {login.title()}!")

#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
#x, y = input("2 ta son kiriting:\n>>> "), input(">>> ")
#if x==y : print("Sonlar teng ekan")

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
#son=int(input("Istalgan sonni kiriting:\n>>> "))
#print("Manfiy son") if son<0 else print("Musbat son")

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
#son=int(input("Istalgan sonni kiriting:\n>>> "))
#print(son**(1/2)) if son>0 else print("Musbat son kiriting")





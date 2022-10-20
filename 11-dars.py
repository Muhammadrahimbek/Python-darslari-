#11-dars, if-elif-else KETMA-KETLIGI
#14/10/2022
#M.Rahimov

# Dastur davomida bir nechta shartni tekshirish talab qilinishi mumkin. Bunday holatda biz if-elif-else ketma-ketligidan foydalanamiz. elif - else va if so'zalrining jamlanmasi bo'lib, "aks holda, agar..." deb tarjima qilinadi. Bunday if bilan boshlangan ketma-ketlik bir nechta elif lardan iborat bo'lishi mumkin.
# Python avval if shartini tekshiradi, shart bajarilmasa elif ga o'tadi, birinchi elif sharti bajarilmasa keyingi elif ga o'tadi va hokazo davom etaveradi.
# Diqqat! if-elif-else ketma-ketlikda biror shart bajarilishi bilan, Python qolgan shartlarni tekshirmaydi.

# Keling bir misol ko'ramiz. Hayvonot bo'giga kirish quyidagicha belgilangan:
# 4 yoshdan kichik bolalarga kirish bepul
# 4 yoshdan 12 yoshgacha kirish 5000 so'm
# 12 yoshdan kattalarga 10000 so'm
# Foydalanuvchidan yoshini so'rab, hayvonot bog'iga kirish chiptasi narhini chiqaruvchi dastur yozamiz.

#yosh=int(input("Yoshingiz nechchida?\n>>> "))
#if yosh<4:
#    print("Sizga kirish bepul!")
#elif yosh<12:
#    print("Sizga kirish 5000 so'm")
#else:
#    print("Sizga kirish 10000 so'm")

# Kod yozishda yaxshi amaliyotlardan biri, kodlarni qisqa yozish va buyruqlarni qayta-qayta takrorlamaslik. Bu kelajakda kodni o'zgartirishda ham juda qo'l keladi.
#yosh=int(input("Yoshingiz nechchida?\n>>> "))
#if yosh<=4:
#    price=0
#elif yosh<=12:
#    price=5000
#else:
#    price=10000
#print(f"Sizga kirish {price} so'm")

# Avval aytganimizdek, if-elif-else zanjirida bit nechta elif lar bo'lishi mumkin. Misol uchun, hayvonot bog'i qariyalar uchun chegirma e'lon qilsa, kodimizni quyidagicha o'zgartirishimiz mumkin:
#yosh=int(input("Yoshingiz nechchida?\n>>> "))
#if yosh<=4:
#    price=0
#elif yosh<=12:
#    price=5000
#elif yosh<=65:
#    price=10000
#else:
#    price=8000
#print(f"Sizga kirish {price} so'm!")

# if-elif-else zanjirida ham else qismi majburiy emas:
#yosh=int(input("Yoshingiz nechchida?\n>>> "))
#if yosh<=4:
#    price=0
#elif yosh<=12:
#    price=5000
#elif yosh<=65:
#    price=10000
#elif yosh>65:
#    price=8000
#print(f"Sizga kirish {price} so'm!")

# AND, OR OPERATORLARI
# Yuqorida aytganimizdek, if-elif-else zanjirida shartlarning biri bajarilishi bilan, Python qolgan shartlarni tekshirmaydi va ularni bajarmaydi. Lekin ba'zida biz 2 yoki undan ko'p shartlarni tekshirishni talab qilishimiz mumkin, buing uchun AND va OR operatorlaridan foydalanamiz.

# OR OPERATORI
# OR ingliz tilidan "yoki" deb tarjima qilinadi, va ikki va undan ko'p shartlardan biri bajarilishini tekshirishda ishlatiladi. Quyidagi misolni ko'raylik, foydalanuvchidan hafta kunini so'raymiz va agar kun shanba yoki yakshanba bo'lsa, bugun dam olish kuni degan xabarni chiqaramiz, aks holda bugun ish kuni degan xabarni chiqaramiz:
#kun=input("Bugun nima kun?\n>>> ")
#if kun.lower()=="shanba" or kun.lower()=="yakshanba":
#    print("Bugun dam olish kuni!")
#else:
#    print("Bugun ish kuni!")

# AND OPERATORI
# AND ingliz tilidan "va" deb tarjima qilinadi, va ikki va undan ko'p shartlarning barchasi bajarilishini tekshirishda ishlatiladi. AND operatori bilan yozilgan shartlarning barchasi bajarilgandagina TRUE qiymati qaytadi, agar shartlardan biri bajarilmay qolsa ham FALSE qiymati qaytadi.
#kun=input("Bugun nima kun?>>> ")
#harorat=float(input("Harorat nechi?>>> "))
#if kun.lower()=="yakshanba" and harorat>30:
#    print("Cho'milgani kettik")
#else:
#    print("Uyda dam olamiz")

# BIR NECHTA SHARTLARNI KETMA-KET YOZISH
# Shartlarni yozishda bir nechta and va or operatorlarini aralashtirib ham yozish mumkin.
#kun=input("Bugun nima kun?>>> ")
#harorat=float(input("Harorat nechchi?>>> "))
#if (kun.lower()=="shanba" or kun.lower()=="yakshanba") and harorat>30:
#   print("Cho'milgani kettik") 
#elif (kun.lower()=="shanba" or kun.lower()=="yakshanba") and harorat<30:
#    print("Uyda dam olamiz")

# BOOLEAN MA'LUMOTLAR TURI
# Avvalgi darsimizda biz turli ifodalarni solishtirishda TRUE yoki FALSE qiymatlari qaytishini ko'rdik. Bu qiymatlar boolean (mantiqiy) qiymatlar deb ataladi, va dasturlashda juda keng qo'llaniladi. Pythonda o'zgaruvchilarda boolean qiymatlarni ham saqlash mumkin.
# Quyidagi dasturga e'tibor bering. Deylik, restoranimizga kelgan mijoz 15000 so'mlik taom oldi, biz mijoz qo'shimcha choy va salat ham olgan (olmaganiga) qarab ularning narhini ham yakuniy narhga qo'shishimiz kerak. Mijozning choy yoki salat olgan (olmaganini) biz TRUE va FALSE qiymatlari bilan belgiladik.
#narh=15000
#choy=True
#salat=False
#if choy and salat:
#    narh=narh+6000
#elif choy or salat:
#    narh=narh+3000
#print(f"Jami {narh} so'm")

# Boolean o'zgaruvchilarni saqlashda TRUE va FALSE qiymatlari o'rniga 1 va 0 sonlarini ham ishlatish mumkin.
#narh=15000
#choy=1
#salat=0
#if choy and salat:
#    narh=narh+6000
#elif choy or salat:
#    narh=narh+3000
#print(f"Jami {narh} so'm")

# SHARTLARNI KETMA-KET TEKSHIRISH
# if-elif-else zanjirining kamchiligidan biri, shartlardan biri bajarilishi bilan, qolgan shartlar tekshirilmaydi. Shung uchun ba'zida shartlarni ketma ket tekshirish uchun, har bir shartni alohida if bilan ajratish talab qilinishi mumkin.
#narh=15000
#choy=True
#salat=False
#non=True
#kompot=True
#assorti=False
#if choy:
#    print("Mijoz choy oldi.")
#    narh=narh+3000
#if salat:
#    print("Mijoz salat oldi.")
#    narh=narh+5000
#if non:
#    print("Mijoz non oldi.")
#    narh=narh+2000
#if kompot:
#    print("Mijoz kompot oldi.")
#    narh=narh+5000
#if assorti:
#    print("Mijoz assorti oldi.")
#    narh=narh+15000
#print(f"Jami {narh} so'm")

# Yuqoridagi dasturda har bir if alohida tekshiriladi va avvalgi yoki keyingi if ga bog'liq emas.

# RO'YXAT TARKIBINI TEKSHIRISH
# in OPERATORI
# in operatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini tekshirishimiz mumkin.
#menu=["osh","shashlik","norin","somsa","qotirma"]
#ovqat=input("Nima ovqat yeysiz?>>> ")
#if ovqat.lower() in menu:
#    print("Buyurtma qabul qilindi")
#else:
#    print("Bizda ushbu ovqat yo'q")

# not in OPERATORI
# not in operatori yordamida esa biror element ro'yxatda yo'qligini tekshirishimiz mumkin.
#menu=["osh","shashlik","norin","somsa","qotirma"]
#ovqat=input("Nima ovqat yeysiz?>>> ")
#if ovqat.lower() not in menu:
#    print("Bizda ushbu ovqat yo'q")
#else:
#    print("Buyurtma qabul qilindi")

# IKKI RO'YXATNI SOLISHTIRISH
# Ikki ro'yxatning tarkibi quyidagicha tekshiriladi:
    
#menu=["osh","shashlik","norin","somsa","qotirma"]
#buyurtma=["osh","manti","somsa","norin"]
#for taom in buyurtma:
#    if taom in menu:
#        print(f"Menuda {taom} bor")
#    else:
#        print(f"Afsuski bizda {taom} yo'q")

# RO'YXAT BO'SH EMASLIGINI TEKSHIRISH
# Yuqoridagi dasturimizda biz foydalanuvchi buyurtma berdi deb tasavvur qilyapmiz. Lekin foydalanuvchidan bo'sh ro'yxat kelsachi? Demak for tsiklini bajarishdan avval ro'yxat bo'sh emasligiga amin bo'lishimiz kerak. Buning uchun avvalgi kodimizni quyidagicha o'zgartiramiz:
#menu=["osh","shashlik","norin","somsa","qotirma"]
#buyurtma=["osh","manti","somsa","norin"]
#if buyurtma:
#    for taom in buyurtma:
#        if taom in menu:
#            print(f"Menuda {taom} bor")
#        else:
#            print(f"Afsuski bizda {taom} yo'q")
#else:
#    print("Savatchangiz bo'sh")

#menu=["osh","shashlik","norin","somsa","qotirma"]
#buyurtma=[]
#if buyurtma:
#    for taom in buyurtma:
#        if taom in menu:
#            print(f"Menuda {taom} bor")
#        else:
#            print(f"Afsuski bizda {taom} yo'q")
#else:
#    print("Savatchangiz bo'sh")

#AMALIYOT
#Quyidagi dasturlarni alohida fayllarga yozing va bajaring:

# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
#juft_son=float(input("Juft son kiriting:>>> "))
#if juft_son%2:
#    print("Bu juft son emas")
#else:
#    print("Rahmat")

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
#yosh=float(input("Yoshingiz nechida?>>> "))
#if yosh<=4 or yosh>=60:
#    print("Chipta bepul")
#elif yosh<=18:
#    print("Chipta 10000 so'm")
#else:
#    print("Chipta 20000 so'm")

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
#x=float(input("Birinchi sonni kiriting>>> "))
#y=float(input("Ikkinchi sonni kiriting>>> "))
#if x==y:
#    print("Sonlar teng")
#elif x>y:
#    print("Birinchi son katta")
#else:
#    print("Ikkinchi son katta")
   
# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
#mahsulotlar=["kola","fanta","shokolad","pepsi","guruch","kartoshka","piyoz","sabzi","go'sht","banan"]
#savat=[]
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni kiriting>>> "))
#for mahsulot in savat:
#    if mahsulot.lower() in mahsulotlar:
#        print(f"Do'konimizda {mahsulot} bor")
#    else:
#        print(f"Do'konimizda {mahsulot} yo'q")

#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
#mahsulotlar=["kola","fanta","shokolad","pepsi","guruch","kartoshka","piyoz","sabzi","go'sht","banan"]
#savat=[]
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni kiriting>>> "))
#mavjud_mahsulotlar=[]
#mavjud_emas=[]
#for mahsulot in savat:
#    if mahsulot.lower() in mahsulotlar:
#            mavjud_mahsulotlar.append(mahsulot)
#    else:
#            mavjud_emas.append(mahsulot)
#if mavjud_emas not in mahsulotlar:
#    print(f"Quyidagi mahsulotlar do'konimizda yo'q: {mavjud_emas}")
#else:
#    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")        

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
#foydalanuvchilar=["anvar","sadi","oleg","otash","muhammadrahim"]
#yangi_login=input("Yangi login kiriting:>>> ")
#if yangi_login.lower() in foydalanuvchilar:
#    print("Login band, yangi login tanlang")
#else:
#    print("Xush kelibsiz, foydalanuvchi")

#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
son=int(input("Biror butun son kiriting>>> "))
for n in range(2,11):
    if not (son%n) :
        print(f"{son} soni {n} soniga qoldiqsiz bo'linadi")
    






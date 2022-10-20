#08-dars, Ro'yhatlar bilan ishlash
#07/10/2022
#M.Rahimov

# RO'YXATNI TARTIBLASH
# Aksar holatlarda ro'yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash talab qilinishi mumkin. Buning uchun list uchun maxsus .sort() metodidan foydalanamiz.
#cars=['tahoe','trailblazer','equinox','malibu','tracker','gentra','cobalt','nexia3']
#print(cars)
#cars.sort()
#print(cars)

#Tartiblashda katta harflar kichik harflardan avval kelishini hisobga oling. Agar matndagi so'zlarning bosh harfi katta-kichik aralash yozilgan bo'lsa, ularni bir ko'rinishga keltirib olish maqsadga muvofiq bo'ladi.
#cars=['Tahoe','trailblazer','equinox','Malibu','tracker','Gentra','cobalt','nexia3']
#print(cars)
#cars.sort()
#print(cars)

# Ro'yxatni teskari tartibda saqlash uchun .sort() metodi ichida reverse=True argumentini ham kiritamiz.
#cars=['tahoe','trailblazer','equinox','malibu','tracker','gentra','cobalt','nexia3']
#print(cars)
#cars.sort(reverse=True)
#print(cars)

# .sort() metodi ro'yxatni tartiblaydi. Ba'zida asl ro'yxat ichidagi elementlarning ketma-ketligini buzmagan holda ro'yxatni tartiblash talab qilinishi mumkin. Buning uchun sorted() funktsiyasidan foydalanamiz:
#cars=['tahoe','trailblazer','equinox','malibu','tracker','gentra','cobalt','nexia3']
#print(sorted(cars))
#print(sorted(cars, reverse=True))
#sonlar=[12,5,93,55.2,-7,-15.2,500]
#print(sonlar)
#print(sorted(sonlar))
#print(sorted(sonlar,reverse=True))

# RO'YXATNING UZUNLIGINI BILISH
# Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun len() funktsiyasidan foydalanamiz
#cars=['tahoe','trailblazer','equinox','malibu','tracker','gentra','cobalt','nexia3']
#cars_number=len(cars)
#print("Mashinalar soni:",cars_number,"dona")

# range() FUNKTSIYASI
# Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. list() funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:
#sonlar=list(range(0,10))
#print(sonlar)
# Yuqoridagi misolda range(0,10) funktsiyasi 0 dan 9 gacha sonlar ketma-ketligini shakllantirdi, list(range(0,9)) esa bu ketma-ketlikni ro'yxatga aylantirdi.
# E'tibor qiling range() funktsiyasi ikkinchi indeksdan bitta avval to'xtaydi.

# range() yordamida qadamni ham berishimiz mumkin:
#toq_sonlar=list(range(1,21,2))
#print(toq_sonlar)
#juft_sonlar=list(range(2,21,2))
#print(juft_sonlar)
#sanash=list(range(0,101,10))
#print(sanash)

# Agar sonlar ketma-ketligi 0 dan boshlansa, range() funktsiyasida yakuniy indeksni ko'rsatish kifoya. Misol uchun range(0,10) emas range(10) deb yozsak ham bo'laveradi.
#print(list(range(30)))

# SONLI RO'YXAT USTIDA SODDA AMALLAR
# Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham bajarish mumkin. Misol uchun ro'yxatdagi eng kichik sonni topish uchun min() funktsiyasidan, eng katta sonni topish uchun esa max() funktsiyasidan, sonlarning yig'indisini topish uchun esa sum() funktsyasidan foydalansak bo'ladi:
    # min()
    # max()
    # sum()
#narhlar=[5000,4800,8500,15000,50000,23600]
#print(narhlar)
#arzon=min(narhlar)
#qimmat=max(narhlar)
#jami=sum(narhlar)
#print("Eng arzon narx:",arzon,", eng qimmat narx:",qimmat,", jami:",jami)

# RO'YXATNI KESISH
# Ba'zida ro'yxatning ma'lum bir bo'lagini ajratib olish talab qilinishi mumkin, deylik biz quyidagi cars degan ro'yxatdan birinchi 3 ta elementni ajratib olmoqchimiz, buning uchun biz boshlang'ich va oxirgi indekslarni beramiz:
#cars=['tahoe','trailblazer','equinox','malibu','tracker','gentra','cobalt','nexia3']
#my_cars=cars[0:3]
#print(my_cars)
#his_cars=cars[2:15]
#print(his_cars)
#her_cars=cars[:4]
#print(her_cars)
# Diqqat! Python 2-indeksdan bitta avval to'xtaydi. Yuqoridagi misolda ham 0,1,2-elementlar ajratib olindi.
# Bu usul bilan ro'yxatning istalgan joyidan bo'lishimiz mumkin:
# Agar boshlang'ich indeksni bermasangiz, Python avtomat ravishda 0 indeksdan boshlab kesadi. Agar 2-indeksni kiritmasangiz, ro'yxat oxirigacha kesadi:
    
# RO'YXATDAN NUSXA OLISH
#cars=['tahoe','trailblazer','equinox','malibu','tracker','gentra','cobalt','nexia3']
#my_cars=cars[:]
#my_cars[0]="spark"
#my_cars.remove('tracker')
#my_cars.append("bmw")
#print(cars)
#print(my_cars)

# TUPLES - O'ZGARMAS RO'YXAT
# Dastur yaratish davomida o'zgarmas ro'yxat tuzish talab qilinishi mumkin. Pythonda bunday ro'yxatlar tuples deb yuritiladi. Tuple ichidagi qiymatlarni bir marta, dastur boshida beriladi va so'ngra o'zgartirib bo'lmaydi. List dan farqli ravishda, Tuple e'lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:
#toys=('teddy','masha','bear','mashina','ball')
#print(toys)
#toys[3]='dragon'
#print(toys)
#toys.append('misha')
#print(toys)

# Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li o'zgarmas ro'yxatni list() funktsiyasi yordamida List (oddiy ro'yxat) ko'rinishiga keltirib olish, o'zgarishlarni bajarsih va qaytarib tuple() funktsiyasi yordamida o'zgarmas ro'yxatga o'tkazish mumkin:
#toys=list(toys)
#toys.append('misha')
#print(toys)
#toys=tuple(toys)
#print(toys)

# AMALIYOT
# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
#countries=['uzbekistan','england', 'russia','us','spain']
#print(countries)

# Ro'yxatning uzunligini konsolga chiqaring
#print(len(countries))

#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#print(sorted(countries))

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
#print(sorted(countries,reverse=True))

#Asl ro'yxatni qaytadan konsolga chiqaring
#print(countries)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
#countries.reverse()
#print(countries)

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring
#countries.sort()
#print(countries)
#countries.sort(reverse=True)
#print(countries)

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
#juft_son=list(range(120,1201,2))
#print(juft_son)

#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
#print(sum(juft_son))

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
#print(max(juft_son)-min(juft_son))

#Ro'yxatdagi elementlar sonini hisoblang
#print(len(juft_son))

#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
#boshi=juft_son[:20]
#oxiri=juft_son[-20:]
#ortasi=juft_son[261:281]
#print(boshi, '\n', oxiri, '\n',ortasi)

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
#taomlar=['osh','shashlik','baliq','qotirma','mastava']

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
#nonushta=taomlar[:]

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
#del nonushta[1]
#del nonushta[1]
#del nonushta[1]
#nonushta.append('shirguruch')
#nonushta.append('pitsa')

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
#print('Taomlar: ',taomlar, 'Nonushta uchun: ', nonushta)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
#nonushta=tuple(nonushta)
#nonushta[0] = "qaymoq va non"



#cars=['Tahoe','trailblazer','equinox','Malibu','tracker','Gentra','cobalt','nexia3']
#cars2=[]
#for car in cars:
#    cars2.append(car.lower())
#print(cars2)
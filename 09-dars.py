#09-dars, for takrorlash funksiyasi
#11/10/2022
#M.Rahimov

# Dasturlash davomida kodimizning biror qismini bir necha marta takrorlash talab etilishi mumkin. Misol uchun, ro'yxat ichidagi har bir elementni alohida qatordan konsolga chiqarish, yoki bo'lmasa har bir elementni kvdartaga oshirish va hokazo.
# Mana shunday vaziyatlarda bizga for operatori yordam beradi. Dasturlashda bu tsikl (loop) deb ataladi.

#mehmonlar=['Ali', 'Vali', 'Olim', 'Oleg', 'Islom']
#for mehmon in mehmonlar:
#    print('Salom', mehmon) 

# 1-qatorda biz mehmonlar degan ro'yxat yaratdik va uni mehmonlarning ismi bilan to'ldirdik.
# 2-qatorda for tsiklini bohladik. Bu qator Pythonga mehmonlar degan ro'yxatdan har bir elementini olib uni yangi, mehmon degan o'zgaruvchiga yuklashni buyuryapti (o'zgaruvchiga istalgan nom berishingiz mumkin. Biz tushunarli bo'lishi uchun mehmon deb atadik)
# 3-qatorda biz mehmon degan o'zgaruvchining qiymatini konsolga chiqardik. Bu tsikl to mehmonlar ro'yxatida elementlar tugagunga qadar takrorlanadi.
# Yuqoridagi kodni oddiy tilga tarjima qilsak "Mehmonlar ro'yxatidagi har bir mehmon uchun uning ismini konsolga chiqar" degan ma'noni beradi.

#mehmonlar=['Ali', 'Vali', 'Olim', 'Oleg', 'Islom']
#for mehmon in mehmonlar:
#    print('Salom', mehmon) 
#    print('Hayr', mehmon)

# Quyidagi kodda 2-qator bu tsikl boshi deyiladi. Aynan shu qator kodimiz nech marta takrorlanishini aniqlaydi. Bizning holatimizda tsikl mehmonlar ro'yxati ichidagi elementlar tugagunga qadar takrorlanadi. Tsikl boshlanishi ikki nuqta (:) bilan tugaydi. Undan keyingi 3 va 4-qatorlar bu tsiklning badani deyiladi.
# Tsikl badani surilish (indentation) bilan ajratiladi, ya'ni tsiklning takrorlanuvchi qismi asosiy koddan bir muncha o'ngroqqa surilgan bo'ladi. Agar biz mana shu surilishni tark qilsak kodimiz xato beradi:
    
#mehmonlar=['Ali', 'Vali', 'Olim', 'Oleg', 'Islom']
#for mehmon in mehmonlar:
#    print('Hurmatli', mehmon, 'sizni 11 oktyabr kuni nahorgi oshga taklif qilamiz')
#    print('Hurmat bilan Rahimovlar oilasi')

#mehmonlar=['Ali', 'Vali', 'Olim', 'Oleg', 'Islom']
#for mehmon in mehmonlar:
#    print('Hurmatli', mehmon, 'sizni 11 oktyabr kuni nahorgi oshga taklif qilamiz')
#print('Hurmat bilan Rahimovlar oilasi')

# for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH
#sonlar=list(range(1,11))
#for son in sonlar:
#    print(son, 'ning kvadrati', son**2, 'ga teng')
    
# for yordamida yangi ro'yxat ham shakllantirish mumkin:
#sonlar=list(range(1,11))
#sonlar_kvadrati=[]
#for son in sonlar:
#    sonlar_kvadrati.append(son**2)
#print(sonlar)   
#print(sonlar_kvadrati)

# for va input()
# for operatori va input() funktsiyasini jamlab, ro'yxatni foydalanuvchidan olingan qiymatlar bilan to'ldirish mumkin:

#dostlar = []
#print("Eng yaqin 5 ta do'stingiz kim?")
#for n in range(5):
#    dostlar.append(input(f"{n+1}-do'stingiz ismini kiriting: "))
#print(dostlar)

# AMALIYOT

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
#ismlar=['Ilhom', "Firdavs","Islom","Abdulbori", "Akram"]
#for ism in ismlar:
#    print("Milanoga dotaga borasanmi,",ism,"?")
    
#Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
#print("Kod", len(ismlar), "marta takrorlandi")

#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
#toq_son=list(range(11,100,2))
#kubi=[]
#for n in toq_son:
#    kubi.append(n**3)
#print(toq_son)
#print(kubi)

#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
#print("5 ta eng yoqtirgan kinolaringiz qaysilar?")
#kinolar=[]
#for n in range(5):
#    kinolar.append(input(f"{n+1}-yoqtirgan kino nomini kiriting: "))
#print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
odam_soni=int(input("Bugun nechta odam bilan suhbatlashdingiz? "))
print("Bugun nechta odam bilan suxbatlashdingiz?")
odamlar=[]
for n in range(odam_soni):
    odamlar.append(input(f"{n+1}-suxbatlashgan odam ismini kiriting: "))
print(odamlar)

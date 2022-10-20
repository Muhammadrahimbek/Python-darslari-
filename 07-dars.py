#07-dars, List/Ro'yhat
#06/10/2022
#M.Rahimov

# Bugun o'rganadigan navbatdagi mal'umot turi List (ro'yxat) deb ataladi. Ro'yxat o'z nomi bilan, bitta o'zgaruvchida bir nechta qiymatlarni saqlash imkonini beradi. Bu qiymatlar List elementlari deyiladi. Ro'yxatda son, matn yoki aralash turdagi elementlarni saqlash mumkin
# List quyidagicha yaratiladi:
# So'zlar ro'yhat qilinsa bo'ladi
#fruits=['apple', 'banan', 'grape', 'limon', 'melon']
# Raqamlar ro'yhat qilinsa bo'ladi
#prices=[10000,21000,5000,30000,4000]
# Aralash ro'yhat qilinsa bo'ladi, yani raqam+so'z
#sonlar=['bir', 'ikki',3,4,5]
# Mutlaqo bo'm bo'sh ro'yhat tuzsa ham bo'ladi
#cars=[]

# LIST ELEMENTLARI
# Ro'yxatdagi har bir element tartib bilan joylashgani sababli, biz istalgan elementga uning tartib raqami (indeksi) bo'yicha murojat qilishimiz mumkin.
# Dasturlash olamida indeks 0 dan boshlanadi! Ya'ni Listning birinchi elementing tartib raqami (indeksi) 0 ga, ikkinchi elementning indeksi 1 ga teng va hokazo.
#fruits=['apple', 'banan', 'grape', 'limon', 'melon']
#print("Birinchi meva: ",fruits[0])
#print("Uchinchi meva: ",fruits[2])

# Pythonda Listning eng oxirgi elementiga -1 indeksi orqali ham murojat qilish mumkin. Bu usul Listning uzunligini bilmaganda juda asqotadi.Orqadan sanash xisoblanadi. -2 oxiridan ikkinchi degani
#fruits=['apple', 'banan', 'grape', 'limon', 'melon']
#print("Oxirgi meva: ",fruits[-1])
#print("Oxirgi oldingi meva: ",fruits[-2])

# Agar list ichidagi elementlar matn ko'rinishid bo'lsa, ularga string metodlarni qo'llashimiz mumkin:
#fruits=['apple', 'banan', 'grape', 'limon', 'melon']
#print(fruits[0].upper())
#print(fruits[1].title())

# List elementlari ustida arifmetik amallar bajarish:
#prices=[10000,21000,5000,30000,4000]
#print(prices[0]+prices[2])

# ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH
# Dastur davomida listning tarkibi o'zgarishi, yangi elementlar qo'shilishi, ba'zi elementlar o'chirilishi tabiiy hol. Misol uchun "Bozorlik ro'yxati" degan dasturni tasavvur qilaylik, foydalanuvchi ro'yxatga yangi mahsulotlar qo'shishi, sotib olganlarini esa o'chrishi mumkin.

# Elementni o'zgartirish
# Ro'yxatdagi biror elementning qiymatini o'zgartirish uchun, o'sha elementga indeksi bo'yicha murojat qilamiz va yangi qiymat yuklaymiz
#fruits=['apple', 'banan', 'grape', 'limon', 'melon']
#prices=[10000,21000,5000,30000,4000]
#prices[0]=12000
#prices[4]=prices[4]+2000
#fruits[1]='peach'

# Yangi element qo'shish
# .append() metodi
# Ro'yxatga yangi element qo'shishning oson usuli bu .append() metodi yordamida ro'yxatning oxiriga qiymat qo'shish:
#fruits=['apple', 'banan', 'grape', 'limon', 'melon']
#fruits.append('peach')
#print(fruits)
#fruits.append('mango')
#print(fruits)

# .insert() metodi
# Ro'yxatning istalgan joyiga yangi element qo'shish uchun .insert() metodidan foydalanamiz. .insert() metodi ichida yangi elementning indeksi va qiymati beriladi:
#fruits=['apple', 'banan', 'grape', 'limon', 'melon']
#print(fruits)
#fruits.insert(1, 'peach')
#print(fruits)
#fruits.insert(1, 'peach'.upper())
#print(fruits)

# Elementni o'chirish
# Ro'yxatdan biror elementni olib tashlash uchun uning indeksini yoki qiymatini bilishimiz lozim.
# Indeks yordamida olib tashlash uchun del operatoridan foydalanamiz:
#cars=[]
#cars.append('Nexia')
#cars.append('Malibu')
#cars.append('Gentra')
#cars.append('Spark')
#cars.append('Damas')
#print(cars)
#del cars[0]
#print(cars)
#cars.insert(0,'Nexia 3')
#print(cars)
#del cars[3]
#print(cars)

# Element qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan foydalanamiz. Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan qiymatni yozamiz
#print(cars)
#cars.remove('Spark')
#print(cars)

# .remove(qiymat) metodi ro'yxatda uchragan birinchi mos keluvchi qiymatni o'chiradi. Agar ro'yxatning ichida 2 va undan ko'p bir hil qiymatli elementlar bo'lsa, ulardan eng birinchisi o'chadi.
#fruits=['apple', 'banan', 'grape', 'limon', 'melon', 'banan']
#print(fruits)
#fruits.remove('banan')
#print(fruits)
# Agar hamma 'banan'ni o'chirishni xoxlasak 'remove' metodidan qayta qayta foydalanamiz. Ro'yhatda tugasa o'zi oshibka beradi

# Elementni sug'urib olish
# Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni ro'yxatdan sug'urib olish va undan foydalanish talab qilinishi mumkin. Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz.
#bozorlik=["yog'", "un", "go'sht", "guruch", "meva"]
#print(bozorlik)
#mahsulot=bozorlik.pop(3)
#print(mahsulot)
#print(bozorlik)
#print('Men '+mahsulot+' sotib oldim')
#print('Sotib olinmagan mahsulotlar: ', bozorlik)

# Agar .pop() metodida indeks berilmasa, ro'yxatdan o'xirgi qiymat sug'urib olinadi.
#bozorlik=["yog'", "un", "go'sht", "guruch", "meva"]
#mahsulot=bozorlik.pop()
#print(bozorlik)

# AMALIYOT
# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
#ismlar=['Ilhom', 'Abdulbori', 'Isomiddin']
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
#print('Salom '+ismlar[0]+" bugun Momiq bilan ko'rishamizmi.")
#print("Salom " + ismlar[1] + " bugun Milanoga o'tamizmi.")
#print("Yig'ilishga bora olmadim, xafa bo'lmadingizmi "+ismlar[2]+"?")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik)
#sonlar=[12,-5,93,36.6]
#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
#print(sonlar)
#print(sonlar[0]+sonlar[2])
#print(sonlar[3]/sonlar[1])
#sonlar[0]=sonlar[0]+10
#sonlar[1]=55
#print(sonlar)

# t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
#t_shaxslar=["Islom Karimov", "Amir Temur", "Imom Buxoriy", "Shayx Muhammadsodiq Muhammadyusuf"]
#z_shaxslar=["Sh.Mirziyoyev", "V.Putin", "Muftiy Nuriddin domla", "Solixon domla"]
#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
#t_shaxs=t_shaxslar.pop(2)
#z_shaxs=z_shaxslar.pop(3)
#print("Men tarixiy shaxslardan "+t_shaxs+" bilan, zamonaviy shaxslardan esa "+z_shaxs+" bilan suxbat qilishni istar edim")

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends=[]
friends.append("Ilhom")
friends.append("Akram")
friends.append("Abdulbori")
friends.append("Isomiddin")
friends.append("Ravshan")
friends.append("Mansur")
#print(friends)

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
#friends.remove("Mansur")
#print(friends)

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
#print(friends)
friends.append("Ismatillo")
friends.insert(0, "Firdavs")
friends.insert(3, "Islom")
#print(friends)

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar=[]
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(-1))
print("Yangi mehmonlar: ",mehmonlar)















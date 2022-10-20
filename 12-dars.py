#12-dars, XATOLAR BILAN ISHLASH
#19/10/2022
#M.Rahimov

# SyntaxError - SINTEKS XATOLIK
# Biz syntax error bilan 3-darsimizda tanishgan edik. Bu eng ko'p uchraydigan xato bo'lib, odatda dasturlash tili qoidalariga amal qilmaslik natijasida kelib chiqadi. Aksar dasturlash muhitlari sintaks xatolikni dastur bajarilishidan avvaloq aniqlab, dasturchiga ishora beradi. Sintaks xatolik bor dasturni Python bajarmaydi.

# EOL va EOF xatolik
# EOL (End of Line - qator yakuni) xatoligi sintaks xatolikning bir turi bo'lib, odatda qator oxirida qo'shtirnoq (birtirnoq) ni yopish esdan chiqqanda yuzaga keladi.
# EOF (End of function - funktsiya yakuni) xatoligi esa funktsiya oxirida qavsni yopish esdan chiqqanda yuzaga keladi.

# IndentationError - JOY TASHLASHDA XATOLIK
# Python tilida qator boshidan yoki joy tashlab yozish muhim ahamiyatga ega. Qator boshidan asossiz joy qoldirish IndentationError ga olib keladi.

# RUN TIME ERROR - DASTURNI BAJARISHDA XATOLIK
# Run time error — dastur bajarish jarayonida kelib chiqadi va dasturning ishlashini to'xtatadi. Sintaks xatolikdan farqli ravishda Python bunday xatolarni dasturni bajarishdan avval aniqlay olmaydi. Run time error ning bir necha turi bor. Keling, ulardan ba'zilari bilan tanishamiz.

# TypeError
# Biror amalni (funktsiya, metod) noto'g'ri ma'lumot turi ustida bajarish.

# NameError
# O'zgaruvchi, funktsiya, obyekt nomini noto'g'ri yozish natijasida kelib chiquvchi xatolik.

#ValueError
# Funktsiyaga noto'g'ri qiymatni yuborish natijasidagi xatolik

# IndexError
# Yangi dasturchilar yo'l qo'yadigan yana bir xato bu indeks xatolik. Ya'ni ro'yxat elementlariga murojat qilishda indeksni noto'g'ri kiritish.

# ZeroDivisionError
# Dastur jarayonida 0 ga bo'lish yuzaga kelgandagi xatolik

# MANTIQIY XATOLAR
# Mantiqiy xatolar - dasturchi tomonidan yo'l qo'yilgan va kutilgan natijani berishda to'sqinlik qiluvchi xatolar. Bunday xatolar eng ko'p uchraydigan va aniqlash eng qiyin bo'lgan xatolar hisoblanadi. Aksar holatlarda Python mantiqiy xatolarni aniqlamaydi va dastur bajarilaveradi (lekin kutilgan natija chiqmaydi).

# AMALIYOT
# Quyida bir nechta kodlar berilgan, kodlar avvalgi darsdagi uy vazifalaridan iborat. Kodlardagi xatolarni toping va to'g'rilang. Har bir dasturda bir nechta xatolar mavjud bo'lishi mumkin. Xatolarni topish uchun dasturlarni bir necha marta, turli qiymatlar bilan bajarib ko'ring.

#son=float(input("Juft son kiriting: "))
#if son%2!=0:
#    print("Bu son juft emas.")
#else:
#    print("Rahmat!")

#yosh = float(input("Yoshingiz nechida? "))
#if yosh<=4 or yosh>=60:
#    narh = 0
#elif yosh<18:
#    narh = 10000
#else:
#    narh = 20000
#print(f"Chipta {narh} so'm")

#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))
#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f"{x}<{y}")
#else:
#    print(f"{x}>{y}")

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#savat=[]
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#if savat:
#    for mahsulot in savat:
#        if mahsulot in mahsulotlar:
#            print(f"Do'konimizda {mahsulot} bor")
#        else:
#            print(f"Do'konimizda {mahsulot} yo'q")
#else: 
#            print("Savatingiz bo'sh")            

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
#    if mahsulot.lower() in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
#        mavjud_emas.append(mahsulot)

#if mavjud_emas:
#    print("Do'konimizda quyidagi mahsulotlar yo'q:")
#    for mahsulot in mavjud_emas:
#        print(mahsulot)
#else:
#    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
#users = ['alisher1983','aziza','yasina' 'umar']
#login = input('Yangi login tanlang: ')

#if login.lower() in users:
#    print('Login band, yangi login tanlang!')
#else:
#    print("Xush kelibsiz!")
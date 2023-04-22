age = input("Qual e' la tua eta'?")

int_age = int(age)

if int_age <3:
    print("A questa eta' non si va a scuola (di solito)")
elif int_age >= 3 and int_age <=5:
    print("A questa eta' si va alla scuola materna")
elif int_age > 5 and int_age < 11:
    print("A questa eta' si va alla scuola elementare")
elif int_age >= 11 and int_age <= 14:
    print("A questa eta' si va alla scuola media")
elif int_age > 14 and int_age <= 19:
    print("A questa eta' si va alle scuole superiori")
else:
    print("""A questa eta' si puo' andare all'universita',
o andare a lavorare o farsi mantenere dai genitori
fino a quando non ti buttano fuori di casa""")

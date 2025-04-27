nota= float(input("Introduce la nota del alumno: "))

if nota >= 9 and nota <= 10:
    print("La nota es A")
elif nota >= 8 and nota <= 9:
    print("La nota es B")
elif nota >= 7 and nota <= 8:
    print("La nota es C") 
elif nota >= 5 and nota <= 6:
    print("La nota es D")
elif nota >= 3 and nota <= 4:
    print("La nota es F")
else: 
    print("La nota es E")
        
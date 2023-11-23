
ievaditais_skaitlis = int(input("Ievadiet skaitli: "))
faktorials = 1
for skaitlis in range(1, ievaditais_skaitlis + 1):
    faktorials *= skaitlis
print("Faktoriāls no", ievaditais_skaitlis, "ir:", faktorials)

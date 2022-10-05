x = int(input("1º codernada: "))
y = int(input("2º codernada: "))

if x > 0 and y > 0:
    print("Primeiro\n")
elif x < 0 and y > 0:
    print("Segundo\n")
elif x < 0 and y < 0:
    print("Terceiro\n")
elif x > 0 and y < 0:
    print("Quarto\n")
else:
    print("")

while x != 0 and y != 0:
    x = int(input("1º codernada: "))
    y = int(input("2º codernada: "))

    if x > 0 and y > 0:
        print("Primeiro\n")
    elif x < 0 and y > 0:
        print("Segundo\n")
    elif x < 0 and y < 0:
        print("Terceiro\n")
    elif x > 0 and y < 0:
        print("Quarto\n")
    else:
        print("")

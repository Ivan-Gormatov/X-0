def ins_pole(inspole):
    print("  0 1 2")
    for ii in range(0, 3):
        print(f"{ii:<2}" + " ".join(inspole[(ii * 3):(ii * 3 + 3)]))


def vvod(vvodpole):
    while True:
        try:
            v, h = [int(s) for s in
                    (input("ВВедите позицию хода через пробел (По вертикали  по горизонтаали): ").split())]

        except ValueError:
            print("Ввод неверен. Введите две координаты через пробел.")
        else:
            if 0 > v or v > 2 or 0 > h or h > 2:
                print("Ввод за пределы поля. Повторите ввод")
            elif vvodpole[v * 3 + h] != "-":
                print("Клетка занята. Повторите ввод")
            else:
                return v, h


def win(winpole, player):
    return any([winpole[0] == winpole[1] == winpole[2] == player,
                winpole[3] == winpole[4] == winpole[5] == player,
                winpole[6] == winpole[7] == winpole[8] == player,
                winpole[0] == winpole[3] == winpole[6] == player,
                winpole[1] == winpole[4] == winpole[7] == player,
                winpole[2] == winpole[5] == winpole[8] == player,
                winpole[0] == winpole[4] == winpole[8] == player,
                winpole[2] == winpole[4] == winpole[6] == player])


yes = "y"
while yes == "y" or yes =="Y":
    pole = ['-'] * 9
    N = "Ничья"
    for i in range(9):
        if i % 2 == 1:
            igrok = "o"
        else:
            igrok = "x"
        ins_pole(pole)
        print("Ходят: " + igrok)
        poleV, poleH = vvod(pole)
        pole[poleV * 3 + poleH] = igrok
        if win(pole, igrok):
            N = "Победили  " + igrok
            break
    ins_pole(pole)
    print("Игра закончена: " + N)
    yes = input("Еще одну игру (y/n): ")

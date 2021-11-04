pyramidHeight = int(input("Высота пирамиды: "))
row = ""
count = 1
spacing = 0
star = 0
u = 0
while (count <= pyramidHeight):
    spacing = spacing + count
    while (spacing < pyramidHeight):
        row += " "
        spacing += 1
    star = count + u
    while (star > 0):
        row += "*"
        star -= 1
    count += 1
    spacing = 0
    u += 1
    print(row)
    row *= -1

import turtle
sc = turtle.Screen()
sc.setup(500, 500)

base_of_number = int(turtle.textinput("NumberSys. Convertor", "Enter Base Value(2/8/10):"))
number = number_input =  int(turtle.textinput("NumberSys. Converter", "Enter numeric value:"))
rem = 0
decimal = binary = octal = hexadecimal = ''
number_string = str(number)
l, a = len(number_string), 0

if base_of_number == 10:  # Decimal Input
    decimal = number
    while True:  # to Binary
        rem = number % 2
        number //= 2
        binary += str(rem)
        if number == 0:
            rem, number = 0, number_input
            break
    while True:  # to Octal
        rem = number % 8
        number //= 8
        octal += str(rem)
        if number == 0:
            rem, number = 0, number_input
            break
    while True:  # to Hexadecimal
        rem = number % 16
        number //= 16
        if rem < 10:
            hexadecimal += str(rem)
        else:
            rem -= 10
            hexadecimal += chr(ord('A') + rem)
        if number == 0:
            break
    binary = binary[::-1]
    octal = octal[::-1]
    hexadecimal = hexadecimal[::-1]

elif base_of_number == 2:  # Binary Input
    binary = number

    for i in range(l):  # to Decimal
        rem += int(number_string[i]) * (2 ** (l - i - 1))
    decimal, rem = rem, ''

    if l % 3 == 0:  # to Octal
        a = 0
    else:
        a = 3 - (l % 3)
    number, a = ('0' * a) + number_string, 0
    z = len(number)
    for j in range(z // 3):
        for k in range(0, 3):
            a += int(number[k]) * (2 ** (2 - k))
        rem += str(a)
        a = 0
        number = number[3:]
    octal, rem = rem, ''

    if l % 4 == 0:  # to Hexadecimal
        a = 0
    else:
        a = 4 - (l % 4)
    number, a = ('0' * a) + number_string, 0
    z = len(number)
    for j in range(z // 4):
        for k in range(0, 4):
            a += int(number[k]) * (2 ** (3 - k))
        if a < 10:
            rem += str(a)
        else:
            a -= 10
            rem += chr(ord('A') + a)
        number = number[4:]
        a = 0
    hexadecimal, rem = rem, 0

elif base_of_number == 8:  # Octal Input
    octal = number
    for i in range(l):  # to Decimal
        rem += int(number_string[i]) * (8 ** (l - i - 1))
    decimal, rem = rem, ''

    for i in range(l):  # to Binary
        if int(number_string[i]) % 2 == 0:
            last = '0'
            number = int(number_string[i])
        else:
            last = '1'
            number = int(number_string[i]) - 1
        for x in range(2):
            for y in range(2):
                if 4 * x + 2 * y == number:
                    m = str(y)
                    s = str(x)
        rem = rem + s + m + last
    binary, rem = rem, ''

    for i in range(l):  # to Hexadecimal
        if int(number_string[i]) % 2 == 0:
            last = '0'
            number = int(number_string[i])
        else:
            last = '1'
            number = int(number_string[i]) - 1
        for x in range(2):
            for y in range(2):
                if 4 * x + 2 * y == number:
                    m = str(y)
                    s = str(x)
        rem = rem + s + m + last
    number = rem
    l = len(number)
    if l % 4 == 0:
        a = 0
    else:
        a = 4 - (l % 4)
    number, rem, a = ('0' * a) + rem, '', 0
    z = len(number)
    for j in range(z // 4):
        for k in range(0, 4):
            a += int(number[k]) * (2 ** (3 - k))
        if a < 10:
            rem += str(a)
        else:
            a -= 10
            rem += chr(ord('A') + a)
        number = number[4:]
        a = 0
    hexadecimal = rem

else:
    decimal = "enter valid values"
    binary = "enter valid values"
    octal = "enter valid values"
    hexadecimal = "enter valid values"

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(height=600, width=800)
result = turtle.Turtle()
result.speed(0)
result.shape("square")
result.shapesize(stretch_len=38, stretch_wid=10)
result.penup()
result.goto(x=-2, y=50)
result.color("Sienna", "black")
result = turtle.Turtle()
result.speed(0)
result.shape("square")
result.shapesize(stretch_len=38, stretch_wid=2)
result.penup()
result.goto(x=-2, y=180)
result.color("lightcyan")

pen_da = turtle.Turtle()
pen_da.speed(0)
pen_da.color("white")
pen_da.penup()
pen_da.hideturtle()
pen_da.goto(0, 215)
pen_da.write("NUMBER SYSTEM CONVERTOR", align="center", font=("Stencil Std", 35, "normal"))
pen_da.color("SandyBrown")
pen_da.goto(0, 165)
pen_da.write("Computer Science Project", align="center", font=("Orbitron", 20, "normal"))
pen_da.color("PaleTurquoise")
pen_da.goto(0, 110)
pen_da.write("Guided by:", align="center", font=("Orbitron", 16, "normal"))
pen_da.goto(0, 75)
pen_da.write("M/s. Sushma Singh Chouhan", align="center", font=("Orbitron", 16, "normal"))
pen_da.goto(0, 40)
pen_da.write("Done by:", align="center", font=("Orbitron", 16, "normal"))
pen_da.goto(0, 5)
pen_da.write("Vedant Garg", align="center", font=("Orbitron", 16, "normal"))
pen_da.goto(0, -30)
pen_da.write("Vinayak Powar", align="center", font=("Orbitron", 16, "normal"))

pen_da.goto(-130, -120)
pen_da.write("Decimal:", align="center", font=("Bowlby One SC", 18, "normal"))
pen_da.goto(120, -111)
pen_da.write(decimal, align="center", font=("Bahnschrift Light", 15, "bold"))

pen_da.goto(-135, -160)
pen_da.write("Binary:", align="center", font=("Bowlby One SC", 18, "normal"))
pen_da.goto(120, -151)
pen_da.write(binary, align="center", font=("Bahnschrift Light", 15, "bold"))

pen_da.goto(-140, -200)
pen_da.write("Octal:", align="center", font=("Bowlby One SC", 18, "normal"))
pen_da.goto(120, -191)
pen_da.write(octal, align="center", font=("Bahnschrift Light", 15, "bold"))

pen_da.goto(-100, -240)
pen_da.write("Hexadecimal:", align="center", font=("Bowlby One SC", 18, "normal"))
pen_da.goto(120, -231)
pen_da.write(hexadecimal, align="center", font=("Bahnschrift Light", 15, "bold"))
turtle.done()

from random import randint

a = 0

print("Running...")
for x in range(1, 11):
    i = 0
    a = 0

    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0

    print("Running #" + str(x))
    for i in range(100000000):
        a += 1
        if "0" in str(a):
            print(a)
        val = randint(1, 10)

        if val == 1:
            one += 1
        elif val == 2:
            two += 1
        elif val == 3:
            three += 1
        elif val == 4:
            four += 1
        elif val == 5:
            five += 1
        elif val == 6:
            six += 1
        elif val == 7:
            seven += 1
        elif val == 8:
            eight += 1
        elif val == 9:
            nine += 1
        elif val == 10:
            ten += 1

    filename = "data" + str(x) + ".txt"
    f = open(filename, "w")

    f.write("1: " + str(one) + "\n")
    f.write("2: " + str(two) + "\n")
    f.write("3: " + str(three) + "\n")
    f.write("4: " + str(four) + "\n")
    f.write("5: " + str(five) + "\n")
    f.write("6: " + str(six) + "\n")
    f.write("7: " + str(seven) + "\n")
    f.write("8: " + str(eight) + "\n")
    f.write("9: " + str(nine) + "\n")
    f.write("10: " + str(ten))

    print("Wrote to " + filename + "!")

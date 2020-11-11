file = open("./../Dane_PR2/statek.txt")
text = file.read()
lines = text.split("\n")
lines.remove("")
lines.remove("data	port	towar	Z/W	ile ton	cena za tone w talarach")


def first():
    towar = [0, 0, 0, 0, 0]
    biggest = 0
    name = 0
    for index in range(len(lines)):
        line = lines[index]
        data = line.split("\t")
        if data[3] == "Z":
            if data[2] == 'T1':
                towar[0] += 1
            if data[2] == 'T2':
                towar[1] += 1
            if data[2] == 'T3':
                towar[2] += 1
            if data[2] == 'T4':
                towar[3] += 1
            if data[2] == 'T5':
                towar[4] += 1
    for index in range(len(towar)):
        if towar[index] > biggest:
            biggest = towar[index]
            name = index + 1
    print("6.1: ",str(biggest) + " T" + str(name))


def second():
    num = 0
    for index in range(len(lines) - 1):
        date1 = lines[index].split("\t")[0].split("-")
        date2 = lines[index + 1].split("\t")[0].split("-")
        if date1[0] == date2[0] and date1[1] == date2[1]:
            if int(date2[2]) - int(date1[2]) > 0:
                num += 1
        elif date1[0] == date2[0]:
            if int(date1[1]) == 2:
                if 28 - int(date1[2]) + int(date2[2]) > 20:
                    num += 1
            if int(date1[1]) < 8:
                if int(date1[1]) % 2 == 1:
                    if 31 - int(date1[2]) + int(date2[2]) > 20:
                        num += 1
                if int(date1[1]) % 2 == 0:
                    if 30 - int(date1[2]) + int(date2[2]) > 20:
                        num += 1
            if int(date1[1]) >= 8:
                if int(date1[1]) % 2 == 1:
                    if 30 - int(date1[2]) + int(date2[2]) > 20:
                        num += 1
                if int(date1[1]) % 2 == 0:
                    if 31 - int(date1[2]) + int(date2[2]) > 20:
                        num += 1
        else:
            if 31 - int(date1[2]) + int(date2[2]) > 20:
                num += 1
    print("6.2: ",num)


def count_to_date(date):
    towar = [0, 0, 0, 0, 0]
    biggest = 0
    b_name = 0
    smallest = float("inf")
    s_name = 0
    for line in lines:
        data = line.split("\t")
        if data[0] == date:
            break
        if data[3] == "Z":
            if data[2] == 'T1':
                towar[0] += int(data[4])
            if data[2] == 'T2':
                towar[1] += int(data[4])
            if data[2] == 'T3':
                towar[2] += int(data[4])
            if data[2] == 'T4':
                towar[3] += int(data[4])
            if data[2] == 'T5':
                towar[4] += int(data[4])
        if data[3] == "W":
            if data[2] == 'T1':
                towar[0] -= int(data[4])
            if data[2] == 'T2':
                towar[1] -= int(data[4])
            if data[2] == 'T3':
                towar[2] -= int(data[4])
            if data[2] == 'T4':
                towar[3] -= int(data[4])
            if data[2] == 'T5':
                towar[4] -= int(data[4])
    for index in range(len(towar)):
        if towar[index] > biggest:
            biggest = towar[index]
            b_name = index + 1
        if smallest > towar[index] > 0:
            smallest = towar[index]
            s_name = index + 1
    print("Biggest for ",date," is T" + str(b_name), "(", biggest,")")
    print("Smallest for ", date, " is T" + str(s_name), "(", smallest, ")")


def third():
    print("6.3:")
    count_to_date("2016-02-19")
    count_to_date("2018-08-05")

first()
second()
third()

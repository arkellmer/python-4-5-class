NUM128 = 128
NUM64 = 64
NUM32 = 32
NUM16 = 16
NUM8 = 8
NUM4 = 4
NUM2 = 2
NUM1 = 1


day_set1 = "set 1: "
day_set2 = "set 2: "
day_set4 = "set 3: "
day_set8 = "set 4: "
day_set16 = "set 5: "

m_set1 = "set 1: "
m_set2 = "set 2: "
m_set4 = "set 3: "
m_set8 = "set 4: "

y_set1 = "set 1: "
y_set2 = "set 2: "
y_set4 = "set 3: "
y_set8 = "set 4: "

whats_left = 0

for i in range(1,32):
    bi_num = ""
    input_num = i
    whats_left = input_num

    if input_num >= NUM128:
        whats_left = input_num - NUM128
        bi_num += "1"
    else:
        bi_num += "0"

    if whats_left >= NUM64:
        whats_left -= NUM64
        bi_num += "1"
    else:
        bi_num += "0"

    if whats_left >= NUM32:
        whats_left -= NUM32
        bi_num += "1"
    else:
        bi_num += "0"

    if whats_left >= NUM16:
        whats_left -= NUM16
        bi_num += "1"
    else:
        bi_num += "0"

    if whats_left >= NUM8:
        whats_left -= NUM8
        bi_num += "1"
    else:
        bi_num += "0"

    if whats_left >= NUM4:
        whats_left -= NUM4
        bi_num += "1"
    else:
        bi_num += "0"

    if whats_left >= NUM2:
        whats_left -= NUM2
        bi_num += "1"
    else:
        bi_num += "0"

    if whats_left >= NUM1:
        whats_left -= NUM1
        bi_num += "1"
    else:
        bi_num += "0"

    xnum7 =bi_num[7]
    xnum6 =bi_num[6]
    xnum5 =bi_num[5]
    xnum4 =bi_num[4]
    xnum3 =bi_num[3]
    xnum2 =bi_num[2]
    xnum1 =bi_num[1]
    xnum0 =bi_num[0]
    

    

    x = str(i)
    if xnum3 == "1":
        day_set16 += x+" "
    if xnum4 == "1":
        day_set8 += x+" "
    if xnum5 == "1":
        day_set4 += x+" "
    if xnum6 == "1":
        day_set2 += x+" "
    if xnum7 == "1":
        day_set1 += x+" "
        
    if i<=12:
        if xnum4 == "1":
            m_set8 += x+" "
        if xnum5 == "1":
            m_set4 += x+" "
        if xnum6 == "1":
            m_set2 += x+" "
        if xnum7 == "1":
            m_set1 += x+" "

    if i<=15:
        if xnum4 == "1":
            y_set8 += x+" "
        if xnum5 == "1":
            y_set4 += x+" "
        if xnum6 == "1":
            y_set2 += x+" "
        if xnum7 == "1":
            y_set1 += x+" "
##    input("press enter to add the next number")
##    print(day_set1)
##    print(day_set2)
##    print(day_set4)
##    print(day_set8)
##    print(day_set16)

birthday = 0
print(day_set1)
x = input("is your birthday in this list?")
if x == "yes" or x == "y":
    birthday +=1
print("\n")
    
print(day_set2)
x = input("is your birthday in this list?")
if x == "yes" or x == "y":
    birthday +=2
print("\n")
    
print(day_set4)
x = input("is your birthday in this list?")
if x == "yes" or x == "y":
    birthday +=4
print("\n")
    
print(day_set8)
x = input("is your birthday in this list?")
if x == "yes" or x == "y":
    birthday +=8
print("\n")

print(day_set16)
x = input("is your birthday in this list?")
if x == "yes" or x == "y":
    birthday +=16
print("\n")

print("your birthday is", birthday)
print("\n")
#month starts here

month = 0

print(m_set1)
x = input("is your birthday month in this list?")
if x == "yes" or x == "y":
    month += 1
print("\n")

print(m_set2)
x = input("is your birthday month in this list?")
if x == "yes" or x == "y":
    month += 2
print("\n")

print(m_set4)
x = input("is your birthday month in this list?")
if x == "yes" or x == "y":
    month += 4
print("\n")

print(m_set8)
x = input("is your birthday month in this list?")
if x == "yes" or x == "y":
    month += 8
print("\n")

print("your birth month is", month)
print("\n")
#year starts here

year = 0
print("this year chart only works for 2000 to 2015")

print(y_set1)
x = input("is your birth year in this list?")
if x == "yes" or x == "y":
    year += 1
print("\n")

print(y_set2)
x = input("is your birth year in this list?")
if x == "yes" or x == "y":
    year += 2
print("\n")

print(y_set4)
x = input("is your birth year in this list?")
if x == "yes" or x == "y":
    year += 4
print("\n")

print(y_set8)
x = input("is your birth year in this list?")
if x == "yes" or x == "y":
    year += 8
print("\n")
    
year = 2000+year





print("your birth year is", year)
print("\n")
print("your birthdate is", month, "/", birthday, "/", year)



        

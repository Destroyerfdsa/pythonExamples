NUM128 = 128
NUM64 = 64
NUM32 = 32
NUM16 = 16
NUM8 = 8
NUM4 = 4
NUM2 = 2
NUM1 = 1

loop = 0

day_set1="set 1: "
day_set2="set 2: "
day_set4="set 3: "
day_set8="set 4: "
day_set16="set 5: "

whatsLeft = 0

for i in range(1,32):
    bi_num=""
    input_num=i
    whatsLeft = input_num

    if input_num >= NUM128:
        whatsLeft = input_num - NUM128
        bi_num += "1"
    else:
        bi_num += "0"

    if whatsLeft >= NUM64:
        whatsLeft = whatsLeft-NUM64
        bi_num += "1"
    else:
        bi_num += "0"

    if whatsLeft >= NUM32:
        whatsLeft = whatsLeft-NUM32
        bi_num += "1"
    else:
        bi_num += "0"

    if whatsLeft >= NUM16:
        whatsLeft = whatsLeft-NUM16
        bi_num += "1"
    else:
        bi_num += "0"

    if whatsLeft >= NUM8:
        whatsLeft = whatsLeft-NUM8
        bi_num += "1"
    else:
        bi_num += "0"
    if whatsLeft >= NUM4:
        whatsLeft = whatsLeft-NUM4
        bi_num += "1"
    else:
        bi_num += "0"

    if whatsLeft >= NUM2:
        whatsLeft = whatsLeft-NUM1
        bi_num += "1"
    else:
        bi_num += "0"

    if whatsLeft >= NUM1:
        whatsLeft = whatsLeft-NUM64
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
    
    x=str(i)
    if xnum3 == "1":
        day_set16+= x+" "
    if xnum4 == "1":
        day_set8+= x+" "
    if xnum5 == "1":
        day_set4+= x+" "
    if xnum6 == "1":
        day_set2+= x+" "
    if xnum7 == "1":
        day_set1+= x+" "








##    loop += 1
##    print(bi_num)
##print(loop)
    

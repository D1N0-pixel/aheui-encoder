# -*- coding:utf-8 -*-
toChange = input()

result = "발박따밭따빠싹발받따다빠싼발박따밝다다빠싿발받따다빠쌀발박따밝다다빠쌈발받따다쌉"

def transNum(num):
    if num == 0:
        return ""
    elif num == 1:
        return "받반타"
    elif num == 2:
        return "반"
    elif num == 3:
        return "받"
    elif num == 4:
        return "밥"
    elif num == 5:
        return "발"
    elif num == 6:
        return "밦"
    elif num == 7:
        return "밝"
    elif num == 8:
        return "밣"

def beforeNum(margin):
    global result
    result += "삭빠"
    result += transNum(abs(margin))
    if margin > 0:
        result += "타"
    elif margin < 0:
        result += "다"
    result += "맣"

def afterNum(margin):
    global result
    result += "산빠"
    result += transNum(abs(margin))
    if margin > 0:
        result += "타"
    elif margin < 0:
        result += "다"
    result += "맣"

def beforeCap(margin):
    global result
    result += "삳빠"
    result += transNum(abs(margin))
    if margin > 0:
        result += "타"
    elif margin < 0:
        result += "다"
    result += "맣"

def afterCap(margin):
    global result
    result += "살빠"
    result += transNum(abs(margin))
    if margin > 0:
        result += "타"
    elif margin < 0:
        result += "다"
    result += "맣"

def beforeSmall(margin):
    global result
    result += "삼빠"
    result += transNum(abs(margin))
    if margin > 0:
        result += "타"
    elif margin < 0:
        result += "다"
    result += "맣"

def afterSmall(margin):
    global result
    result += "삽빠"
    result += transNum(abs(margin))
    if margin > 0:
        result += "타"
    elif margin < 0:
        result += "다"
    result += "맣"

for i in toChange:
    if ord(i) >= 32 and ord(i) < 48:
        beforeNum(40 - ord(i))
    elif ord(i) >= 48 and ord(i) < 64:
        afterNum(55 - ord(i))
    elif ord(i) >= 64 and ord(i) < 80:
        beforeCap(72 - ord(i))
    elif ord(i) >= 80 and ord(i) < 96:
        afterCap(87 - ord(i))
    elif ord(i) >= 96 and ord(i) < 112:
        beforeSmall(104 - ord(i))
    elif ord(i) >= 112 and ord(i) < 127:
        afterSmall(119 - ord(i))
    else:
        print("지원되지 않는 문자가 포함되어 있습니다")
        exit()
result += "희"
print(result)

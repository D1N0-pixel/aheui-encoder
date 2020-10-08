# -*- coding:utf-8 -*-
import sys 

result = str()
bN = False
aN = False
bC = False
aC = False
bS = False
aS = False
kor = False

def whichChar(toChange):
    global result, bN, aN, bC, aC, bS, aS
    for i in toChange:
        if ord(i) >= 32 and ord(i) < 48:
            bN = True
        elif ord(i) >= 48 and ord(i) < 64:
            aN = True
        elif ord(i) >= 64 and ord(i) < 80:
            bC = True
        elif ord(i) >= 80 and ord(i) < 96:
            aC = True
        elif ord(i) >= 96 and ord(i) < 112:
            bS = True
        elif ord(i) >= 112 and ord(i) < 127:
            aS = True
        elif ord(i) > 10000:
            kor = True
        else:
            print("지원되지 않는 문자가 포함되어 있습니다")
            exit()

def useChar():
    global result, bN, aN, bC, aC, bS, aS
    if bN:
        result += "발밣따싹"
    if aN:
        result += "발밦다발따싺"
    if bC:
        result += "밢밣따싻"
    if aC:
        result += "밢밢따밦다싼"
    if bS:
        result += "밦밝다밣따싽"
    if aS:
        result += "밢밣다밝따싾"
    if kor:
        result += "발반따빠빠싿빠빠따빠쌀따빠쌁따쌂"

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
    elif num == 9:
        return "밢"

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
    result += "삮빠"
    result += transNum(abs(margin))
    if margin > 0:
        result += "타"
    elif margin < 0:
        result += "다"
    result += "맣"

def beforeCap(margin):
    global result
    result += "삯빠"
    result += transNum(abs(margin))
    if margin > 0:
        result += "타"
    elif margin < 0:
        result += "다"
    result += "맣"

def afterCap(margin):
    global result
    result += "산빠"
    result += transNum(abs(margin))
    if margin > 0:
        result += "타"
    elif margin < 0:
        result += "다"
    result += "맣"

def beforeSmall(margin):
    global result
    result += "삱빠"
    result += transNum(abs(margin))
    if margin > 0:
        result += "타"
    elif margin < 0:
        result += "다"
    result += "맣"

def afterSmall(margin):
    global result
    result += "삲빠"
    result += transNum(abs(margin))
    if margin > 0:
        result += "타"
    elif margin < 0:
        result += "다"
    result += "맣"

def kor(letter):
    global result
    num = list(map(lambda x: int(x), list(str(letter))))
    ten = ['삶','삵','살','삳']
    zero = 0
    for i in range(len(num)-1):
        if num[i] != 0:
            result += ten[i]
            result += "빠쌃삷"
            if num[i] != 1:
                result += transNum(num[i])
                result += "따"
        else:
            zero += 1
    if num[4] != 0:
        result += transNum(num[4])
        result += "다"
    result += "다" * (3 - zero)
    result += "맣"

def newLine():
    global result
    result += "발박따맣"

def encode(toChange):
    global result
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
        elif ord(i) > 10000 and ord(i) < 100000:
            kor(ord(i))

def main():
    global result
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            toChange = file.read().split('\n')
            for i in toChange:
                whichChar(i)
            useChar()
                
        with open(sys.argv[1], 'r') as file:
            toChange = file.read().split('\n')
            for i in toChange:
                encode(i)
                newLine()
            result = result[:-4]
    else:
        toChange = input()
        whichChar(toChange)
        useChar()
        encode(toChange)
    result += "희"
    print(result)

if __name__ == "__main__":
    main()
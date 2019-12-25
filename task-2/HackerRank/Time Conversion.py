import os
import sys
def timeConversion(s):
    lst = []
    h1 = int(s[1])
    h2 = int(s[0])
    hh = (h2 * 10) + (h1 % 10)
    if s[8] == 'A' :
        if hh == 12:
            lst.append("00")
            for i in range (2,8):
                lst.append(str(s[i]))
        else:
            for i in range (0,8):
                lst.append(str(s[i]))
    else:
        if hh == 12:
            lst.append("12")
            for i in range (2,8):
               lst.append(str(s[i]))
        else:
            hh = hh + 12
            lst.append(str(hh))
            for i in range(2,8):
                lst.append(str(s[i]))
    return "".join(lst)
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()




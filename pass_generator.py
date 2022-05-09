import secrets as s
import re
pool = [
"A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", "!", "@", "#", "$", "%", "&", "*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
]


def selection():
    count=40
    while count>0:
        l.append(pool[s.randbelow(67)])
        count-=1
while True:
    l = []
    selection()
    pw="".join([str(i) for i in l])

    patt = r"[0-9]"
    patt1 = r"[a-z]"
    patt2 = r"[A-Z]"
    patt3 = r"[!@#$%]"
    if re.search(patt, pw):
        if re.search(patt1, pw):
            if re.search(patt2, pw):
                if re.search(patt3, pw):
                    print(pw)
                    break
            
        
    else:
        del(l)
        continue



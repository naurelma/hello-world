kaikki = "qwertyuiopåasdfghjklöä'zxcvbnm,.- !#¤%&/()=?`1234567890+´QWERTYUIOPÅASDFGHJKLÖÄ*ZXCVBNM;:_€@£${[]}§½<>|!"


def count(f,char):
    count = {}
    for i in kaikki:
        count[i] = 0
    count["\n"] = 0
    count['"'] = 0
    total = 0
    for i in f:
        for j in i:
            total += 1
            count[j] += 1
    return [total, count]
                

import states

def init(nimi = "100", kenttä = "sade", value = 1):
    template = states.tilat[kenttä]
    current = template.copy()
    seur = {}
    for i,v in current.items():
        seur[i] = 0
    current = seur.copy()
    #print(template)
    #print (seur)


    current[nimi]=value
    for luku in range(60000):
        for n,v in current.items():
            for i in template[n]:
                seur[i[0]]+=i[1]*v
        current = seur.copy()
        for n,v in seur.items():
            seur[n] = 0

    print(current)
    input()

if __name__ == "__main__":
    print(__name__)
    test = input()
    #init(test)

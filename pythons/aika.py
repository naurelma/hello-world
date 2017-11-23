def main():
    while True:
        aika = input("Anna aika: ")
        tunnit = int(aika[:1])
        paikka = input("Anna lyhenne tai määrä: ")
        try:
            muutos = int(paikka)
        except:
            paikka = paikka.lower()
            if paikka == "gmt":
                muutos = 0
            elif paikka == "cst":
                muutos = -10

        
            

            

if __name__ == "__main__":
    main()

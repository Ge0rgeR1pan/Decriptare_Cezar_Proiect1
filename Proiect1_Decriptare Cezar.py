# Proiect Python  1
#Criptare/Decriptare codul Cezar

def criptare(k,text):
    crip = ''
    for caracter in text:
        if caracter not in " ,.?!":
            val =ord(caracter) #conversie in ASCII
            val += k
            while ( val>90 and caracter<="Z") or (val>122 and caracter<="z"):
                val -= 26 # revenire la A sau a
            caracter=chr(val) # conversie in char
        crip += caracter
    return crip

def decriptare(k,text):
    decrip = ''
    for caracter in text:
        if caracter not in " ,.?!":
            val =ord(caracter) # conversie in ASCII
            val -= k
            while (val<65 and caracter<="Z") or (val<97 and caracter<="z" and caracter>="a"):
                val += 26 #revenire la Z sau z
            caracter=chr(val) # conversie in char
        decrip += caracter 
    return decrip

def verf_romana(text):
    list = text.split(" ")
    ok=1
    for cuvant in list:
        ok2=0
        for i in cuvant:
            if i in "AEIOUaeiou":# verificare vocala
                ok2=1
        if ok2==0: ok=0
    return ok


text = input("Introdu un text:\n")
k = int(input("Introdu cheia de criptare:\n"))

text=criptare(k,text) # criptare text
print("Textul cripat este:", text)
print()
print("Textul decriptat este:", decriptare(k,text))


# Daca nu se cunoaste cheia de criptare
print()
for cheie in range(1,27):
    rasp = decriptare(cheie,text)
    if verf_romana(rasp)==1:
        print("Cheia",cheie,":",rasp)
        
        

    


        
    
      
       
        
    
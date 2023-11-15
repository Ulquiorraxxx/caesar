alfabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#def sifresana; t=ievaditais teksts; r=rotacijas skaitlis; Katru burtu no ievadita teksta meklē vai ir tekstā alfabets, ja tāda burta tur nav tad ievadītā teksta burts paliek tāds pats else: Azivieto to burtu ar + o vērtību nākamais burts pec alfabēta (A ir 1, B ir 2, C ir 3, utt.) un pievieno to pie izvades teksta r
def sifresana(teksts, rotacija):
    rezultats = ""
    for c in teksts:
        c=c.upper()
        if (alfabets.find(c) == -1):
            rezultats+=c
        else:
            rezultats += (alfabets[(alfabets.find(c) + rotacija) % len(alfabets)])
    return rezultats
#def atsifresana; t=ievaditais teksts; r=rotacijas skaitlis; Katru burtu no ievadita teksta meklē vai ir tekstā alfabets, ja tāda burta tur nav tad ievadītā teksta burts paliek tāds pats else: Azivieto to burtu ar - o vērtību iepriekšējais burts pec alfabēta (A ir 1, B ir 2, C ir 3, utt.) un pievieno to pie izvades teksta r
def atsifresana(teksts, rotacija):
    rezultats = ""
    for c in teksts:
        c=c.upper()
        if (alfabets.find(c) == -1):
            rezultats += c
        else:
            rezultats += (alfabets[(alfabets.find(c) - rotacija) % len(alfabets)])
    return rezultats

def fullatsifresana(teksts, n):
    rezultats = ""
    
    for c in teksts:
        c=c.upper()
        if (alfabets.find(c) == -1):
            rezultats += c
        else:
            rezultats += (alfabets[(alfabets.find(c) - n) % len(alfabets)])
    return rezultats
        

w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))
#ja ivada mode '1' tad izvada 2 tekstus (otrais parādās tikai tad, kad tiek ievaditi dati pēc pirmā teksta) un izmantojas def sifresana
if mode == 1:
    text = input("Enter the text: ")
    rotation = int(input("Enter the rotation: "))
    print("Encrypted: " + sifresana(text, rotation))
#ja ivada mode '2' tad izvada 2 tekstus (otrais parādās tikai tad, kad tiek ievaditi dati pēc pirmā teksta) un izmantojas def atsifresana
elif mode == 2:
    text = input("Enter the text: ")
    rotation = int(input("Enter the rotation: "))
    print("Decrypted: " + atsifresana(text, rotation))
#ja ievada mode=3 tad izvada 2 textus uzreiz
elif mode == 3:
    text = input("enter the text: ")
    for n in range(27):
        
        print(str(n) + ": " + fullatsifresana(text, n))
else:
    print("Wrong input")

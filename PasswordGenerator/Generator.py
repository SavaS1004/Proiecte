
import string
import secrets
import pickle

MASTERPASSWORD = "100469"
DATA_FILE = "Data.pkl"

def RandomGenerator (useDigits, useSymbol, length):
    characters=string.ascii_letters
    if(useDigits):
        characters+=string.digits
    if(useSymbol):
        characters+=string.punctuation
    password=''.join(secrets.choice(characters) for _ in range(length))
    return password

def SaveData(storageAccounts):
    with open("DATA_FILE","wb") as file:
        pickle.dump(storageAccounts,file)

def LoadData():
    try:
        with open("DATA_FILE","rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}
def Meniu():


    print("\n..........................")
    print("1.Cautare.")
    print("2.Adaugare cont existent.")
    print("3.Adauagre cont nou.")
    print("4.Modificare.")
    print("5.Stergere.")
    print("6.Afisare totala")
    print("7.Iesire.")
    print("..........................")

def AddNewAccount(storageAccounts):
    id=input("Site/aplicatie:")
    email=input("Username sau email:")
    password=RandomGenerator(True, True,16)
    storageAccounts[id]=[email,password]

def AddExistingAccount(storageAccounts):
    name=input("Site/aplicatie:")
    email=input("Username sau email:")
    password=input("Noua parola.")
    storageAccounts[name]=[email,password]

def SearchAccount(storageAccounts):
    name=input("Ce cautati?")
    if name in storageAccounts:
        print(storageAccounts[name])
    else:
        print("Contul cautat nu este prezent.")

def ChangeAccount(storageAccounts):
    name=input("La ce cont faci modificari?")
    if name not in storageAccounts:
        print("Contul nu este prezent.")
    else:
        option=5
        while(option!=4):
            print("1.Username\n" \
        "2.Password\n" \
        "3.Contul intreg.\n" \
        "4.Iesire.")
            option=int(input("Ce doriti sa schimbati?"))
            if option==1:
                username=input("Username sau email:")
                storageAccounts[name][0]=username
            elif option ==2:
                password=input("Noua parola.")
                storageAccounts[name][1]=password
            elif option==3:
                username=input("Username sau email:")
                password=input("Noua parola.")
                storageAccounts[name]=[username,password]
            elif option==4:
                print("Exit.")
                break
            else:
                print("Optiune invalida.")
def DeleteAccount(storageAccounts):
    name=input("Ce cont stergi?")
    if name in storageAccounts:
        storageAccounts.pop(name)
    else:
        print("Contul cautat nu este prezent.")

def ShowAll(storageAccounts):
    for site, (email, password) in storageAccounts.items():
        print(f"🔹 Site: {site} | 📧 Email: {email} | 🔑 Parolă: {password}")
    
def main():
    if input("Parola:") != MASTERPASSWORD:
        print("Acces refuzat.")
        return
    storageAccounts=LoadData()
    
    while(True):
        Meniu()
        option=int(input("Ce vrei sa faci?"))
        if option==7:
            print("Exit.")
            SaveData(storageAccounts)
            break
        elif option==1:
            SearchAccount(storageAccounts)
            SaveData(storageAccounts)
        elif option==2:
            AddExistingAccount(storageAccounts)
            SaveData(storageAccounts)
        elif option==3:
            AddNewAccount(storageAccounts)
            SaveData(storageAccounts)
        elif option==4:
            ChangeAccount(storageAccounts)
            SaveData(storageAccounts)
        elif option==5:
            DeleteAccount(storageAccounts)
            SaveData(storageAccounts)
        elif option==6:
            ShowAll(storageAccounts)
            SaveData(storageAccounts)

main()


import string
import secrets
import pickle
from cryptography.fernet import Fernet
from getpass import getpass
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

def SaveData(storageAccounts, fernet):
    data = pickle.dumps(storageAccounts)
    encrypted_data = fernet.encrypt(data)
    with open(DATA_FILE, "wb") as file:
        file.write(encrypted_data)

def LoadData(fernet):
    try:
        with open(DATA_FILE, "rb") as file:
            encrypted_data = file.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            return pickle.loads(decrypted_data)
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

def CheckDuplicates(storageAccounts, name):
    if name in storageAccounts:
        # if any( email== acc[0] for acc in storageAccounts[name]):
        return True
    
    return False
def AddNewAccount(storageAccounts):
    id=input("Site/aplicatie:")
    email=input("Username sau email:")
    password=RandomGenerator(True, True,16)
    print(f"Parola generată: {password}")
    storageAccounts[id]=[(email,password)]

def AddExistingAccount(storageAccounts):
    name=input("Site/aplicatie:")
    if name in storageAccounts:
        option=int(input("Exista un cont deja.\n Doriti sa adaugati inca unul?\n1-'DA'\n2-'NU'"))
        if option==2:
            return
        elif option!=1:
            print("Optiune invalida.")
            return
    email=input("Username sau email:")
    password = input("Noua parola:")
    if name not in storageAccounts:
        storageAccounts[name] = []
    storageAccounts[name].append((email, password))
    print("✅ Contul a fost adăugat.")

def SearchAccount(storageAccounts):
    name=input("Ce cautati?")
    if name in storageAccounts:
        email, password = storageAccounts[name]
        print(f"📧 Email: {email} | 🔑 Parolă: {password}")
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
            email,password=storageAccounts[name]
            if option==1:
                username=input("Username sau email:")
                storageAccounts[name]=(username,password)
            elif option ==2:
                password=input("Noua parola.")
                storageAccounts[name]=(email,password)
            elif option==3:
                username=input("Username sau email:")
                password=input("Noua parola.")
                storageAccounts[name]=(username,password)
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
    
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()


def main():
    fernet = Fernet(load_key())
    if getpass("Parola:") != MASTERPASSWORD:
        print("Acces refuzat.")
        return
    storageAccounts=LoadData(fernet)
    
    while(True):
        Meniu()
        option=int(input("Ce vrei sa faci?"))
        if option==7:
            print("Exit.")
            SaveData(storageAccounts, fernet)
            break
        elif option==1:
            SearchAccount(storageAccounts)
        elif option==2:
            AddExistingAccount(storageAccounts)
            SaveData(storageAccounts, fernet)
        elif option==3:
            AddNewAccount(storageAccounts)
            SaveData(storageAccounts, fernet)
        elif option==4:
            ChangeAccount(storageAccounts)
            SaveData(storageAccounts, fernet)
        elif option==5:
            DeleteAccount(storageAccounts)
            SaveData(storageAccounts, fernet)
        elif option==6:
            ShowAll(storageAccounts)
            

main()

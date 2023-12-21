from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''
def load_key():
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key 

master_pwd = input("what is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())#strip off character
            user, passw = data.split("|")
            print("user: " + user + ", password: " + fer.decrypt(passw.encode()).decode())

view()

def add():
    name = input("account name: ")
    pwd = input("password: ")
#w - overwrite, r - read, a - appendable file if passwords.txt exists
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("would you like to add a new passowrd or view saved passwords? ")
    if mode == 'q':
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode. ")
        continue

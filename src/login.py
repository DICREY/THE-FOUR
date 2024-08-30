from config.usuario import Usuario
import bcrypt
def login():
    def check(user = None,password = None):
        return Usuario().login(user,password)
    
    while True:
        try:
            user = input("Ingrese el correo: ")
            if "@" in user and 0 < len(user):
                break
        except ValueError:
            print("Correo Invalido")
            continue
    while True:
        try:
            password = input("Ingrese la contraseña: ")
            if 8 < len(password):
                pwd = password.encode("utf-8")
                sal = bcrypt.gensalt()
                escript = bcrypt.hashpw(pwd,sal)
                break
        except ValueError:
            print("Contraseña Invalida")
            continue
    
    checking = check(user,password)
    if checking:
        print("Ingreso Exitoso")
    else:
        print("Usuario No Existe")
login()


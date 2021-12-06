
import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("clave.json")
firebase_admin.initialize_app(cred)
usuarios = []
condition = True
db = firestore.client()
def agregarDatos(email,password):
    data = {"Email":email,"Contraseña":password}
    doc_ref = db.collection("users").add(data)

def leerDato():
    docs =  db.collection("users").stream()
    for doc in docs:
        datos = doc.to_dict()
        usuarios.append([doc.id,datos["Email"],datos["Contraseña"]])
    for i in usuarios:
        print(i)


while(condition == True):
    print("FIREBASE REGISTRO DE EMAILS")
    print("OPCION 1: CREATE EMAIL")
    print("OPCION 2: READ EMAIL")
    print("OPCION 3: EXIT APP")
    entry = int(input("INGRESA UNA OPCION:  "))
    if entry == 1:
        print("INGRESA UN EMAIL Y CONTRASEÑA")
        email = str(input("INGRESA UN EMAIL:  "))
        password = str(input("INGRESA UNA CONTRASEÑA:  "))
        agregarDatos(email,password)
    elif entry == 2:
        print("ESTAS SON LAS CUENTAS")
        leerDato()
    elif entry == 3:
        print("SALISTE DEL PROGRAMA")
        condition = False
    else:
        entry = int(input("INGRESA UNA OPCION VALIDA:  "))







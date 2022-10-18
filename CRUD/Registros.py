import json

def GrabarJson(Nombre,password):
    Json = 'JSON/Usuarios.json'
    data = {}
    with open(Json) as file:
        data = json.load(file)

    ##for client in data['usuarios']:
    ##   print('Nombre:', client['Nombre'])

    entry = {"Nombre" :Nombre ,"password" :password}
    data['usuarios'].append(entry)

    with open(Json, "w") as file:
        json.dump(data, file)
    return 
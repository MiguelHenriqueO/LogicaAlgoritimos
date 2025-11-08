def incluir(lista,cod,desc,valor):
    lista.append({
        'codigo':cod,
        'descricao':desc,
        'valor':valor})

lista = []

incluir(lista, 111, 'tv', 1999.99)
incluir(lista, 222, 'geladeira', 2500.0)

print(lista)

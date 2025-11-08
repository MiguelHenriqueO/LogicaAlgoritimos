def contarVogal(text):
    vogais = ["a","e","i","o","u"]
    cont = 0
    for c in text:
        for v in vogais:
            if c == v:
                cont = cont +1
    return cont


texto = input("informe um texto: ")

print(contarVogal(texto))
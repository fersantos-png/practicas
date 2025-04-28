def censor(a, b):
    len_b = len(b)
    i = []
    for char in a:
        i.append(char)
        if len(i) >= len_b and ''.join(i[-len_b:]) == b:
            del i[-len_b:]
    return ''.join(i)


a = input("ingresa la frace que se quiere cencusar: ").strip()
b = input("ingresa la frace a eliminar: ").strip()

censura = censor(a, b)

# Mostrar el resultado en la consola
print(censura)
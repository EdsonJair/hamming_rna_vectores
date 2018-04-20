import numpy as np

# PATRONES EJEMPLARES
a1 = [1, 1, 1]
a2 = [-1, -1, -1]
a3 = [1, -1, 1]

entradas = [a1, a2, a3]

prueba1 = [-1, 1, 1]
# prueba2=[1,-1,1]
# prueba3=[1,1,-1]
valores_pesos = []
print("++++++++  PATRONES EJEMPLARES ++++++")
print(entradas)
j = 0
i = 0
pos_e = 0
pos_s = 0
while (j < len(entradas)):
    for i in range(len(entradas[j])):
        valor = entradas[j][i] * 1 / 2
        valores_pesos.append(valor)
    j += 1
matrices_pesos = np.array(valores_pesos).reshape(len(entradas), len(a1))
print("++++++++  Matrices Pesos: ++++++")
print(matrices_pesos)
vias = []
for i in range(len(entradas)):
    valor_vias = len(entradas[i]) / 2
    vias.append(valor_vias)
vias = np.array(vias).reshape(len(entradas), 1)
print("+++++++++++  VIAS: +++++++++++++")
print(vias)
#####    Patron   ######
patron = np.array(prueba1).reshape(1, len(prueba1))
patron_t = np.transpose(patron)
u = np.dot(matrices_pesos, patron_t) + vias

u0 = []
for i in u:
    j = i * (1 / len(a1))
    u0.append(j)
u0 = np.array(u0).reshape(1, len(entradas))
print("u0", u0)
###FUNCION DE TRANSFERENCIA
x = 0
y1 = []
for x in u0:
    if x.all() > 1:
        y1.append(1)
    elif x.all() >= 0 or x.all() <= 1:
        y1.append(x)
    else:
        y1.append(0)
y1 = np.array(y1).reshape(u0.shape)
y1_1 = y1[0]
convergencia = False
E = (1 / (len(a1) - 1))
c = 0
suma = 0
aux = 0
n_iter = 1
while convergencia != True:
    y = []
    y0 = []
    for j in range(len(y1_1)):
        suma += y1_1[j]
    for i in range(len(y1_1)):
        value = y1_1[i] - (E * (suma - y1_1[i]))
        y0.append(value)

    for x in y0:
        if x > 1:
            y.append(1)
        elif x >= 0 and x <= 1:
            y.append(x)
        else:
            y.append(0)
    veces = y.count(0)
    if veces == (len(y) - 1):
        convergencia = True
        maximo = max(y)
        posicion = y.index(maximo)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(y, "iteracion", n_iter)
        print("La red converge y asocia con el patron", posicion, entradas[posicion])
    else:
        y1_1 = y
        print(y1_1, "iteracion", n_iter)
        n_iter += 1
        suma = 0
        maximo = max(y1_1)
        valor = y1_1.count(maximo)
        if (valor >= 2):
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("La red NO converge y NO asocia con NINGUN patron porque tienes mas de un valor igual")
            print(y1_1)
            break



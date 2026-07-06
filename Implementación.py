import numpy as np


print("Bienvenido \n")

grado = int(input("Digite el grado de la función de recurrencia: "))
print("")



valores_iniciales = []

for i in range(0,grado):

    valores_iniciales.append(int(input(f"Digite el valor inicial de f_({i}): ")))

print("")

print("Los valores iniciales son: ")

for i in range(0,grado):

    print(f"f_({i}) = {valores_iniciales[i]}")

print("")



coeficientes = []

funcion_de_recurrencia="f_(n) = "

for i in range(0,grado):

    coeficientes.append(int(input(f"Digite el coeficiente de f_(n-{i+1}): ")))

    if i == grado-1 :
      funcion_de_recurrencia = funcion_de_recurrencia + f"({str(coeficientes[i])})f_(n-{i+1})"
    else :
      funcion_de_recurrencia = funcion_de_recurrencia + f"({str(coeficientes[i])})f_(n-{i+1}) + "

print("")
print("Esta es la función de recurrencia: \n" + funcion_de_recurrencia + "\n")



funcion_de_recurrencia_homogenea = "f_(n) + "

for i in range(0,grado):

  if i == grado-1 :
    funcion_de_recurrencia_homogenea = funcion_de_recurrencia_homogenea + f"({str(- coeficientes[i])})f_(n-{str(i+1)}) = 0"
  else :
    funcion_de_recurrencia_homogenea = funcion_de_recurrencia_homogenea + f"({str(- coeficientes[i])})f_(n-{str(i+1)}) + "

print("Este es la función de recurrencia de manera homogenea: \n" + funcion_de_recurrencia_homogenea + "\n")



polinomio_caracteristico = f"t^{grado} + "

for i in range(0,grado):

  if i == grado-1 :
    polinomio_caracteristico = polinomio_caracteristico + f"({str(- coeficientes[i])}) = 0"
  elif i == grado-2 :
    polinomio_caracteristico = polinomio_caracteristico + f"({str(- coeficientes[i])})t + "
  else :
    polinomio_caracteristico = polinomio_caracteristico + f"({str(- coeficientes[i])})t^({str(grado-(i+1))}) + "

print("Este es el polinomio característico: \n" + polinomio_caracteristico + "\n")



coeficientes_totales = [None]*(grado+1)

# Tomamos el coeficiente de f_n como 1 ya que las raices son enteras

coeficientes_totales[0] = 1

for i in range (0,grado):

  coeficientes_totales[i+1] = - coeficientes[i]



raices = np.roots(coeficientes_totales)
raices = np.round(raices)
raices = raices.astype(int)
print("Las raíces del polinomio característico son: ")


for i in range(0,len(raices)):

  print(f"r_{i+1} = {str(raices[i])}")



multiplicidad_raices = []
raices_iguales = False
raices_sin_repeticiones = []

for i in range(0,len(raices)):

  if raices[i] not in raices_sin_repeticiones:
    raices_sin_repeticiones.append((raices[i]))

    contador_multiplicidad = 1

    for j in range(i,len(raices)):

      if raices[i] == raices[j] and i!=j:
        raices_iguales = True
        contador_multiplicidad = contador_multiplicidad + 1

    multiplicidad_raices.append(contador_multiplicidad)

print("")
print("La multiplicidad de las raices son: ")

for i in range(0,len(raices_sin_repeticiones)):

  print(f"Multiplicidad de r_({str(raices_sin_repeticiones[i])}) = {str(multiplicidad_raices[i])}")

ecuaciones = []

if raices_iguales==True:

  for i in range(0,grado):

    ecuaciones.append([])

    for j in range(0,len(raices_sin_repeticiones)):

      for k in range(0,(multiplicidad_raices[j])):

        ecuaciones[i].append(((raices_sin_repeticiones[j])**i)*((i)**k))

else:
  for i in range(0,grado):

    ecuaciones.append([])

    for j in range(0,len(raices_sin_repeticiones)):

      ecuaciones[i].append(((raices_sin_repeticiones[j])**i))



igualdades = []

for i in range(0,grado):

  igualdades.append(valores_iniciales[i])



a=np.array(ecuaciones)
b=np.array(igualdades)
incognitas = np.linalg.solve(a,b)



formula_no_recurrente = ""
aux = 0

# Dejamos un espacio entre las multiplicaciones para que se pudiera evidenciar mejor cada operación y no se vieran tan contraidas

if raices_iguales==True:

    for j in range(0,len(raices_sin_repeticiones)):

      for k in range(0,(multiplicidad_raices[j])):

        if j == len(raices_sin_repeticiones)-1 and k == multiplicidad_raices[j]-1:
          formula_no_recurrente = formula_no_recurrente + f"(({str(incognitas[aux])})n^{str(k)} ({str(raices_sin_repeticiones[j])})^n)"

        else:
          formula_no_recurrente = formula_no_recurrente + f"(({str(incognitas[aux])})n^{str(k)} ({str(raices_sin_repeticiones[j])})^n) + "

        aux = aux + 1

else:

  for i in range (0,grado):

    if i==grado-1:
      formula_no_recurrente = formula_no_recurrente + f"(({str(incognitas[i])}) ({str(raices_sin_repeticiones[i])})^n)"
    else:
      formula_no_recurrente = formula_no_recurrente + f"(({str(incognitas[i])}) ({str(raices_sin_repeticiones[i])})^n) + "

print("")
print("Esta es la función no recurrente: \n" + formula_no_recurrente + "\n")
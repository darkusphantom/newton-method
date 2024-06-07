import math

diferencia =  0.00000045399 # EPSILON
valorMinimo = 0.0000004 # DELTA
PI = 3.1416   # VALOR DE PI
M = 3000 # MAXIMO DE ITERACIONES


def function(x):  # FUNCION
    c = 2 * x

    if (c - ((math.pi / 2) * 1.0)) != math.pi:
        b = math.cos(c)
    else:
        b = 0  # coseno vale cero en este punto

    if (x - (math.pi)) != math.pi:
        a = math.sin(x)
    else:
        a = 0  # seno vale cero en este punto

    return ((0.25 * pow(x, 2)) - (x * a) - ((0.5) * b) + 0.5)


def function_der(x): # FUNCION DERIVADA
    # ejercio 2
    aux = x * 2

    if (aux - math.pi) != math.pi:
        a = math.sin(aux)
    else:
        a = 0 # coseno vale cero en este ppunto

    if (x - ((math.pi / 2) * 1.0)) != math.pi:
        b = math.cos(x)
    else:
        b = 0 # coseno vale cero en este ppunto

    if (x - ((math.pi / 2) * 1.0)) != math.pi:
        b = math.cos(x)
    else:
        b = 0 # coseno vale cero en este ppunto

    if (x - math.pi) != math.pi:
        c = math.sin(x)
    else:
        c = 0

    return (((0.5) * x) + a - (x * b) - c)

def methodNewton():
    converge = False
    a = ((math.pi) / 2) * 1.0
    b = 5 * (math.pi)
    c = 10 * (math.pi)

    t0 = [a, b, c]

    for l in range(1):
        v = function(t0[l])
        print("METODO DE NEWTON-\n\n")

        print("VALORES INICIALES:\n")
        print("\t t0= ", t0[l], "  v=", v, "\n")

        if abs(v) >= valorMinimo:  # t0 en la funcion es mayor al valor minimo
            i = 0
            auxt0 = t0[l]
            while (i < M) and (not converge):  # MIENTRAS NO SE AGOTEN EL MAXIMO DE ITERACION Y LA FUNCION NO CONVERGE
                # ECUACIONES PARA CONSEGUIR EL SIGUIENTE T1
                fx = function_der(auxt0)
                t1 = auxt0 - ((v / fx) * 1.0)
                v = function(t1)

                print("  i=", i + 1, "    t1=", t1, "    fx=", v, "    f'x=", fx, "\n")
                if (abs(t1 - auxt0) <= diferencia) or (abs(v) <= valorMinimo):  # CONDICION DE PARADA, CUANDO HAYA UNA RAIZ
                    converge = True  # DETIENE EL CICLO
                    raiz = t1  # VARIBALE QUE REPRESENTA LA RAIZ
                else:
                    if math.isnan(t1) or math.isnan(v):  # VALIDA SI NO ES UN NUMERO, PARA QUE CICLO PARE
                        i = M  # DETIENE EL CICLO
                    i += 1  # INCREMENTO DE ITERACION
                    auxt0 = t1  # ASIGNACION DEL NUEVO AUXT0

        if converge:  # SI CONVERGE MUESTRA LA RAIZ SINO MUESTRA (NO EXISTE RAIZ)
            print("EXISTE RAIZ: ", raiz)
        else:
            print("NO EXISTE RAIZ")
        converge = False  # REINICIA LA VARIABLE CONVERGE
        print("\n\n")

methodNewton()
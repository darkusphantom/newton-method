import math

M = 10  # MAXIMO ITERACIONES
diferencia = 0.11  # EPSILON
valorMinimo = 0.1  # DELTA

def funtion(x):  # RESULTADO f(t0)
    return ((0.9060939 * x) * math.exp((-1.0 * x) / 3))

def funtion_der(x):  # RESULTADO f'(t0)
    return (math.exp((-1.0 * x) / 3) - (((x) * math.exp((-1.0 * x) / 3)) / 3))

def mNewton():  # ALGORITMO DEL METODO DE NEWTON
    converge = False
    auxt0 = 0.25
    v = funtion(auxt0)

    print("METODO DE NEWTON")
    print(f"VALORES INICIALES: i=0  t0={auxt0}  fx={v}\n")

    if abs(v) >= valorMinimo:
        i = 0
        while (i < M) and (not converge):
            fx = funtion_der(auxt0)
            t1 = auxt0 - ((v / fx) * 1.0)
            v = funtion(t1)

            print(f"  i={i + 1}    t1={t1}    fx={v}    f'x={fx}\n")
            if (abs(t1 - auxt0) <= diferencia) or (abs(v) <= valorMinimo):
                converge = True
                raiz = t1
            else:
                if math.isnan(t1) or math.isnan(v):
                    i = M
                i += 1
                auxt0 = t1

        if converge:
            print(f"EXISTE RAIZ: {raiz}")
        else:
            print("NO EXISTE RAIZ")
        converge = False
        print("\n\n")

mNewton()

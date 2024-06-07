import math

S = 20
diferencia = 0.00000000045399  # epsilon elevado a la -10

def funtion(x):
    return ((2 * x**3) - ((34.0 / 7) * (x**2)) + ((209.0 / 49) * x) - (173.0 / 343))

def methodSecant(x1, x2):  # ALGORITMO DEL METODO DE LA SECANTE
    converge = False
    i = 0
    print("METODO DE LA SECANTE")
    print(f"VALORES INICIALES: i=0   x1={x1}  x2={x2}\n")

    while (i < S) and (not converge):  # MIENTRAS NO SE AGOTEN EL MAXIMO DE ITERACION Y LA FUNCION NO CONVERGE
        fx1 = funtion(x1)
        fx2 = funtion(x2)
        xn = (((x1 * fx2) - (x2 * fx1)) * 1.0) / (fx2 - fx1)

        print(f"  x{i}= {x1}  \tx{i+1}=  {x2}   \tx{i+2}=  {xn}")
        print(f"  f(x{i})= {fx1} \t f(x{i+1})= {fx2} \t f(x{i+2})=  {funtion(xn)}\n")

        if abs((x2 - x1) / x1) <= diferencia:  # CONDICION DE PARADA, CUANDO HAYA UNA RAIZ
            converge = True  # DETIENE EL CICLO
            raiz = x2  # VARIBALE QUE REPRESENTA LA RAIZ
        else:
            if math.isnan(xn):  # VALIDA SI NO ES UN NUMERO, PARA QUE CICLO PARE
                i = S  # DETIENE EL CICLO
            i += 1  # INCREMENTO DE ITERACION
            x1 = x2  # ASIGNACION DEL NUEVO X1
            x2 = xn  # ASIGNACION DEL NUEVO X2

    if converge:  # SI CONVERGE MUESTRA LA RAIZ SINO MUESTRA (NO EXISTE RAIZ)
        print(f"EXISTE RAIZ: {raiz}")
    else:
        print("NO EXISTE RAIZ")

a = -1  # VALORES DEL INTERVALO [-1,1]
b = 1
methodSecant(a, b)


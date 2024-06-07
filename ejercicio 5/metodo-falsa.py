import math

F = 70
diferencia = 0.00000000045399  # epsilon elevado a la -10

def funtion(x):
    return ((2 * x**3) - ((34.0 / 7) * (x**2)) + ((209.0 / 49) * x) - (173.0 / 343))

def mFalsaP(x1, x2):  # ALGORITMO DEL METODO DE FALSA POSICION
    converge = False
    i = 0
    print("METODO DE FALSA POSICION")
    print("VALORES INICIALES:")
    print(f"Intervalo    x1= {x1}  x2={x2}")

    while (i < F) and (not converge):  # MIENTRAS NO SE AGOTEN EL MAXIMO DE ITERACION Y LA FUNCION NO CONVERGE
        fx1 = funtion(x1)
        fx2 = funtion(x2)
        xn = x2 - (((fx2) * (x1 - x2) * 1.0) / (fx1 - fx2))

        print(f"  x{i}= {x1}  \tx{i+1}=  {x2} \tx{i+2}=  {xn}\n\n")
        print(f"  f(x{i})= {fx1} \t f(x{i+1})= {fx2} \t f(x{i+2})=  {funtion(xn)}\n")

        if abs((xn - x2) / xn) <= diferencia:  # CONDICION DE PARADA, CUANDO HAYA UNA RAIZ
            converge = True  # DETIENE EL CICLO
            raiz = xn  # VARIBALE QUE REPRESENTA LA RAIZ
        else:
            if math.isnan(xn):  # VALIDA SI NO ES UN NUMERO, PARA QEU CICLO PARE
                i = F  # DETIENE EL CICLO
            i += 1  # INCREMENTO DE ITERACION
            x2 = xn  # ASIGNACION DEL NUEVO Xn

    if converge:  # SI CONVERGE MUESTRA LA RAIZ SINO MUESTRA (NO EXISTE RAIZ)
        print(f"\nEXISTE RAIZ: {raiz}")
    else:
        print("\nNO EXISTE RAIZ")

a = -1  # VALORES DEL INTERVALO [-1,1]
b = 1
mFalsaP(a, b)

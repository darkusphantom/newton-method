import numpy as np
import math

# Definimos la función
def f(x):
    """
    Calculates the value of the function f(x) using the given input x.

    Parameters:
        x (float): The input value for the function.

    Returns:
        float: The calculated value of the function f(x).
    """

    return 1 - np.exp(-1 * ((x**2) - 12.15 * x + 36.875)) - np.exp(-1 * ((x**2) - 7.4 * x + 13.20))

# Definimos la derivada de la función
def df(x):
    """
    Calculates the derivative of a function at a given point.

    Parameters:
        x (float): The input value for which the derivative is calculated.

    Returns:
        float: The derivative of the function at the given point.
    """

    return ((-(2*x) + 12.15) * -np.exp(-1 * ((x**2) - 12.15 * x + 36.875)) + ((-(2*x) + 7.4) * -np.exp(-1 * (x**2 - 7.4 * x + 13.20))))

def methodNewton(): # ALGORITMO DEL METODO DE NEWTON
    """
    The methodNewton function implements the Newton's method algorithm to find the roots of a function.

    Parameters:
        None

    Returns:
        None

    This function takes no input parameters. It initializes the variables valorMinimo, M, diferencia, and t0 with their respective values. Then, it iterates over the range of 5 and performs the following steps for each value of t0:
        1. Calculate the value of the function f(t0) and store it in the variable v.
        2. Print the initial values of i, t0, and fx.
        3. Check if the absolute value of v is greater than or equal to valorMinimo. If true, proceed to the next step; otherwise, skip to the next iteration.
        4. Initialize the variable i to 0 and assign the value of t0 to the variable auxt0.
        5. Enter a while loop that continues until i is less than M or the function does not converge.
        6. Calculate the derivative of the function at auxt0 and store it in the variable fx.
        7. Calculate the next approximation for the root using the formula t1 = auxt0 - (v / fx) * 1.0 and store it in the variable t1.
        8. Calculate the value of the function f(t1) and store it in the variable v.
        9. Print the values of i, t1, fx, and v.
        10. Check if the absolute difference between t1 and auxt0 is less than or equal to diferencia or the absolute value of v is less than or equal to valorMinimo. If true, set the variable converge to True and assign the value of t1 to the variable raiz. Break out of the while loop. Otherwise, proceed to the next step.
        11. Check if t1 or v is NaN (not a number). If true, break out of the while loop. Otherwise, increment i by 1 and assign the value of t1 to the variable auxt0.
        12. After the while loop, check the value of converge. If true, print the message "EXISTE RAIZ: {raiz}" (where {raiz} is the value of raiz). Otherwise, print the message "NO EXISTE RAIZ".
    """
    valorMinimo = 0.0001
    M = 100
    diferencia = 0.0001
    t0 = [3.5, 3.6, 3.7, 3.8, 3.9] # CONJUNTO DE T0 A EVALUAR

    for l in range(5): # CICLO PARA OBTENER TODOS LOS T0
        v = f(t0[l])

        print("VALORES INICIALES:\n")
        print(f"\ti=0  t0= {t0[l]}  fx={v}\n")

        if abs(v) >= valorMinimo: # t0 en la funcion es mayor al valor minimo
            i = 0
            auxt0 = t0[l]
            while (i < M): # MIENTRAS NO SE AGOTEN EL MAXIMO DE ITERACION Y LA FUNCION NO CONVERGE
                # ECUACIONES PARA CONSEGUIR EL SIGUIENTE T1
                fx = df(auxt0)
                t1 = auxt0 - ((v / fx) * 1.0)
                v = f(t1)

                print(f"  i={i+1}    t1={t1}    fx={v}    f'x={fx}\n")
                if (abs(t1-auxt0) <= diferencia) or (abs(v) <= valorMinimo): # CONDICION DE PARADA, CUANDO HAYA UNA RAIZ
                    converge = True # DETIENE EL CICLO
                    raiz = t1 # VARIBALE QUE REPRESENTA LA RAIZ
                    break
                else:
                    if math.isnan(t1) or math.isnan(v): # VALIDA SI NO ES UN NUMERO, PARA QUE CICLO PARE
                        break
                    i += 1 # INCREMENTO DE ITERACION
                    auxt0 = t1 # ASIGNACION DEL NUEVO AUXT0

            if converge: # SI CONVERGE MUESTRA LA RAIZ SINO MUESTRA (NO EXISTE RAIZ)
                print(f"\nEXISTE RAIZ: {raiz}")
            else:
                print("\nNO EXISTE RAIZ")
            print("\n\n")

print("METODO DE NEWTON\n\n")
methodNewton()
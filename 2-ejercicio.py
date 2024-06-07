import math

def newton_method(k, epsilon=1e-3, max_iter=1000):
    # Definimos la función y su derivada
    def f(x):
        return math.atan((k+1)*x/2) - 1

    def df(x):
        return (k+1)/(2*(1 + ((k+1)*x/2)**2))

    # Inicializamos x en 0
    x = 0

    # Iteramos hasta alcanzar la máxima cantidad de iteraciones
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < epsilon:
            # Si la función es menor que epsilon, hemos encontrado una raíz
            return x

        # Actualizamos x usando el método de Newton
        x = x - fx/df(x)

    # Si llegamos a este punto, el método de Newton no convergió
    return None

# Probamos el método de Newton con k = 1
k = 26781816
root = newton_method(k)

if root is None:
    print("El método de Newton no convergió")
else:
    print(f"La raíz encontrada es {root}")

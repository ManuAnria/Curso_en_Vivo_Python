#Ejercicio 1
def saludo() -> None:
    print("Hola amiga!")

saludo()

#Ejercicio 2
def saludo2(nombre: str) -> None:
    print(f"Hola {nombre}!!")

saludo2("Manuel")

#Ejercicio 3
def factorial(numero: int) -> int:
    inicio = 1
    for i in range(numero):
        inicio *= i+1
    return inicio

print(factorial(5))

#Ejericio 4
def IVA(neto: float,alicuota: float =21) -> float:
    bruto = round(neto * (1+(alicuota/100)),2)
    return bruto

print(f"El importe bruto es de {IVA(100)}")

#Ejercicio 5
def area_circulo(radio: float) -> float:
    rdo_area = round(radio * 3.1416,4)
    return rdo_area

def volumen_cilindro(func: float, h: float) -> float:
    rdo_vol = round(func * 3.1416 * h,4)
    return rdo_vol

print(f"Para un radio de 5, el area de un circulo es {area_circulo(5)} y el volumen de un cilindro es {volumen_cilindro(area_circulo(5),5)}")

#Ejercicio 6
def promedio(*numeros: int) -> float:
    inicio = 0
    for i in numeros:
        inicio += i
    return round(inicio / len(numeros),2)

print(promedio(1,2,3,4,5))

#Ejercicio 7
def cuadrado(*nums:int) -> list:
    lista = []
    for i in nums:
        operacion = i**2
        lista.append(operacion)
    return lista


print(cuadrado(2, 3, 4, 5, 6, 7, 8, 9))

#Ejercicio 8
def estadistica(*muestras: int) -> dict:
    dicc = {}
    cero = 0
    desvios = 0
    for n in muestras:
        cero += n
        media = round(cero/len(muestras),2)
        desvio = (n - media) ** 2
        desvios += desvio
        varianza = round(desvios/len(muestras),2)
        desv_est = varianza ** 0.5
    dicc["Media"] = media
    dicc["Varianza"] = varianza
    dicc["Desviacion Estandar"] = desv_est
    return dicc

print(estadistica(1,2,3))

#Ejercicio 9,10 y 11 quedan para despues

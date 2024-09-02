class OperacionesAritmeticas():
    def ingresoNumeros(self):
        numero01=float(input('Ingrese sumando uno: '))
        numero02=float(input('Ingrese sumando dos: '))
        return numero01,numero02

    def suma(self,numero01,numero02):
       return numero01+numero02


if __name__ == '__main__':
    operación = OperacionesAritmeticas()
    num1, num2 = operación.ingresoNumeros()
    print(f"{num1} + {num2} = {operación.suma(num1, num2)}")

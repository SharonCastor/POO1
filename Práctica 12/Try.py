class Calculadora:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def dividir(self):
        try:
            resultado = self.numerador / self.denominador
            return f"El resultado de la división es: {resultado}"
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero."
        except TypeError:
            return "Error: Ambos valores deben ser números."
        except Exception as e:
            return f"Ocurrió un error inesperado: {e}"

if __name__ == "__main__":
    num = input("Ingresa el numerador: ")
    den = input("Ingresa el denominador: ")

    try:
        num = float(num)
        den = float(den)
        calc = Calculadora(num, den)
        print(calc.dividir())
    except ValueError:
        print("Error: Debes ingresar valores numéricos válidos.")

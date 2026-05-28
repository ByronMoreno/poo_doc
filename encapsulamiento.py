# Encapsulamiento
class CuentaBancaria:
    def __init__(self):
        self.__saldo=1000
    #Metodo para leer el saldo
    def get_saldo(self):
        print(f"El saldo de su cuenta es: {self.__saldo}")
    #Metodo para cambiar el saldo
    def set_saldo(self,nuevo_saldo):
        self.__saldo=nuevo_saldo
#Fuera de la clase
#Instanciar el objeto
cuenta = CuentaBancaria()
cuenta.get_saldo()
#Cambio del saldo
cuenta.set_saldo(200)
cuenta.get_saldo()



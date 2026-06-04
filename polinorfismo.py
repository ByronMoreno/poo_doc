class Pato:
    def volar(self):
        print("El pato vuela bajo")

class Aguila:
    def volar(self):
        print("El aguila vuela alto")

aves = [Pato(), Aguila()]

for ave in aves:
    ave.volar()

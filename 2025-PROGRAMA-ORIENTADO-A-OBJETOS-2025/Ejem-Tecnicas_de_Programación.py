class nivelJairo:
    def __init__(self, nombre, ataque, defensa, vida):
        self.nombre = nombre    # Nombre del personaje
        self.ataque = ataque    # Puntos de ataque base
        self.defensa = defensa  # Puntos de defensa
        self.vida = vida    # Puntos de vida actuales

    def atacar(self, enemigo):
        daño = max(1, self.ataque - enemigo.defensa // 2)
        enemigo.vida -= daño
        print(f"{self.nombre} ataca -> {daño} de daño a {enemigo.nombre}")

    def esta_vivo(self):
        return self.vida > 0


class Guerrero(nivelJairo):
    def __init__(self, nombre):
        super().__init__(nombre, ataque=15, defensa=10, vida=100)

    def ataque_poderoso(self, enemigo):
        daño = self.ataque * 2 - enemigo.defensa
        enemigo.vida -= daño
        print(f"{self.nombre} usa ATAQUE PODEROSO -> {daño} de daño!")


class Mago(nivelJairo):
    def __init__(self, nombre):
        super().__init__(nombre, ataque=8, defensa=5, vida=80)
        self.mana = 50

    def hechizo_fuego(self, enemigo):
        if self.mana >= 15:
            daño = self.ataque + 10
            enemigo.vida -= daño
            self.mana -= 15
            print(f"{self.nombre} lanza BOLA DE FUEGO -> {daño} de daño!")
        else:
            print("¡No tienes suficiente mana!")


# Ejemplo de uso
heroe1 = Guerrero("Jairo")
heroe2 = Mago("Felipe")

while heroe1.esta_vivo() and heroe2.esta_vivo():
    heroe1.atacar(heroe2)
    if heroe2.esta_vivo():
        heroe2.hechizo_fuego(heroe1)

if heroe1.esta_vivo():
    print(f"\n¡{heroe1.nombre} gana!")
else:
    print(f"\n¡{heroe2.nombre} gana!")
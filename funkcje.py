# energia kinetyczna, potencjalna i zasada zachowania energii


def kinetic_energy(mass, velocity):
    return (mass*velocity**2)/2


G = 6.674*10**(-11)


def potential_energy(mass1, mass2, distance):
    return (G*mass1*mass2)/distance


def conservation_of_energy(kinetic_1, potential_1, kinetic_2, potential_2):
    return 0


class Przyklad:
    oreo = "oreo"
    oreo_ile = 4


obiekt = Przyklad()
print(obiekt.oreo)
print(obiekt.oreo_ile)
obiekt.oreo = 10
print(obiekt.oreo)

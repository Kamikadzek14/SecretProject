# zasada zachowania pędu gęstość


def momentum(mass, velocity):
    return (mass*velocity)

def density(mass, volume):
    return (mass/volume)

# TO JEST ŹLE :)

def momentum_rule(mass1, mass2, velocity1, velocity2):

    if #object_1rect.colliderect(object2rect):
        if abs(object2rect.top - object_1rect.bottom) < collision_tollerance:
                velocity1[1] = -velocity1[1]
        if abs(object2rect.bottom - object_1rect.top) < collision_tollerance:
                velocity1[1] = -velocity1[1]
        if abs(object2rect.right - object_1rect.left) < collision_tollerance:
                velocity2[0] = -velocity2[0]
        if abs(object2rect.left - object_1rect.right) < collision_tollerance:
                velocity2[0] = -velocity2[0]
import numpy as np

G = 6.67430e-11

test_vector = np.array([5,0])
test_vector2 = np.array([5,7,8])

def get_magnitude(vector):
    return np.linalg.norm(vector)

#print(get_magnitude(test_vector2))

def get_unit_vector(vector):
    return vector/get_magnitude(vector)


result = get_unit_vector(test_vector2)
print(result)
print(get_magnitude(result))

def get_gravitational_force_vector(G, mass_1, mass_2, r_vector):
    distance_magnitude = get_magnitude(r_vector)
    print(distance_magnitude)
    unit_vector = get_unit_vector(r_vector)
    print(unit_vector)
    result = - G * (mass_1 * mass_2 / distance_magnitude**2)
    print(result)
    result = result * unit_vector
    print(result)
    return result

mass1 = 1200000000000000000000000000
mass2 = 200
r_vector = np.array([10,0,23])

get_gravitational_force_vector(G, mass1, mass2, r_vector)



# https://www.codewars.com/kata/get-planet-name-by-id/train/python


def get_planet_name(id):

    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"}
    return planets.get(id)


print(get_planet_name(4))
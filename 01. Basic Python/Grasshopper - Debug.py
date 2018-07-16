# https://www.codewars.com/kata/grasshopper-debug


def weather_info(temp):
    def convertToCelsius(temp):
        celsius = (temp - 32) * (5 / 9)
        return celsius

    c = convertToCelsius(temp)
    if (c > 0):
        return ("{:.1f}".format(c) + " is above freezing temperature")
    else:
        return ("{:.1f}".format(c) + " is freezing temperature")


print(weather_info(23))
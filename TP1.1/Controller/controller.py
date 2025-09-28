from Model.fichier import celsius_vers_fahrenheit, fahrenheit_vers_celsius

class ControllerConvertisseur:
    def __init__(self, vue):
        self.vue = vue

    def convertir_temperature(self, mode, valeur: float) -> str:
        if mode == "C2F":
            res = celsius_vers_fahrenheit(valeur)
            return f"{valeur:.2f} °C = {res:.2f} °F"
        else:
            res = fahrenheit_vers_celsius(valeur)
            return f"{valeur:.2f} °F = {res:.2f} °C"

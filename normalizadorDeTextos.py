from unidecode import unidecode

class NormalizadorDeNomes:
    def normalizar_string(texto):
        # Remove a acentuação e transforma em minúsculas
        texto_normalizado = unidecode(texto).lower()
        return texto_normalizado
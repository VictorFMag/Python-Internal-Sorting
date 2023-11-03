from normalizadorDeTextos import NormalizadorDeNomes

class BubbleSort:
    def bubble_sort(arr, tipo):
        n = len(arr)
        match tipo:
            case "track":
                for i in range(n):
                    for j in range(0, n - i - 1):
                        nome1_normalizado = NormalizadorDeNomes.normalizar_string(arr[j].track_name)
                        nome2_normalizado = NormalizadorDeNomes.normalizar_string(arr[j+1].track_name)
                        if nome1_normalizado > nome2_normalizado:
                            aux = arr[j]
                            arr[j] = arr[j+1]
                            arr[j+1] = aux
            case "artist":
                for i in range(n):
                    for j in range(0, n - i - 1):
                        nome1_normalizado = NormalizadorDeNomes.normalizar_string(arr[j].artist_name)
                        nome2_normalizado = NormalizadorDeNomes.normalizar_string(arr[j+1].artist_name)
                        if nome1_normalizado > nome2_normalizado:
                            aux = arr[j]
                            arr[j] = arr[j+1]
                            arr[j+1] = aux
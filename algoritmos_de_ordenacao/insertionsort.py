from normalizadorDeTextos import NormalizadorDeNomes

class InsertionSort:
    def insertion_sort(arr, tipo):
        n = len(arr)
        match tipo:
            case "track":
                for i in range(1, n):
                    key = arr[i]
                    j = i - 1
                    nome1_normalizado = NormalizadorDeNomes.normalizar_string(key.track_name)
                    nome2_normalizado = NormalizadorDeNomes.normalizar_string(arr[j].track_name)
                    while j >= 0 and nome1_normalizado < nome2_normalizado:
                        arr[j + 1] = arr[j]
                        j -= 1
                    arr[j + 1] = key
            case "artist":
                for i in range(1, n):
                    key = arr[i]
                    j = i - 1
                    nome1_normalizado = NormalizadorDeNomes.normalizar_string(key.artist_name)
                    nome2_normalizado = NormalizadorDeNomes.normalizar_string(arr[j].artist_name)
                    while j >= 0 and nome1_normalizado < nome2_normalizado:
                        arr[j + 1] = arr[j]
                        j -= 1
                    arr[j + 1] = key
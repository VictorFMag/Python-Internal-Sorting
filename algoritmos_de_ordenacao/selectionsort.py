from normalizadorDeTextos import NormalizadorDeNomes

class SelectionSort:
    def selection_sort(arr, tipo):
        n = len(arr)
        match tipo:
            case "track":
                for i in range(n):
                    min_idx = i
                    for j in range(i + 1, n):
                        nome1_normalizado = NormalizadorDeNomes.normalizar_string(arr[j].track_name)
                        nome2_normalizado = NormalizadorDeNomes.normalizar_string(arr[min_idx].track_name)
                        if nome1_normalizado < nome2_normalizado:
                            min_idx = j
                    arr[i], arr[min_idx] = arr[min_idx], arr[i]
            case "artist":
                for i in range(n):
                    min_idx = i
                    for j in range(i + 1, n):
                        nome1_normalizado = NormalizadorDeNomes.normalizar_string(arr[j].artist_name)
                        nome2_normalizado = NormalizadorDeNomes.normalizar_string(arr[min_idx].artist_name)
                        if nome1_normalizado < nome2_normalizado:
                            min_idx = j
                    arr[i], arr[min_idx] = arr[min_idx], arr[i]
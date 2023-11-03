from normalizadorDeTextos import NormalizadorDeNomes

class ShellSort:
    def shell_sort(arr, tipo):
        n = len(arr)
        match tipo:
            case "track":
                gap = n // 3
                while gap > 0:
                    for i in range(gap, n):
                        temp = arr[i]
                        j = i
                        nome1_normalizado = NormalizadorDeNomes.normalizar_string(arr[j-gap].track_name)
                        nome2_normalizado = NormalizadorDeNomes.normalizar_string(temp.track_name)
                        while j >= gap and nome1_normalizado > nome2_normalizado:
                            arr[j] = arr[j - gap]
                            j -= gap
                        arr[j] = temp
                    gap //= 2
            case "artist":
                gap = n // 3
                while gap > 0:
                    for i in range(gap, n):
                        temp = arr[i]
                        j = i
                        nome1_normalizado = NormalizadorDeNomes.normalizar_string(arr[j-gap].artist_name)
                        nome2_normalizado = NormalizadorDeNomes.normalizar_string(temp.artist_name)
                        while j >= gap and nome1_normalizado > nome2_normalizado:
                            arr[j] = arr[j - gap]
                            j -= gap
                        arr[j] = temp
                    gap //= 2
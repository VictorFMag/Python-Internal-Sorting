from normalizadorDeTextos import NormalizadorDeNomes

class QuickSort:
    def quick_sort(self, arr, tipo):
        match tipo:
            case "track":
                if len(arr) <= 1:
                    return arr
                meio = len(arr)//2
                pivot = arr[meio]
                left = [x for x in arr[:meio] + arr[meio+1:] if NormalizadorDeNomes.normalizar_string(x.track_name) <= NormalizadorDeNomes.normalizar_string(pivot.track_name)]
                right = [x for x in arr[:meio] + arr[meio+1:] if NormalizadorDeNomes.normalizar_string(x.track_name) > NormalizadorDeNomes.normalizar_string(pivot.track_name)]

                return self.quick_sort(self, left, tipo) + [pivot] + self.quick_sort(self, right, tipo)
            case "artist":
                if len(arr) <= 1:
                    return arr
                meio = len(arr)//2
                pivot = arr[meio]
                left = [x for x in arr[:meio] + arr[meio+1:] if NormalizadorDeNomes.normalizar_string(x.artist_name) <= NormalizadorDeNomes.normalizar_string(pivot.track_name)]
                right = [x for x in arr[:meio] + arr[meio+1:] if NormalizadorDeNomes.normalizar_string(x.artist_name) > NormalizadorDeNomes.normalizar_string(pivot.track_name)]
                return self.quick_sort(self, left, tipo) + [pivot] + self.quick_sort(self, right, tipo)
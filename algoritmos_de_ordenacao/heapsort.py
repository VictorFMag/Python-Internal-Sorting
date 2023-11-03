from normalizadorDeTextos import NormalizadorDeNomes

class HeapSort:
    def heapify(self, arr, n, i, tipo):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        match tipo:
            case "track":
                if left < n and NormalizadorDeNomes.normalizar_string(arr[left].track_name) > NormalizadorDeNomes.normalizar_string(arr[largest].track_name):
                    largest = left

                if right < n and NormalizadorDeNomes.normalizar_string(arr[right].track_name) > NormalizadorDeNomes.normalizar_string(arr[largest].track_name):
                    largest = right

                if largest != i:
                    arr[i], arr[largest] = arr[largest], arr[i]
                    self.heapify(self, arr, n, largest, tipo)
            case "artist":
                if left < n and NormalizadorDeNomes.normalizar_string(arr[left].artist_name) > NormalizadorDeNomes.normalizar_string(arr[largest].artist_name):
                    largest = left

                if right < n and NormalizadorDeNomes.normalizar_string(arr[right].artist_name) > NormalizadorDeNomes.normalizar_string(arr[largest].artist_name):
                    largest = right

                if largest != i:
                    arr[i], arr[largest] = arr[largest], arr[i]
                    self.heapify(self, arr, n, largest, tipo)

    def heap_sort(self, arr, tipo):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(self, arr, n, i, tipo)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(self, arr, i, 0, tipo)
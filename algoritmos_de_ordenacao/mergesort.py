from normalizadorDeTextos import NormalizadorDeNomes

class MergeSort:
    def merge_sort(self, arr, tipo):
        match tipo:
            case "track":
                if len(arr) > 1:
                    mid = len(arr) // 2
                    left_half = arr[:mid]
                    right_half = arr[mid:]

                    self.merge_sort(self, left_half, tipo)
                    self.merge_sort(self, right_half, tipo)

                    i = j = k = 0

                    while i < len(left_half) and j < len(right_half):
                        nome1_normalizado = NormalizadorDeNomes.normalizar_string(left_half[i].track_name)
                        nome2_normalizado = NormalizadorDeNomes.normalizar_string(right_half[j].track_name)
                        if nome1_normalizado < nome2_normalizado:
                            arr[k] = left_half[i]
                            i += 1
                        else:
                            arr[k] = right_half[j]
                            j += 1
                        k += 1

                    while i < len(left_half):
                        arr[k] = left_half[i]
                        i += 1
                        k += 1

                    while j < len(right_half):
                        arr[k] = right_half[j]
                        j += 1
                        k += 1
            case "artist":
                if len(arr) > 1:
                    mid = len(arr) // 2
                    left_half = arr[:mid]
                    right_half = arr[mid:]

                    self.merge_sort(self, left_half, tipo)
                    self.merge_sort(self, right_half, tipo)

                    i = j = k = 0

                    while i < len(left_half) and j < len(right_half):
                        nome1_normalizado = NormalizadorDeNomes.normalizar_string(left_half[i].artist_name)
                        nome2_normalizado = NormalizadorDeNomes.normalizar_string(right_half[j].artist_name)
                        if nome1_normalizado < nome2_normalizado:
                            arr[k] = left_half[i]
                            i += 1
                        else:
                            arr[k] = right_half[j]
                            j += 1
                        k += 1

                    while i < len(left_half):
                        arr[k] = left_half[i]
                        i += 1
                        k += 1

                    while j < len(right_half):
                        arr[k] = right_half[j]
                        j += 1
                        k += 1
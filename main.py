from leitorDeArquivo import LeitorDeArquivo
from algoritmos_de_ordenacao.selectionsort import SelectionSort
from algoritmos_de_ordenacao.insertionsort import InsertionSort
from algoritmos_de_ordenacao.shellsort import ShellSort
from algoritmos_de_ordenacao.quicksort import QuickSort
from algoritmos_de_ordenacao.bubblesort import BubbleSort
from algoritmos_de_ordenacao.mergesort import MergeSort
from algoritmos_de_ordenacao.heapsort import HeapSort

def main():
    arrOriginal = []
    LeitorDeArquivo.lerArquivo(arrOriginal)

    arr = list(arrOriginal)

    escolha = 0
    while escolha != 15:
        print("Escolha um tipo de ordenação:")
        print("1 -> SelectionSort por nome da música")
        print("2 -> SelectionSort por nome dos autores")
        print("3 -> InsertionSort por nome da música")
        print("4 -> InsertionSort por nome dos autores")
        print("5 -> ShellSort por nome da música")
        print("6 -> ShellSort por nome dos autores")
        print("7 -> QuickSort por nome da música")
        print("8 -> QuickSort por nome dos autores")
        print("9 -> BubbleSort por nome da música")
        print("10 -> BubbleSort por nome dos autores")
        print("11 -> MergeSort por nome da música")
        print("12 -> MergeSort por nome dos autores")
        print("13 -> HeapSort por nome da música")
        print("14 -> HeapSort por nome dos autores")

        print("\n15 -> Sair")

        escolha = int(input("Sua escolha: "))

        match escolha:
            case 1:
                SelectionSort.selection_sort(arr, "track")
                printSorted(arr)
            case 2:
                SelectionSort.selection_sort(arr, "artist")
                printSorted(arr)
            case 3:
                InsertionSort.insertion_sort(arr, "track")
                printSorted(arr)
            case 4:
                InsertionSort.insertion_sort(arr, "artist")
                printSorted(arr)
            case 5:
                ShellSort.shell_sort(arr, "track")
                printSorted(arr)
            case 6:
                ShellSort.shell_sort(arr, "artist")
                printSorted(arr)
            case 7:
                arr = QuickSort.quick_sort(QuickSort, arr, "track")
                printSorted(arr)
            case 8:
                arr = QuickSort.quick_sort(QuickSort, arr, "artist")
                printSorted(arr)
            case 9:
                BubbleSort.bubble_sort(arr, "track")
                printSorted(arr)
            case 10:
                BubbleSort.bubble_sort(arr, "artist")
                printSorted(arr)
            case 11:
                MergeSort.merge_sort(MergeSort, arr, "track")
                printSorted(arr)
            case 12:
                MergeSort.merge_sort(MergeSort, arr, "artist")
                printSorted(arr)
            case 13:
                HeapSort.heap_sort(HeapSort, arr, "track")
                printSorted(arr)
            case 14:
                HeapSort.heap_sort(HeapSort, arr, "artist")
                printSorted(arr)
            case 15:
                print("Sistema encerrado!\n")
            case _:
                print("Escolha inválida!\n")

def printSorted(arr):
    for musica in arr:
        print ("Track_name: ",musica.track_name)
        print ("Artist_name: ",musica.artist_name+"\n")

main()
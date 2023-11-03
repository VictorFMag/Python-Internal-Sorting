from musica import Musica

class LeitorDeArquivo:

    def lerArquivo(arr):
        # Abrir o arquivo em modo de leitura
        arquivo = open("./spotify-2023.csv", "r")

        # Ler o conteúdo do arquivo linha por linha
        linha = arquivo.readline()
        while linha:
            linha = linha.replace(", ", "#$%")
            linhaFormatada = linha.split(",")
            linhaFormatada[1].replace("#$%", ", ")

            if len(linhaFormatada) >= 2:
                musica = Musica(linhaFormatada[0], linhaFormatada[1], linhaFormatada[2], linhaFormatada[3], linhaFormatada[4], linhaFormatada[5],
                 linhaFormatada[6], linhaFormatada[7], linhaFormatada[8], linhaFormatada[9], linhaFormatada[10], linhaFormatada[11], linhaFormatada[12], 
            linhaFormatada[13], linhaFormatada[14], linhaFormatada[15], linhaFormatada[16], linhaFormatada[17], linhaFormatada[18], linhaFormatada[19], 
            linhaFormatada[20], linhaFormatada[21], linhaFormatada[22], linhaFormatada[23])
                arr.append(musica)

            linha = arquivo.readline()
        
        arquivo.close()
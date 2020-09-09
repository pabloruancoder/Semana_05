def num_int(inicio,fim):
    # variavel numeros que irá armazenar a sequência de número em string
    numeros = ""
    # Usando laço For para impressão dos números
    for num in range(inicio,fim + 1):
        # incrementação da variavel números que irá rceber o valores de num em string  e concatenar a quebra de linha
        numeros += str(num) + '\n'
    # retornando os números em formaato de string
    return numeros.strip()

# função princinpal
def main():
    # os dados que irá fazer o laço for funcionar com inicio e fim
    inicio = 1
    fim = 50
    # saídas dos dados
    print(num_int(inicio, fim))

if __name__=='__main__':
    main()
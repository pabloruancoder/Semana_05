def cont_impar_par(inicio,fim):
    # variavel maior que recebe como maior número o inicio da sequência, pois é a primeira entrada de dados
    maior = inicio
    # laço de repetição
    for c in range(inicio,fim):
        # entrada de dados
        num = int(input(f'Digite o {c + 1} número: '))
        # condiçao se o número for maior que o inicio, será substituido sempre pelo maior digitado
        if num > maior:
            maior  = num
    # retorno do maior número
    return f'o maior número digitado foi {maior}'

# função principal
def main():
    # os dados que irá fazer o laço for funcionar com inicio e fim
    inicio = 0
    fim = 100
    # saída dos dados
    print(cont_impar_par(inicio,fim))

if __name__ == '__main__':
    main()
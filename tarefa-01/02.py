def cont_impar_par(inicio,fim):
    # contadores par e impar
    contpar = 0
    contimpar = 0
    # laço que irá rodar 100 vezes
    for c in range (inicio,fim):
        # entrada de dados
        num = int(input(f'Digite o {c + 1} número: '))
        # verificação se os numeros forem Par
        if num % 2 == 0:
            # irá somar todos os números que forem par e armazenar na variavel contapar
            contpar += 1
        else:
            # irá somar todos os números que forem par e armazenar na variavel contapar
            contimpar +=1
    # retorno da quantidade de números par e impar
    return f'Todos os números digitados tem {contpar} pares e {contimpar} números impares.'

# funçao principal
def main():
    # os dados que irá fazer o laço for funcionar com inicio e fim
    inicio = 0
    fim = 100

    # saída de dados
    print(cont_impar_par(inicio,fim))

if __name__ == '__main__':
    main()
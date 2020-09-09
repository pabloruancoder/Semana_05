def cont_impar_par(inicio,fim):
    # variavel soma que vai receber a soma de todos os números 
    soma = 0
    # laço de repetição
    for c in range (inicio,fim):
        # entrada de dados
        num = int(input(f'Digite o {c + 1} número: '))
        # armazenamento da soma de todos os números
        soma += num

    # retorno da media dos números
    return f'média de todos os números é {soma / fim:.2f}'
# funçao principal
def main():
    # os dados que irá fazer o laço for funcionar com inicio e fim
    inicio = 0
    fim = 100
    # saída dos dados
    print(cont_impar_par(inicio,fim))

if __name__ == '__main__':
    main()
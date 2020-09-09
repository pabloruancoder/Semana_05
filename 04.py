def contador(inicio,fim,quant_numeros_a_pular):
    # variavel sequencia que irá armazenar a sequência de número em string
    sequencia = ''
    # Usando laço For para impressão dos números
    for num in range(inicio, fim, quant_numeros_a_pular):
        # incrementação da variavel sequência que irá rceber o valores de num em string  e concatenar com a ','
        sequencia += str(num) + ', '
    # retorno da sequência  com a variavel que concatenar com o '.' no final dessa sequência
    return f'{sequencia}{fim}' + "."

# funçao principal
def main():
    # os dados que irá fazer o laço for funcionar com inicio e fim
    inicio = 10
    fim = 1000
    quant_a_pular = 10
    # saída dos dados
    print(contador(inicio,fim,quant_a_pular))

if __name__ == '__main__':
    main()
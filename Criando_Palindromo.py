# Solicite que o usuario digite uma frase
frase = str(input("Digite uma Frase: ")).lower()

# Remove o espaços da frase e armazena em outra variavel
frase_sem_espaco = frase.replace(" ","")

# Cria uma variavel para armazena a versão invertida
frase_invertida = ''

# Loop for para percorre a frase sem espaços de trás para frente
for i in range(len(frase_sem_espaco) -1, -1, -1):
    # Adiciona cada caractere da frase sem espaços a variavel invertida
    frase_invertida += frase_sem_espaco[i]

# Compara a frase sem espaços com a frase invertida e imprime a mensagem se e ou não palindromo
if frase_sem_espaco == frase_invertida:
    print(f"A frase {frase_sem_espaco} e Um Palindromo {frase_invertida}")
else:
    print(f"A frase {frase_sem_espaco} Não e Um Palindromo {frase_invertida}")

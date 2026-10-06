# "parâmetros"
NOTA_MIN = 0
NOTA_MAX = 10
QTD_NOTAS = 3
MEDIA_APROVACAO = 6

# uma função para tratar possíveis erros na digitação da nota
def ler_nota(mensagem):
    """Pede uma nota até receber uma válida e a retorna."""
    while True:
        texto = input(mensagem)
        try:
            nota = float(texto)          # o try protege só a conversão
        except ValueError:
            print("Entrada inválida: digite um número (ponto separador decimal).")
            continue                     # pula o resto do while e volta ao início
        if NOTA_MIN <= nota <= NOTA_MAX:
            return nota                  # única saída: nota aceita
        print(f"A nota deve estar entre {NOTA_MIN} e {NOTA_MAX}.")


aluno = input("Nome do aluno: ").strip()        # tira espaços acidentais
notas = []

for n in range(1, QTD_NOTAS + 1):        # +1 pois se não não pediria a última nota
    notas.append(ler_nota(f"{n}ª nota do aluno: "))

# sum soma todas as notas digitadas, e len(ght) divide pela quantidade de notas
media = sum(notas) / len(notas)      
if media >= MEDIA_APROVACAO:
    print(f"{aluno} aprovado(a) com média de {media:.2f}!")
else:
    print(f"{aluno} reprovado(a) com média de {media:.2f}.")
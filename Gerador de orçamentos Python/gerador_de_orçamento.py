# Script de automação em Python
# Autor: Kelven Patrick Novaes Barbosa
# Data: 11-08-2024
# Descrição: esse escript de automação feito em python gera um orçamento em PDF.

# importar a biblioteca "fpdf"
from fpdf import FPDF

# armazena os dados de imput em variaveis locais
projeto = input("Descrição do projeto: ")
horas_previstas = input("Quantidade de horas previstas: ")
valor_hora = input("Valor da hora trabalhada: ")
prazo = input("Prazo estimado: ")

# converte "string" em "inteiro" e efetua o calculo matemático
valor_total = int(horas_previstas) * int(valor_hora)

# variavel PDF
pdf = FPDF()

# adiciona a vareavel a pagina
pdf.add_page()

# define a fonte e a poseição do texto no PDF
pdf.set_font("Arial")
pdf.image("template.png", x=0, y=0)

# inserir os dados no arquivo de PDF
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_previstas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

# exporta o orçamento já finalizado
pdf.output("Orçamento.pdf")

# exibe uma mensagem quando o processo é comcluido
print("Orçamento gerado com sucesso!")


# Fim do Script.

#inicio
print("Bem vindo à Calculadora de KW/h da sua geladeira!")

#variaveis
marca = input("Qual é a marca da sua geladeira?")
potencia = int (input("Qual é a potência dela em Watts?"))
horas_dia = int (input("Quantas horas ela fica ligada no dia, em média?"))

#calculo
kwh = float (potencia * horas_dia * 30) / 1000
valor = float (kwh * 0.7)

#final
print(f"A sua {marca} gasta {kwh:.1f}KW/h, custando R${valor:.2f}.")







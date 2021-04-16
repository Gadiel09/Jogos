import random
import time
print("""\033[1m			ROLE OS DADOS		

• Instruções:
	- - > Role os dados quantas vezes quiser
	- - > O jogador ganha caso  os dados dele seja maior do que os do computador
	- - > Quem alcançar o placar definido primeiro vence
	\033[m""")
	

placar = int(input("\n • Qual o Placar Limite, você deseja ? : "))
print("\n"*2)
jog = 0
pc= 0	
while True:
	pergunta = " "
	jogador = random.randint(1,6)
	comp= random.randint(1,6)
	print("\033[1;36m  • Analisando resultados... \033[m")
	time.sleep(0.7)
	print(f"\033[1;33m \n - - - > Resultado : Jogador = {jogador} x Computador = {comp} \033[m")
	if jogador > comp:
		jog +=1
		print("\n \033[1;32m - - - > Jogador venceu\033[m ")
		if  jog == placar:
			break
	elif jogador < comp:
		pc +=1
		print("\033[1;35m\n - - - > Computador venceu\033[m")
		if pc == placar:
		 	break
	else:
		print("\n - - - > Empate")
	print(f"\n		PLACAR : [ J - {jog} x C - {pc} ]")
	print("___"*25,"\n")	
	while pergunta not in "SsNn":
		pergunta = str(input(" \n- - - > Deseja Jogar Novamnete ? [ S/ N] : "))
		print("..."*15)
	if pergunta in "Nn":
		print(f"\n		PLACAR : [ J - {jog} x C - {pc} ]")
		break
print(f"\n\033[1;36;m		PLACAR FINAL :  [ J - {jog} x C - {pc} ]\033[m")	

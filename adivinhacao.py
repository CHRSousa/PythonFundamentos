#Author: @CHRSousa
#Data: 20/10/2020
#Programa: Jogo de adivinhação para estudo da linguagem python

import random
def jogar():
	print("*********************************")
	print("Bem vindo ao jogo de Adivinhação!")
	print("*********************************")

	numero_secreto = random.randrange(1,101)

	tentativas = 0
	nivel = 0
	niveis = [1,2,3]
	pontos = 1000

	#Configuração da partida
	while nivel not in niveis:
		try:
			print("Qual nível de dificuldade?")
			print("(1) Fácil   (2) Médio   (3) Difícil")
			nivel = int(input("Informe o nível que deseja jogar:"))

			if(nivel == 1):
				tentativas = 10
			elif(nivel == 2):
				tentativas = 5
			elif(nivel == 3):
				tentativas = 3
			else:
				print('Por favor, escolha um nível válido.')
		except:
			print('Por favor, escolha um nível válido.')
			continue



	#partida
	rodada = 1
	while (rodada <= tentativas):

		print ("Tentativa {} de {}".format(rodada, tentativas))
		#print('Sua pontuação atual é de {} pontos'.format(pontos))
		chute_str = input('Digite um número inteiro entre 1 e 100: ')

		try:
			print('Você digitou ', chute_str)
			chute = int(chute_str)
		except:
			print('Por favor, informe um número válido.')
			continue	

		if (chute < 1 or chute > 100):
			print('Você deve digitar um número inteiro entre 1 e 100.')
			continue

		acertou = chute == numero_secreto
		if acertou:
			print('Você acertou e fez {} pontos!'.format(pontos))
			break		
		else:
			if chute > numero_secreto:
				print('Você errou! O seu chute foi maior do que o número secreto!')	
				pontos = pontos - (chute - numero_secreto)

			else:
				print('Você errou! O seu chute foi menor do que o número secreto!')	
				pontos = pontos - (numero_secreto - chute)

			if (rodada == tentativas):
				print('O número secreto era', numero_secreto)



			rodada += 1
	print("   ")
	print("************")
	print("Fim do jogo!")
	print("************")

# Executa o jogo diretamente quando o arquivo é chamado
if (__name__ == '__main__'):
	jogar()
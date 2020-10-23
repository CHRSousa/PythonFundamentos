#Author: @CHRSousa
#Data: 20/10/2020
#Programa: Seleção de Jogos

import forca
import adivinhacao

def escolhe_jogo():
	jogos = [1, 2]
	jogo = 0
	#Configuração da partida
	while jogo not in jogos:
		try:
			print("*********************************")
			print("**Qual jogo você deseja jogar?***")
			print("*********************************")
			print("(1) Forca   (2) Adivinhação   (3) Sair")
			jogo = int(input("Seleção: "))

			if(jogo == 1):
				print("Jogando Forca...")
				forca.jogar()
				jogo = 0

			elif(jogo == 2):
				print("Jogando Advinhação...")
				adivinhacao.jogar()
				jogo = 0

			elif(jogo == 3):
				print("Tchau!")
				break
			else:
				print('Por favor, escolha uma das opções acima.')
		except:
			print('Por favor, escolha uma das opções acima.')
			continue

# Executa o jogo diretamente quando o arquivo é chamado
if (__name__ == '__main__'):
	escolhe_jogo()
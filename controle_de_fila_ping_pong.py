print("+---------------------------------------+")
print("|                                       |")
print("|CONTROLE DE JOGADORES DE TÊNIS DE MESA |")
print("|                                       |")
print("+---------------------------------------+")
numero_jogadores = int(input("Digite o número de Jogadores iniciais: "))
contador1 = 0
lista_jogadores = [] #cria lista de jogadores vazia
while contador1 < numero_jogadores: #vai definir a repetição de pedir os nomes de cada jogador
	jogador = input("Insira o nome do jogador %i: "%(contador1+1))
	lista_jogadores.append(jogador)
	contador1 += 1
while True: #Cadeia de repetição de perguntas
     print("\nExistem %d jogadores na espera" % len(lista_jogadores)) #quantidade de jogadores esperando
     print("\n\n\n\n#######################")
     print("# Lista de Jogadores: #")
     print("#######################\n\n\n\n\n\n\n")
     for player in lista_jogadores: #lista de jogadores na vertical
     	print(player)
     print("\n\n\n\n\n\n\nDigite F para adicionar um jogador ao fim da fila\nDigite T para terminar uma partida\nDigite S para sair.")
     print("+---------------------------+")
     operação = input("|  Operação (F, T ou S): ")
     print("+---------------------------+")
     if operação == "T":
         if(len(lista_jogadores))>0:
               finalizado = lista_jogadores.pop(0)#RETIRA O PRIMEIRO JOGADOR/ JOGADOR 0
               print("\n\nJogador %s terminou a partida" % finalizado)
         else:
               print("\n\n\n=======>Fila vazia! Ninguém para Jogar.<=======\n\n\n")
     elif operação == "F":
     	 jogadornovo = input("Insira o nome do novo jogador: ")
     	 lista_jogadores.append(jogadornovo)#ADICIONA UM JOGADOR AO FINAL DA FILA
     elif operação == "S":
     	print("\n\nDeveloped by Pedro Cunha")
     	print("email: pedrokunhapimenta1234@gmail.com")
     	print('''
    ____  ____      _________          ____________  ____      __
   / __ \/ __ \____/__  / __ \_____   / ____/ / __ \/ __ \____/ /
  / / / / / / / ___/ / / / / / ___/  / /_  / / / / / / / / __  / 
 / /_/ / /_/ / /__  / / /_/ / /     / __/ / / /_/ / /_/ / /_/ /  
/_____/\____/\___/ /_/\____/_/     /_/   /_/\____/\____/\__,_/   
                                                                 
	                  @@@
	                  @@@
	                   @@@                       D 0 C 7 0 R
	                   @@@
	           @@@@@@@@@@@@@@@@@@@@@@         F L 0 0 D
	         @@@@@@@@@@@@@@@@@@@@@@@@@@
	       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	     @@@@@@@@ @@@@@@@@@@@@@@@@ @@@@@@@@
	   @@@@@@@@@   @@@@@@@@@@@@@@   @@@@@@@@@
	 @@@@@@@@@@     @@@@@@@@@@@@     @@@@@@@@@@
	@@@@@@@@@@       @@@@  @@@@       @@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@
	 @@@@@@@@  @@ @@ @@ @@ @@ @@ @@ @  @@@@@@@@
	   @@@@@@@                        @@@@@@@
	     @@@@@@  @@ @@ @@ @@ @@ @@ @ @@@@@@
	       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	         @@@@@@@@@@@@@@@@@@@@@@@@@@
	           @@@@@@@@@@@@@@@@@@@@@@''')
     	break
     else:
         print("\n\n********Operação inválida! Digite apenas F, T ou S!********")
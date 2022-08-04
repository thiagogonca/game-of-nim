# NIM GAME - made by thiagogonca :D

# é tal que n_atual - pc_retira = maior multiplo possível de m+1 e que ainda é menor que n_atual

# Given the current n_pieces 'n_atual' the alogitirhm removes 1 by 1 so it finds the (m+1) 
# multiplicity (which will be greater always)
#  Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um. 
#  Quem tirar as últimas peças possíveis ganha o jogo.

def escolha_modalidade():

    print("Bem vindo ao jogo do NIM! Escolha: ")
    print()
    print("1- para jogar uma partida isolada")
    print("2- para jogar um campeonato")
    print()

    digitou_correto = False
    while not digitou_correto:
        modalidade = int(input())

        if modalidade == 1:
            print("Você escolheu uma partida isolada!")
            digitou_correto = True
        else:
            if modalidade == 2:
                print("Você escolheu um campeonato!")
                digitou_correto = True
            else:
                print("O dígito informado deve ser 1 ou 2")
    return modalidade

def computador_escolhe_jogada(n,m):    

    if n > (m+1) and n % (m+1) != 0: # qnd n for maior que o menor múltiplo possível (E NÃO FOR MULTIPLO DIRETO DE M+1)
        
        achou = False
        n_temp = n
        while not achou:
            n_temp = n_temp -1 #afinal o pc tem q tirar pelo menos 1 peça, ent já começa com n_temp-1
            if n_temp % (m+1)== 0:
                n_restante = n_temp
                achou = True

        pc_retira = n - n_restante  
    else:
        if n > m:
            pc_retira = m     # Here is the computer lost game scenario
        else:                 # Only when n<=m, the computer removes the remaining pieces
            pc_retira = n    

    print("O computador tirou",pc_retira,"peça(s)")
    return pc_retira

def usuario_escolhe_jogada (n,m): # o n vai constantemente atualizando para o n_atual

    valido = False
    while not valido:
        usuario_retira = int(input("Quantas peças você vai tirar?: "))

        if (usuario_retira <= m) and (usuario_retira <= n) and (usuario_retira >= 1 ): # o jogador só pode tirar até m peças se n>m e até n peças se m>n
            print("Você tirou",usuario_retira,"peça(s)")
            valido = True
        else:
            print("Oops! Jogada inválida! Tente de novo.")

    return usuario_retira

def partida (): 
    n = int(input("Total de peças iniciais: "))
    m = int(input("Limite de peças por jogada: "))

    # when n has m+1 multiplicity the player begins
    if n % (m+1) == 0:
        print("Você começa!")
        print()
        vez = True # True means player's turn

    #otherwise computer begins
    else:
        print()
        print("O PC começa!")
        print()
        vez= False # False for computer turn
        
    peças=n

    while not (peças == 0) : #enquanto n zerar o número de peças
        
        if vez == True:
            peças = peças - usuario_escolhe_jogada(peças,m)
            vez = False
        else:
            peças = peças - computador_escolhe_jogada(peças,m)
            vez = True

        print("Agora resta(m)",peças,"peça(s) no tabuleiro.")
        print()

        if peças == 0 :
            venceu = not vez #como inverte a chave de quem jogou, a cada rodada, pra saber qm venceu, precisa inverter dnv 

    if venceu :
        print("Fim do jogo! você ganhou!")
    else :
        print("Fim do jogo! O computador ganhou!")


partida()






    
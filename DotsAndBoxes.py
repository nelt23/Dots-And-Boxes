
#Dots And Boxes

# Isto significa system exit
import sys
# Para escolher as coordenadas aleatoriamente
import random

# NOTAS IMPORTANTES
# Numa funçao quando se passa valores pelos parametros pode acontecer 2 coisas:
    # Se for um Integer (Valor inteiro) é passado uma copia do valor, ou seja se alteramos o valor dentro da funçao ele nao vai ser alterado fora da funçao
    # Se for um List (Lista) (seja unidimensional ou bidimensional) é passada o endereço da lista, quer isto dizer que se a lista for alterada dentro da funçao tambem fica alterada fora da funçao

# Menu Principal
def Main(Matriz,X1,Y1,X2,Y2,*ListTwoDimensionsSquaresMadePlayersWin):

    print("Escolha uma das seguintes opções:")
    print("0 - Exit")
    print("1 - Player vs Player")
    print("2 - Resume Game")
    print("3 - Player vs Computer")

    # Opçao introduzida pelo user
    ValueInput = int(input("Opção ? "))

    # Caso o user introuduza um valor mal
    while ValueInput < 0 or ValueInput > 3:
        print("A opção introduzida é invalida tente novamente")
        ValueInput = int(input("Opção ? "))

    if ValueInput == 0:
        print("A sair")
        sys.exit()
    elif ValueInput == 1:
        PLayerVsPlayer()
    elif ValueInput == 2:
        ResumeGame(Matriz,X1,Y1,X2,Y2,*ListTwoDimensionsSquaresMadePlayersWin)
    elif ValueInput == 3:
        PlayerVSComputer()


# Funçoes Principais

# 1
def PLayerVsPlayer():

    print("\nGrid dimension? (lines, columns)")
    Lines = int(input("linhas -> "))
    Columns = int(input("colunas -> "))
    print ("(%d , %d)" % (Lines,Columns))

    # Matriz Limpa
    CleanMatriz(Lines,Columns)

    # Numero do jogador vai variar entre 1 e 2
    Player = 1

    # listas que vao conter as coordenadas dos traços da matriz
    X1 = []
    Y1 = []
    X2 = []
    Y2 = []
    
    # é necessario criar fora da funçao pois os valores do player tao sempre a variar
    ListTwoDimensionsSquaresMadePlayersWin = [[0 for x in range(Columns-1)] for y in range(Lines-1)]

    # Inicializar a 0
    l = 0
    for l in range(Lines-1):

        c = 0
        for c in range(Columns-1):
            ListTwoDimensionsSquaresMadePlayersWin[l][c] = 0


    # Onde vao ser introduzidas as coordenadas dos traços
    while True:
        Player = AddNewLine(Player,Lines,Columns,X1,Y1,X2,Y2,*ListTwoDimensionsSquaresMadePlayersWin)


# 2
def ResumeGame(MatrizF,X1F,Y1F,X2F,Y2F,*ListTwoDimensionsSquaresMadePlayersWin):

    # matriz com 0 linhas e 0 colunas nao se consegue fazer pedese ao user para criar uma
    # Linhas               Colunas
    if ((MatrizF[0] == 0) & (Matriz[1] == 0)):

        print("\nGrid dimension? (lines, columns)")
        Lines = int(input("linhas -> "))
        Columns = int(input("colunas -> "))
        print ("(%d , %d)" % (Lines,Columns))

        MatrizF[0] = Lines
        MatrizF[1] = Columns

        # é necessario criar fora da funçao pois os valores do player tao sempre a variar
        ListTwoDimensionsSquaresMadePlayersWin = [[0 for x in range(Columns-1)] for y in range(Lines-1)]

        # Inicializar a 0
        l = 0
        for l in range(Lines-1):

            c = 0
            for c in range(Columns-1):
                ListTwoDimensionsSquaresMadePlayersWin[l][c] = 0

        # Matriz Limpa
        CleanMatriz(Lines,Columns)

    # Caso o ja exista matriz mostra-la
    else:

        Lines = MatrizF[0]
        Columns = MatrizF[1]

        # https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
        # Listas (Lines) Elementos (Columns)
        ListTwoDimensionsHorizontal = [[0 for x in range(Columns)] for y in range(Lines)]
        ListTwoDimensionsVertical = [[0 for x in range(Columns)] for y in range(Lines)]

        # Adicionar a listas Horizontal e Vertical os valores ja presentes na Matriz
        # https://stackoverflow.com/questions/48814875/missing-1-required-keyword-only-argument
        AddToHorizontalAndVerticalList(Lines,Columns,X1,Y1,X2,Y2,*ListTwoDimensionsHorizontal,ListTwoDimensionsVertical=ListTwoDimensionsVertical)

        # Testar Horizontal Matriz
        TestHorizontal(Lines,Columns,*ListTwoDimensionsHorizontal)

        # Testar Vertical Matriz
        TestHorizontal(Lines,Columns,*ListTwoDimensionsVertical)

        # Valores que correspondem as colunas
        ColumnsValues(Columns)

        # Matriz Completa
        CompleteMatriz(Lines,Columns,*ListTwoDimensionsHorizontal,ListTwoDimensionsVertical=ListTwoDimensionsVertical,ListTwoDimensionsSquaresMadePlayersWin=ListTwoDimensionsSquaresMadePlayersWin)

    # ir para as jogadas independente se foi ou nao criado um novo jogo
    InsertPlay(MatrizF,X1F,Y1F,X2F,Y2F,*ListTwoDimensionsSquaresMadePlayersWin)


    while True:
        print("0 - Save Game")
        print("1 - Insert Play")

        # Opçao introduzida pelo user
        ValueInput = int(input("Opção ? "))

        while ValueInput < 0 or ValueInput > 1:
            print("A opção introduzida é invalida tente novamente")
            ValueInput = int(input("Opção ? "))

        if ValueInput == 0:
            Main(MatrizF,X1F,Y1F,X2F,Y2F,*ListTwoDimensionsSquaresMadePlayersWin)
            break
        elif ValueInput == 1:
            InsertPlay(MatrizF,X1F,Y1F,X2F,Y2F,*ListTwoDimensionsSquaresMadePlayersWin)


# 2.1
def InsertPlay(MatrizF,X1,Y1,X2,Y2,*ListTwoDimensionsSquaresMadePlayersWin):

        Lines = MatrizF[0]
        Columns = MatrizF[1]

        # Numero do jogador vai variar entre 1 e 2
        Player = 0

        # Total que esta na lista -> jogador a jogar
        # 0 -> 1
        # 1 -> 2
        # numero par -> 1
        # numero impar -> 2
        # Total de elementos na lista
        LenghtOfList = len(X1)

        # usar o resto do valor inteiro para saber se fica par ou impar
        if LenghtOfList%2 == 0:
            Player = 1
        else:
            Player = 2

        PLayer = AddNewLine(Player,Lines,Columns,X1,Y1,X2,Y2,*ListTwoDimensionsSquaresMadePlayersWin)


# 3
def PlayerVSComputer():

    print("1 - First Player")
    print("2 - Second Player")

    # Opçao introduzida pelo user
    ValueInput = int(input("Opção ? "))

    while ValueInput < 1 or ValueInput > 2:
        print("A opção introduzida é invalida tente novamente")
        ValueInput = int(input("Opção ? "))

    print("\nGrid dimension? (lines, columns)")
    Lines = int(input("linhas -> "))
    Columns = int(input("colunas -> "))
    print ("(%d , %d)" % (Lines,Columns))

    # listas guardadas que vao conter as coordenadas dos traços da matriz
    X1 = []
    Y1 = []
    X2 = []
    Y2 = []

    # é necessario criar fora da funçao pois os valores do player tao sempre a variar
    ListTwoDimensionsSquaresMadePlayersWin = [[0 for x in range(Columns-1)] for y in range(Lines-1)]

    # Inicializar a 0
    l = 0
    for l in range(Lines-1):

        c = 0
        for c in range(Columns-1):
            ListTwoDimensionsSquaresMadePlayersWin[l][c] = 0

    # Matriz Limpa
    CleanMatriz(Lines,Columns)

    # User primeiro a jogar
    if ValueInput == 1:

        while True:
            AddNewLine(1,Lines,Columns,X1,Y1,X2,Y2,*ListTwoDimensionsSquaresMadePlayersWin)
            ComputerPlay(2,Lines,Columns,X1,Y1,X2,Y2,*ListTwoDimensionsSquaresMadePlayersWin)

    # Computador primeiro a jogar
    elif ValueInput == 2:

        while True:
            ComputerPlay(1,Lines,Columns,X1,Y1,X2,Y2,*ListTwoDimensionsSquaresMadePlayersWin)
            AddNewLine(2,Lines,Columns,X1,Y1,X2,Y2,*ListTwoDimensionsSquaresMadePlayersWin)


# 3.1
def ComputerPlay(Player,Lines,Columns,X1,Y1,X2,Y2,*ListTwoDimensionsSquaresMadePlayersWin):

    print("Computer going to Play")

    # verificar as coordenadas disponiveis e escolher uma delas

    # situaçoes que podem acontecer e as que podem ser adicionadas
    # (0,2) (0,2) -> N
    # (0,2) (1,2) -> S
    # (0,1) (0,2) -> S
    # (0,1) (1,2) -> N

    # Os valores tambem nao podem estar cruzados ou seja os do (x e y)1 nao podem ser os mesmos que dos (x e y)2


    # coordenadas vao ser escolhidas aleatoriamente (random)
    # se nao forem possiveis ou ja existirem escolhe outras ate encontrar uma que possa ser usada
    while True:

        X1OP = random.randint(0,Columns-1)
        Y1OP = random.randint(0,Lines-1)
        X2OP = random.randint(0,Columns-1)
        Y2OP = random.randint(0,Lines-1)

        Choise = -1
        Choise = CheckCoordIfArePossible(3,Player,Lines,Columns,X1,Y1,X2,Y2,X1OP,Y1OP,X2OP,Y2OP,*ListTwoDimensionsSquaresMadePlayersWin)

        # Apenas para cortar codigo para o jogo ficar mais pequeno
        # Forma que arranjamos de ficar universal as funçoes para as 3 opçoes dai ter este IF and Else
        if Choise == 0:
            continue
        elif Choise == 1:
            break


# Funçoes Extras

def PlayerNumber(value):
    if value == 1:
        return 2
    else:
        return 1


def CleanMatriz(Lines,Columns):

    # Valores que correspondem as colunas
    ColumnsValues(Columns)

    # Valores que correspondem as linhas e a matriz com os pontos
    l = 0
    for l in range(Lines):
        print(l, end='')

        c = 0
        for c in range(Columns):

            if c == 0:
                print(" .", end="")
            else:
                print("  ", end=" ")
                print(".", end="")
        print("\n")


# Tando da para todas as opçoes 1 2 3 apenas para poupar codigo
def AddNewLine(Player,Lines,Columns,X1,Y1,X2,Y2,*ListTwoDimensionsSquaresMadePlayersWin):

    print("Player %d: coordinates for the line endpoints? (x1,y1)(x2,y2)" % Player)

    # Coordenadas opecionais temporarias tanto podem ser possivies ou nao
    X1OP = int(input("X1 -> "))
    Y1OP = int(input("Y1 -> "))
    X2OP = int(input("X2 -> "))
    Y2OP = int(input("Y2 -> "))

    # situaçoes que podem acontecer e as que podem ser adicionadas
    # (0,2) (0,2) -> N
    # (0,2) (1,2) -> S
    # (0,1) (0,2) -> S
    # (0,1) (1,2) -> N

    # Os valores tambem nao podem estar cruzados ou seja os do (x e y)1 nao podem ser os mesmos que dos (x e y)2
    Player = CheckCoordIfArePossible(0,Player,Lines,Columns,X1,Y1,X2,Y2,X1OP,Y1OP,X2OP,Y2OP,*ListTwoDimensionsSquaresMadePlayersWin)

    return Player


# Tando da para todas as opçoes 1 2 3 apenas para poupar codigo
def CheckCoordIfArePossible(ID,Player,Lines,Columns,X1,Y1,X2,Y2,X1OP,Y1OP,X2OP,Y2OP,*ListTwoDimensionsSquaresMadePlayersWin):

    # Se os xxs so variarem 1 unidade e os yys mantem se iguais e menor que o numero de linhas                      # Se os yys so variarem 1 unidade e os xxs mantem se iguais e menos que o numero de colunas
    if ((( ( (X1OP == (X2OP-1)) | (X2OP == (X1OP-1)) ) & (Y1OP == Y2OP)) & ((X1OP<=(Lines-1)) & (X2OP<=(Lines-1)))) | ((((Y1OP == (Y2OP-1)) | (Y2OP == (Y1OP-1))) & (X1OP == X2OP)) & ((Y1OP<=(Columns-1)) & (Y2OP<=(Columns-1)))) ):

        # as listas ja contem coordenadas
        if len(X1) != 0:

            # 1 corresponde a true
            AddToList = 1

            # Verificar se as novas coordenadas ja existem na lista
            d = 0
            for d in range(len(X1)):

                # vamos ver se o traço ja esta nas listas (ou seja valores repetidos nas listas)
                # Os valores tambem nao podem estar cruzados ou seja os do (x e y)1 nao podem ser os mesmos que dos (x e y)2
                if (((X1[d] == X1OP) & (X2[d] == X2OP) & (Y1[d] == Y1OP) & (Y2[d] == Y2OP)) | ((X1[d] == X2OP) & (X2[d] == X1OP) & (Y1[d] == Y2OP) & (Y2[d] == Y1OP))):
                    AddToList = 0
                    break


            # Caso seja possivel adicionar as listas
            if AddToList == 1:

               X1.append(X1OP)
               Y1.append(Y1OP)
               X2.append(X2OP)
               Y2.append(Y2OP)

            else:
                print("as coordenadas que introduzio ja existem")

                # Sair da Funçao

                # Quer dizer que é Do Computador Unica forma que arranjamos de poupar codigo
                if (ID == 3):
                    # Continue
                    return 0
                else:
                    return Player

        else:

            # esta vazia a lista estes sao os primeiros elementos
            X1.append(X1OP)
            Y1.append(Y1OP)
            X2.append(X2OP)
            Y2.append(Y2OP)


        # imprime as coordenadas do novo traço adicionadas
        New = (len(X1)-1)
        print ('(%d , %d) , (%d , %d)' % (X1[New],Y1[New],X2[New],Y2[New]))

        # https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
        # Listas (Lines) Elementos (Columns)
        ListTwoDimensionsHorizontal = [[0 for x in range(Columns)] for y in range(Lines)]
        ListTwoDimensionsVertical = [[0 for x in range(Columns)] for y in range(Lines)]

        # Adicionar a listas Horizontal e Vertical os valores ja presentes na Matriz
        # estas listas sao necessarias para criar os traços
        # https://stackoverflow.com/questions/48814875/missing-1-required-keyword-only-argument
        AddToHorizontalAndVerticalList(Lines,Columns,X1,Y1,X2,Y2,*ListTwoDimensionsHorizontal,ListTwoDimensionsVertical=ListTwoDimensionsVertical)

        # Testar Horizontal Matriz
        TestHorizontal(Lines,Columns,*ListTwoDimensionsHorizontal)

        # Testar Vertical Matriz
        TestVertical(Lines,Columns,*ListTwoDimensionsVertical)

        # Valores que correspondem as colunas
        ColumnsValues(Columns)

        # Lista com os quadrados ja feitos
        # Columns-1 e Lines-1 devem se ao facto de so serem possiveis fazer este numero de quadrados
        ListTwoDimensionsSquaresMade = [[0 for x in range(Columns-1)] for y in range(Lines-1)]

        # Inicializar a 0
        l = 0
        for l in range(Lines-1):

            c = 0
            for c in range(Columns-1):
                ListTwoDimensionsSquaresMade[l][c] = 0


        # Como vai funcionar -> Como sao necessarios 4 traços para fazer 1 quadrado vamos ver os traços ja presentes na matriz e ver a quais quadrados pertencem


        # Horizontal
        l = 0
        for l in range(Lines):

            c = 0
            for c in range(Columns-1):

                # So conta um quadrado # linha 0 ou ultima linha
                if ( (ListTwoDimensionsHorizontal[l][c]!=-1) & ((l==0) | (l==Lines-1)) ) :

                    if (l==0):
                        ListTwoDimensionsSquaresMade[0][c] = ListTwoDimensionsSquaresMade[0][c] + 1
                    elif (l==Lines-1):
                        # l-1 pois a matriz tem menos 1 linha
                        ListTwoDimensionsSquaresMade[l-1][c] = ListTwoDimensionsSquaresMade[l-1][c] + 1

                # conta em varios quadrados ao mesmo tempo no dele e no anterior
                elif  (ListTwoDimensionsHorizontal[l][c]!=-1):
                    ListTwoDimensionsSquaresMade[l-1][c] = ListTwoDimensionsSquaresMade[l-1][c] + 1
                    ListTwoDimensionsSquaresMade[l][c] = ListTwoDimensionsSquaresMade[l][c] + 1

        # Vertical
        l = 0
        for l in range(Lines-1):

            c = 0
            for c in range(Columns):

                # So conta um quadrado # Coluna 0 ou ultima Coluna
                if ( (ListTwoDimensionsVertical[l][c]!=-1) & ((c==0) | (c==Columns-1)) ) :

                    if (c==0):
                        ListTwoDimensionsSquaresMade[l][0] = ListTwoDimensionsSquaresMade[l][0] + 1
                    elif (c==Columns-1):
                        # c-1 pois a matriz tem menos 1 coluna
                        ListTwoDimensionsSquaresMade[l][c-1] = ListTwoDimensionsSquaresMade[l][c-1] + 1

                # conta em varios quadrados ao mesmo tempo no dele e no anterior
                elif  (ListTwoDimensionsVertical[l][c]!=-1):
                    ListTwoDimensionsSquaresMade[l][c-1] = ListTwoDimensionsSquaresMade[l][c-1] + 1
                    ListTwoDimensionsSquaresMade[l][c] = ListTwoDimensionsSquaresMade[l][c] + 1

        # Aqui vamos Verificar se ja existe algum quadrado completo e atribuir noutra lista fora da funçao (para guardar o valor) o jogador que fez o quadrado
        l = 0
        for l in range(Lines-1):
            c = 0
            for c in range(Columns-1):

                # Caso um quadrado fique completo colocar o jogador que fez o feito numa outra matriz
                if ((ListTwoDimensionsSquaresMade[l][c] == 4) & (ListTwoDimensionsSquaresMadePlayersWin[l][c] == 0)):
                    ListTwoDimensionsSquaresMadePlayersWin[l][c] = Player


        # Matriz Completa Imprimir
        CompleteMatriz(Lines,Columns,*ListTwoDimensionsHorizontal,ListTwoDimensionsVertical=ListTwoDimensionsVertical,ListTwoDimensionsSquaresMadePlayersWin=ListTwoDimensionsSquaresMadePlayersWin)

        # Testar as matrizes da percentagem q os quadrados estao e os players que fizeram o quadrados
        TestMatrizSquares(Lines,Columns,*ListTwoDimensionsSquaresMade,ListTwoDimensionsSquaresMadePlayersWin=ListTwoDimensionsSquaresMadePlayersWin)

        CountToFinish = 0
        TotalPlayer1 = 0
        TotalPlayer2 = 0

        # Aqui vamos verificar se ja foram introduzidos todos o traços ou seja feito todos os quadrados e se sim dizer o numero de quadrados que cada um fez
        l = 0
        for l in range(Lines-1):
            c = 0
            for c in range(Columns-1):

                # Caso um quadrado fique completo colocar o jogador que fez o feito numa outra matriz
                if (ListTwoDimensionsSquaresMade[l][c] == 4):
                    CountToFinish = CountToFinish + 1

                    # Numero de quadrados de cada jogador
                    if (ListTwoDimensionsSquaresMadePlayersWin[l][c] == 1):
                            TotalPlayer1 = TotalPlayer1+1
                    else:
                            TotalPlayer2 = TotalPlayer2+1

        # Caso Tenha Feito os quadrados Todos
        if CountToFinish == (Lines-1)*(Columns-1):
            print("Game ended. Score is:")
            print("  PLayer 1 -> %d" % TotalPlayer1)
            print("  PLayer 2 -> %d" % TotalPlayer2)
            print("")
            print("A sair")
            sys.exit()

        Player = PlayerNumber(Player)

        # Quer dizer que é Do Computador Unica forma que arranjamos de poupar codigo
        if (ID == 3):
            # Break
            return 1
        else:
            return Player
    else:
        print("As coordenadas que introduzio nao sao validas tente novamente")


def ColumnsValues(Columns):
    c = 0
    for c in range(Columns):
            print(" ", c, end=" ")
    print ()


# https://stackoverflow.com/questions/36620025/pass-array-as-argument-in-python
def AddToHorizontalAndVerticalList(Lines,Columns,X1,Y1,X2,Y2,*ListTwoDimensionsHorizontal,ListTwoDimensionsVertical):

    # Inicializar com os valores -1
    l = 0
    for l in range(Lines):

        c = 0
        for c in range(Columns):
            ListTwoDimensionsHorizontal[l][c] = -1
            ListTwoDimensionsVertical[l][c] = -1

    x = 0
    for x in range(len(X1)):

        # Hozintal(-)
        l = 0
        for l in range(Lines):

            # se as 2 coordenadas nos eixos dos xxs tiverem o mesmo valor
            # Adicionar na Matriz (lista de 2 dimensoes) Horizontal
            if ((X1[x] == l) & (X2[x] == l)):

                    # Verificar qual dos 2 yys o que vem primeiro (menor)
                    if (Y1[x] < Y2[x]):
                        ListTwoDimensionsHorizontal[l][Y1[x]] = X1[x]
                    elif (Y1[x] > Y2[x]):
                        ListTwoDimensionsHorizontal[l][Y2[x]] = X1[x]


        # Vertical (|)
        c = 0
        for c in range(Columns):

            # se as 2 coordenadas nos eixos dos yys tiverem o mesmo valor
            # Adicionar na Matriz (lista de 2 dimensoes) Vertical
            if ((Y1[x] == c) & (Y2[x] == c)):

                # Verificar qual dos 2 yys o que vem primeiro (menor)
                if (X1[x] < X2[x]):
                    ListTwoDimensionsVertical[X1[x]][c] = Y1[x]
                elif (X1[x] > X2[x]):
                    ListTwoDimensionsVertical[X2[x]][c] = Y1[x]


# https://stackoverflow.com/questions/36620025/pass-array-as-argument-in-python
def CompleteMatriz(Lines,Columns,*ListTwoDimensionsHorizontal,ListTwoDimensionsVertical,ListTwoDimensionsSquaresMadePlayersWin):
    # Matriz Completa
    l = 0
    for l in range(Lines):
        print(l, end="")

        # Horizontal(-)
        c = 0
        for c in range(Columns):
            if c == 0:
                print(" .", end="")
            else:

                # necessario ser c-1 por causa do primeiro .
                if (ListTwoDimensionsHorizontal[l][c-1] == -1):
                    print("  ", end=" ")
                else:
                    print(" -", end=" ")

                # Mudança de linha
                if c == Columns-1:
                    print(".")
                else:
                    print(".", end="")


        # Vertical(|)
        c = 0
        for c in range(Columns):

            if (c==0):
                print("  ", end="")

            if (ListTwoDimensionsVertical[l][c] == -1):
                print(" ", end="")
            else:
                print("|", end="")

            if (l != Lines-1):
                if (c!=Columns-1):
                    if (ListTwoDimensionsSquaresMadePlayersWin[l][c] != 0):
                        print("",ListTwoDimensionsSquaresMadePlayersWin[l][c],"", end="")
                    else:
                        print("   ", end="")
                else:
                    print("   ", end="")


            # Mudança de linha
            if c == Columns-1:
                print("")


# https://stackoverflow.com/questions/36620025/pass-array-as-argument-in-python
def TestHorizontal(Lines,Columns,*ListTwoDimensionsHorizontal):

    print()
    print("Teste Horizontal")
    l = 0
    for l in range(Lines):

        c = 0
        for c in range(Columns):
            print(" ",ListTwoDimensionsHorizontal[l][c], end="")
        print()
    print()


# https://stackoverflow.com/questions/36620025/pass-array-as-argument-in-python
def TestVertical(Lines,Columns,*ListTwoDimensionsVertical):

    print("Teste Vertical")
    l= 0
    for l in range(Lines):

        c = 0
        for c in range(Columns):
            print(" ",ListTwoDimensionsVertical[l][c], end="")
        print()
    print()
    print()


# https://stackoverflow.com/questions/36620025/pass-array-as-argument-in-python
def TestMatrizSquares(Lines,Columns,*ListTwoDimensionsSquaresMade,ListTwoDimensionsSquaresMadePlayersWin):

    print("Squares Percentage to 4")
    l= 0
    for l in range(Lines-1):
        c = 0
        for c in range(Columns-1):
            print(' ',ListTwoDimensionsSquaresMade[l][c], end='')
        print()
    print()
    print()

    print("Players Made Squares")
    l= 0
    for l in range(Lines-1):
        c = 0
        for c in range(Columns-1):
            print(' ',ListTwoDimensionsSquaresMadePlayersWin[l][c], end='')
        print()
    print()
    print()



# ***
# O programa começa aqui onde é chamada a funçao do Menu Principal

# é necessario uma matriz pois queremos guardar as linhas e as colunas para o Save Game na opçao 2
# Linhas e Colunas
Matriz = [0,0]

# é necessario pois queremos guardar as coordenadas dos traços para o Save Game na opçao 2
# listas guardadas que vao conter as coordenadas dos traços da matriz
X1 = []
Y1 = []
X2 = []
Y2 = []

# é necessario Para o Save Game na opçao 2
# Vai guardar os numeros dos players que ja fizeram quadrados pois os valores do player tao sempre a variar
# Começa com dimensao 1 / 1 pois nao sabemos o numero de linhas nem colunas
ListTwoDimensionsSquaresMadePlayersWin = [[0 for x in range(1)] for y in range(1)]

# Chamar a funçao Main
Main(Matriz,X1,Y1,X2,Y2,*ListTwoDimensionsSquaresMadePlayersWin)
 

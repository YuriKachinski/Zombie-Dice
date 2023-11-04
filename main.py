import random
from random import randint

print("#" * 46)
print("Aluno: Yuri Kachinski")
print("Curso: Análise e Desenvolvimento de Sistemas")
print("Matéria: Raciocinio Computacional")
print("Zombie dice (semana 8)")
print("#" * 46, "\n")
print("Seja bem-vindo ao jogo Zombie dice!")
print("Vencerá a partida, quem comer 13 cérebros primeiro")

numJogadores = 0
while (numJogadores < 2):
    numJogadores = int(input("Informe o número de jogadores:"))

    if (numJogadores < 2):
        print("AVISO: É necessario pelo menos 2 jogadores para executar o jogo!")

listaJogadores = []

for i in range(numJogadores):
    nome = str(input("Informe o nome do jogador" + str(i + 1) + ":")).strip()
    listaJogadores.append(nome)

print("Agora sim, vamos iniciar o jogo?")
str(input("Pressione 'S' para sim:")).strip().upper()

def pegardadosVerde():
    return ("C","P","C","T","P","C")

def pegardadosAmarelo():
    return ("T","P","C","T","P","C")

def pegardadosVermelho():
    return ("T", "P", "T", "C", "P", "T")

def initdadosCopo(copo):
    # colocar dados verdes no copo
    for i in range(0,6):
        copo.append(pegardadosVerde())
        #colocar dados amarelos no copo
    for i in range(0,4):
        copo.append(pegardadosAmarelo())
        #colocar dados vermelhos no copo
    for i in range(0,3):
        copo.append(pegardadosVermelho())

def pegardadosCopo(copo):
    # Quantidade de dados no copo
    if len(copo) !=0:
        numDados = (len(copo)-1)
        index = randint(0,numDados)
        dado = copo[index]
        del(copo[index])
        return dado, copo
    else:
        print("Copo vazio!!")
        return -1, copo

def lancarDado(dado):
    dadoSorteado = randint(0,5)

    if dado[dadoSorteado] == "C":
        print("Cerebro!!!")
        return 'C'
    elif dado[dadoSorteado] == "T":
        print("Tiro!")
        return 'T'
    else:
        print("Passos...")
        return 'P'



dadoVerde: tuple = ("C", "P", "C", "T", "P", "C")
dadoAmarelo: tuple = ("T", "P", "C", "T", "P", "C")
dadoVermelho: tuple = ("T", "P", "T", "C", "P", "T")


listaDados = [dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,
              dadoAmarelo,dadoAmarelo,dadoAmarelo,dadoAmarelo,
              dadoVermelho,dadoVermelho,dadoVermelho]


print("INICIANDO JOGO!")
jogadorAtual = 0
dadosSorteados = []
tiros = 0
passos = 0

pontuacaoJogadores =[[0,0], [1,0]]

while True:
    print("Turno do jogador  {}".format(listaJogadores[jogadorAtual]))
    print("-" * 36)
    for i in range(0, 3):
        numSorteado = random.randint(0,12)
        dadoSorteado = listaDados[numSorteado]
        if dadoSorteado == ("C", "P", "C", "T", "P", "C"):
            corDado = "Verde"
        elif dadoSorteado == ("T", "P", "C", "T", "P", "C"):
            corDado = "Amarelo"
        else:
            corDado = "Vermelho"
        print("A cor do dado sorteado foi: {}".format(corDado))
        dadosSorteados = dadoSorteado

    print("--------------------")
    print("Vamos ver a face sorteada de cada um dos dados?")
    str(input("Digite 'S' para sim:")).strip().upper()
    print("Após jogar os 3 dados, a face de cada um foi: ")
    print("--------------------")
    for i in range(0, 3, 1):
        faceSorteada = random.choice(dadosSorteados)
        if faceSorteada == "C":
            print("Cérebro - Você devorou um cérebro!")
            pontuacaoJogadores[jogadorAtual][1] = pontuacaoJogadores[jogadorAtual][1] + 1
        elif faceSorteada == "T":
            print("Tiros... Você levou um tiro")
            tiros = tiros + 1
        else:
            print("Passos - Sua vítima escapou!")
            passos = passos + 1


    print("-" * 37)
    print("PONTUAÇÃO ATUAL")
    print("Cérebros: {}".format(pontuacaoJogadores[jogadorAtual][1]))
    print("Tiros: {}".format(tiros))
    print("Passos: {}".format(passos))
    if tiros >= 3:
        pontuacaoJogadores[jogadorAtual][1]=0
        continuarTurno = "N"
        print("Você pegou 3 tiros, sua pontuacao foi zerada...")
    if pontuacaoJogadores[jogadorAtual][1] >= 13:
        print("Voce devorou 13 cerebros e venceu o jogo!")
        break
    if tiros <3:
        continuarTurno = str(input("Deseja continuar seu turno? Pressione S para sim e N para não:")).strip()\
        .upper()
    if continuarTurno == "N":
        jogadorAtual = jogadorAtual + 1
        dadosSorteados = []
        tiros = 0
        passos = 0
        if jogadorAtual == len(listaJogadores):
            jogadorAtual = 0
    else:
        print("Iniciando mais uma rodada para o jogador atual")
        dadosSorteados = []
from flask import Flask, render_template, request, jsonify
import pandas as pd
import random
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

#NESTE PEQUENO TRECHO É DEFINIDO A DIFICULDADE DA IA
#CASO CAIA NOS 92%, ELE VAI EXECUTAR UMA JOGADA PERFEITA, CASO CONTRÁRIO ELE VAI JOGAR ALEATORIAMENTE

DIFICULDADE = 0.92

#IMPORTAÇÃO DO DATASET PARA TREINAMENTO

data = pd.read_csv("tic_tac_toe_dataset.csv")

X = data.iloc[:,0:9]
y = data["move"]

#TREINAMENTO DO MODELO (NESTE CASO USEI RamdomForestClassifier)
model = RandomForestClassifier()
model.fit(X,y)

#VERIFICACAO DE VITÓRIA

def verificar_vitoria(tab,player):

    combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in combos:
        if tab[a]==tab[b]==tab[c]==player:
            return True

    return False

#====================================================================================#
# ALGORITMO MINIMAX - USADO PARA jogos de dois jogadores (xadrez, jogo da velha),    #
# que busca a melhor jogada maximizando o próprio ganho e minimizando o do oponente. #
#====================================================================================#

def minimax(tab, player):

    if verificar_vitoria(tab,1):
        return 1,None

    if verificar_vitoria(tab,2):
        return -1,None

    if 0 not in tab:
        return 0,None

    melhor_jogada = None

    if player == 1:

        melhor = -999

        for i in range(9):

            if tab[i] == 0:

                tab[i] = 1
                score,_ = minimax(tab,2)
                tab[i] = 0

                if score > melhor:
                    melhor = score
                    melhor_jogada = i

        return melhor,melhor_jogada

    else:

        melhor = 999

        for i in range(9):

            if tab[i] == 0:

                tab[i] = 2
                score,_ = minimax(tab,1)
                tab[i] = 0

                if score < melhor:
                    melhor = score
                    melhor_jogada = i

        return melhor,melhor_jogada

#=================================
# CODIGO DE JOGADAS DA IA
#=================================

def jogada_ia(tab):

    # probabilidade de jogar perfeito
    if random.random() < DIFICULDADE:

        _,pos = minimax(tab,1)
        return pos

    # jogada aleatória (erro da IA)
    livres = [i for i in range(9) if tab[i] == 0]
    return random.choice(livres)

#=================================
# ROTAS FLASK
#=================================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/jogar", methods=["POST"])
def jogar():

    tab = request.json["tabuleiro"]
    vencedor = None

    # VERIFICA A VITÓRIA POR PARTE DO JOGADOR
    if verificar_vitoria(tab,2):
        vencedor = "Jogador Venceu!"

    elif 0 not in tab:
        vencedor = "Empate"

    else:

        pos = jogada_ia(tab)
        tab[pos] = 1

        # VERIFICA A VITÓRIA POR PARTE DA IA 
        if verificar_vitoria(tab,1):
            vencedor = "IA Venceu!"

        elif 0 not in tab:
            vencedor = "Empate"

    return jsonify({
        "tabuleiro": tab,
        "vencedor": vencedor
    })

#ESTE PEQUENO CODIGO ABAIXO EXECUTA TUDO

app.run(debug=True)
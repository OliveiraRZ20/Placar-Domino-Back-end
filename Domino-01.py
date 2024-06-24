from os import system, name

# primeiro de tudo vou fazer a função que vai limpar a tela quando eu precisar

def limpa_tela():
    _ = system("cls")


# a ideia aqui é fazer um sistema de dominó para contar o número de jogadores, somar as suas pontações e dizer rodada por rodada quem está vencendo
# primeira coisa, perguntar o número de jogadores pra saber quantos nomes serão:

num_jogadores = int(input("Quantos jogadores estão presentes esta noite? "))
list_jogadores = []

for i in range(1, num_jogadores + 1):
    nome = input(f"Qual o nome do {i}° jogador? ")
    list_jogadores.append(nome)

# com isso aqui encima ja temos um sistema de anotar todos os jogadores e os seus nomes
# proximo passo é: criar uma lista com as pontuações e preencher elas com 0's o suficiente pra cada jogador (analise futura pra poder adicionar pontuações)

list_points = []

for i in range(1, num_jogadores + 1):
    list_points.append(0)

# agora podemos criar uma tela de check das pontuações, assim poderemos analisas como está o jogo de cada um por um "diplay no prompt"

contagem = 0
def tabela():
    global contagem
    print("###############################################################")
    print()
    print(f"para a nossa {contagem}° rodada temos as seguintes pontuações")
    print()
    for i in range(0, num_jogadores):
        print(f"{list_jogadores[i]}: {list_points[i]}")
    print()
    print("###############################################################")
    input("Pressione Enter para continuar ")
    contagem += 1

# a ideia agora é fazer um jeito de atualizar o placar quando uma nova rodada é realizada no dominó
# ir de jogador em jogador perguntando quantos pontos eles fizeram na rodada atual e somar esse valor ao da lista de pontuações pra mostras depois

def update():
    global list_jogadores, list_points
    print()
    print("###############################################################")
    print()
    for i in range(0, num_jogadores):
        num_add = int(input(f"quantos pontos o jogador(a) {list_jogadores[i]} fez nessa rodada? "))
        while not type(num_add) == int:
            num_add = int(input("Resposta invalida, tente novamente: "))
        memory = list_points[i]
        list_points[i] = num_add + memory
    print()
    print("###############################################################")

# agora vou fazer um verificador de finalização de jogo

end_game = False
def finalizacao():
    global end_game
    choice = input("Proxima rodada ou finalizar o jogo? [1] / [2]: ")
    while choice not in ("1","2"):
        choice = input("Resposta inválida, Tente novamente, proxima rodada ou finalizar o jogo? [1] / [2]: ")
    if choice == "1":
        end_game = False
    if choice == "2":
        end_game = True

# por fim podemos fazer uma tela de placar final mostrando as pontuações de cada jogador rankeado



def placar_final():
    dict_jogadores = {}

    for i in range(0, num_jogadores):
        name, point = list_jogadores[i], list_points[i]
        dict_update = {point: name}
        dict_jogadores.update(dict_update)


    list_placar_final = list_points
    list_placar_final.sort()
    print("###############################################################")
    print()
    print("Para o nosso placar final então teremos:")
    print()
    for i in range(0, num_jogadores):
        print(f"em {i+1}° lugar temos: {dict_jogadores[list_placar_final[i]]} ({list_points[i]})")
    print()
    print("###############################################################")


# esse ultimo passo aqui faz com que o jogo funcione e inicie com o código quando eu executo

if __name__ == "__main__":
    while not end_game:
        limpa_tela()
        tabela()
        update()
        finalizacao()
    placar_final()
    
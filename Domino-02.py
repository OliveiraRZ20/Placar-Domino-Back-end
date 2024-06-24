from os import system, name


class Domino:

    def __init__(self):
        self.num_jogadores = 0
        self.list_jogadores = []
        self.list_points = []
        self.contagem = 0
        self.dict_jogadores = {}
        self.end_game = False

        print("Bem vindo ao Dominó do lucca")
        print("Jogo inicializado com sucesso.")
        

    def limpa_tela(self):
        _ = system("cls")


    def cadastro_jogadores(self):
        self.num_jogadores = int(input("Quantos jogadores estão presentes esta noite? "))

        for i in range(1, self.num_jogadores + 1):
            nome = input(f"Qual o nome do {i}° jogador? ")
            self.list_jogadores.append(nome)

        for i in range(1, self.num_jogadores + 1):
            self.list_points.append(0)


    def tabela(self):
        print("###############################################################")
        print()
        print(f"para a nossa {self.contagem}° rodada temos as seguintes pontuações")
        print()
        for i in range(0, self.num_jogadores):
            print(f"{self.list_jogadores[i]}: {self.list_points[i]}")
        print()
        print("###############################################################")
        input("Pressione Enter para continuar ")

        self.contagem += 1
    

    def update(self):
        print()
        print("###############################################################")
        print()
        for i in range(0, self.num_jogadores):
            num_add = int(input(f"quantos pontos o jogador(a) {self.list_jogadores[i]} fez nessa rodada? "))
            while not type(num_add) == int:
                num_add = int(input("Resposta invalida, tente novamente: "))
            memory = self.list_points[i]
            self.list_points[i] = num_add + memory
        print()
        print("###############################################################")


    def finalizacao(self):
        choice = input("Proxima rodada ou finalizar o jogo? [1] / [2]: ")
        while choice not in ("1","2"):
            choice = input("Resposta inválida, Tente novamente, proxima rodada ou finalizar o jogo? [1] / [2]: ")
        if choice == "1":
            self.end_game = False
        if choice == "2":
            self.end_game = True

    def verifica_end(self):
        if self.end_game:
            return True
        else:
            return False
    

    def placar_final(self):

        for i in range(0, self.num_jogadores):
            name, point = self.list_jogadores[i], self.list_points[i]
            dict_update = {point: name}
            self.dict_jogadores.update(dict_update)

        list_placar_final = self.list_points
        list_placar_final.sort()
        print("###############################################################")
        print()
        print("Para o nosso placar final então teremos:")
        print()
        for i in range(0, self.num_jogadores):
            print(f"em {i+1}° lugar temos: {self.dict_jogadores[list_placar_final[i]]} ({self.list_points[i]})")
        print()
        print("###############################################################")


if __name__ == "__main__":
    Game = Domino()
    Game.cadastro_jogadores()
    while not Game.verifica_end():
        Game.limpa_tela()
        Game.tabela()
        Game.update()
        Game.finalizacao()
    Game.placar_final()
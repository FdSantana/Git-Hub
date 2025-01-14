import random

# Personagem: classe mae
# Heroi: derivado do personagem / controlado pelo usuario
# Inimigo: adversario do usuario

class Personagem:

    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f'Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}'

    def receber_ataque(self, dano):
        self.__vida = self.__vida - dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = self.__nivel * 2
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        return print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")


class Heroi(Personagem):

    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)  # dano aumentado
        alvo.receber_ataque(dano)
        return print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")


class Inimigo(Personagem):

    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo


class Jogo:
    """
    Classe orquestradora do jogo
    """

    def __init__(self) -> None:
        self.heroi = Heroi('Heroi', 100, 5, 'Super Força')
        self.inimigo = Inimigo('Morcego', 80, 5, 'Voador')

    def iniciar_batalha(self):
        """
        Fazer a gestao da batalha em turnos
        """
        print("iniciando batalha")

        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input(
                "Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
            else:
                print('escolha invalida. Escolha novamente..')
                
            if self.inimigo.get_vida() > 0:
                """
                Vez do inimigo atacar o heroi
                """
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("Parabéns, você venceu a batalha!")
        else:
            print("\nVocê foi derrotado!")


# Criar instancia do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()

import tkinter as tk
from tabuleiro import Tabuleiro
from puzzle import Puzzle


def main():
    estado_final = [0,1,2,3,4,5,6,7,8,9]
    estado_atual = []
    # Cria uma instância da classe Puzzle
    game = Puzzle(estado_final)
    print(game)
    print("Aperte a tecla A para o jogo começar...")
    teclado = input()
    while True:
        if teclado == "A":
            estado_atual = game.gerar_estado_aleatorio()
            print(game)
            break
        else:
            print("Tecla inválida. Aperte a tecla A para o jogo começar")
            teclado = input()

    # Verifica se o estado gerado é resolvível
    while game.eh_solucionavel():
        if teclado == "A":
            estado_atual = game.gerar_estado_aleatorio()
            game.estado = estado_atual
            game.solucionar(estado_atual)
            print(game)
        elif teclado == "E":
            estado_atual = game.mover_esquerda()
            game.estado = estado_atual
            game.solucionar(estado_atual)
            print(game)
        elif teclado == "D":
            estado_atual = game.mover_direita()
            game.estado = estado_atual
            game.solucionar(estado_atual)
            print(game)
        elif teclado == "B":
            estado_atual = game.mover_baixo()
            game.estado = estado_atual
            game.solucionar(estado_atual)
            print(game)
        elif teclado == "C":
            estado_atual = game.mover_cima()
            game.estado = estado_atual
            game.solucionar(estado_atual)
            print(game)
        else:
            print("Tecla inválida escolha uma das opções: ")

        teclado = input()


if __name__ == '__main__':
    main()

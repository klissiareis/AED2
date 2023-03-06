import random
from queue import PriorityQueue
from typing import List


class Puzzle:
    def __init__(self, estado: List[int]):
        self.estado = estado

    def __str__(self):
        """Retorna uma representação em string do tabuleiro."""
        s = ""
        print("\n" * 130)
        for i in range(3):
            for j in range(3):
                index = 3 * i + j
                if self.estado[index] == 0:
                    s += "  "
                else:
                    s += f"{self.estado[index]:2d}"
                if j < 2:
                    s += " |"
            s += "\n"
            if i < 2:
                s += "---+---+---\n"

        print("\n-------Jogo das 8 peças------------")
        print("\nDigite uma tecla para a opção desejada: \n")
        print("Esquerda(E) - Direita(D) - Baixo(B)\nCima(C) - Gerar Aleatorio(A)\n")
        return s

    def eh_estado_final(self) -> bool:
        """Retorna True se o tabuleiro estiver no estado final."""
        return self.estado == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def mover_esquerda(self) -> bool:
        """Move a peça vazia para a esquerda."""
        index = self.estado.index(0)
        if index % 3 == 0:
            return False
        self.estado[index], self.estado[index - 1] = self.estado[index - 1], self.estado[index]
        return True

    def mover_direita(self) -> bool:
        """Move a peça vazia para a direita."""
        index = self.estado.index(0)
        if index % 3 == 2:
            return False
        self.estado[index], self.estado[index + 1] = self.estado[index + 1], self.estado[index]
        return True

    def mover_cima(self) -> bool:
        """Move a peça vazia para cima."""
        index = self.estado.index(0)
        if index < 3:
            return False
        self.estado[index], self.estado[index - 3] = self.estado[index - 3], self.estado[index]
        return True

    def mover_baixo(self) -> bool:
        """Move a peça vazia para baixo."""
        index = self.estado.index(0)
        if index > 5:
            return False
        self.estado[index], self.estado[index + 3] = self.estado[index + 3], self.estado[index]
        return True

    def contar_inversoes(self) -> int:
        """Conta o número de inversões no estado atual."""
        count = 0
        for i in range(8):
            for j in range(i + 1, 9):
                if self.estado[i] > self.estado[j] and self.estado[i] != 0 and self.estado[j] != 0:
                    count += 1
        return count

    def eh_solucionavel(self) -> bool:
        """Retorna True se o tabuleiro for solucionável."""
        return self.contar_inversoes() % 2 == 0

    def heuristica(self) -> int:
        """Calcula a heurística do estado atual."""
        count = 0
        for i in range(9):
            if self.estado[i] != i and self.estado[i] != 0:
                count += 1
        return count

    def gerar_estado_aleatorio(self):
        """Gera um estado aleatorio"""
        self.estado = list(range(9))
        random.shuffle(self.estado)
        while not self.eh_solucionavel():
            i, j = random.sample(range(9), 2)
            self.estado[i], self.estado[j] = self.estado[j], self.estado[i]
        return self.estado
    
    def solucionar(self, estado):
        if not self.eh_solucionavel():
            return None
        fila = PriorityQueue()
        fila.put((0, estado, []))
        visitado = set()
        while fila.empty():
            _, estado, caminho = fila.get()
            if estado == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                return caminho
            if tuple(estado) in visitado:
                continue
            visitado.add(tuple(estado))
            posicao_vazia = estado.index(0)
            for move, neighbor_pos in [('left', posicao_vazia-1), ('right', posicao_vazia+1), ('up', posicao_vazia-3), ('down', posicao_vazia+3)]:
                if 0 <= neighbor_pos < 9 and (posicao_vazia % 3 != 0 or move != 'right') and ((posicao_vazia + 1) % 3 != 0 or move != 'left'):
                    neighbor_state = estado[:]
                    neighbor_state[posicao_vazia], neighbor_state[neighbor_pos] = neighbor_state[neighbor_pos], neighbor_state[posicao_vazia]
                    fila.put((len(caminho)+1+self.heuristica(neighbor_state), neighbor_state, caminho+[move]))
        return None


from random import random
import time, colorama, os, platform
os_name = platform.system()

def console_clear():
    if os_name == "Windows":
        os.system("cls")
        return
    os.system("clear")
def draw(matriz):
    global steps, dimension
    size = dimension*2 + 2
    txt = "mov = {}".format(steps)
    posx = "x = {}".format(x)
    posy = "y = {}".format(y)
    r = int(size/2) # Para dividir o largura em 2
    q = int(r/2) # Para dividir a largura em 4
    console_clear()
    print(colorama.Back.BLUE + " "*(r - int(len(txt)/2) - 2) + txt + " "*(r - (len(txt) - int(len(txt)/2)) - 2) + colorama.Style.RESET_ALL) # Corrigir isso
    print("\n".join("".join(el for el in row) for row in matriz))
    print(colorama.Back.BLUE + " "*(q - int(len(posx)/2) - 1) + posx + " "*(q - (len(posx) - int(len(posx)/2))) + " "*(q - int(len(posy)/2)) + posy + " "*(q - (len(posy) - int(len(posy)/2)) - 1) + colorama.Style.RESET_ALL)

dimension = int(input("Digite a dimensão da rede: ")) + 2
console_clear()
mov = int(input("Digite a quantidade de movimentos: "))
console_clear()
tm = float(input("Digite o intervalo de tempo entre cada movimento: "))
console_clear()

box_symb = ["\u2554","\u2557","\u2551","\u2550","\u255A","\u255D", "\u001b[35m\u25A0\u001b[0m", "\u001b[35m\u2584\u001b[0m", "\u001b[35m\u2580\u001b[0m"]
matrix = [[0 for i in range(dimension)] for j in range(dimension)] # Matriz que vai ser printada no console
pos_init = int(dimension/2) - 1
y,x = [pos_init,pos_init] # Posição inicial da partícula
steps = 0

for j in range(dimension):
    for i in range(dimension):
        if j == 0 and i == 0: # Canto superior esquerdo
                matrix[j][i] = box_symb[0]
        elif j == 0 and i == dimension - 1: # Canto superior direito
            matrix[j][i] = box_symb[1]
        elif j == dimension - 1 and i == 0: # Canto inferior esquerdo
            matrix[j][i] = box_symb[4]
        elif j == dimension - 1 and i == dimension - 1: # Canto inferior direito
            matrix[j][i] = box_symb[5]
        elif j == 0 or j == dimension - 1: # Lados superior e inferior
            matrix[j][i] = box_symb[3]*2
        elif i == 0 or i == dimension - 1: # Lados esquerdo e direito
            matrix[j][i] = box_symb[2]
        elif j == pos_init and i == pos_init: # Partícula
            matrix[j][i] = box_symb[6] + " "
        else: # Restante da matriz em branco
            matrix[j][i] = " "*2

# Os elementos dos lados superior e inferior e os elementos "em branco" em toda a matriz estão multiplicados por 2 para 
# manter a proporcionalidade no terminal, onde a altura é aprox. duas vezes maior que a largura. 
# Como a largura agora é o dobro da original, para compensar na posição da partícula sempre será adicionado um espaço em branco.
 
draw(matrix) # Printar a partícula na posição inicial
input()
while steps < mov: # Loop para mudar a posição da partícula
    p = random() # Número aleatório entre 0 e 1
    loc_init_part = [y,x]
    matrix[y][x] = " "*2
    # Se a partícula estiver longe das bordas:
    if 1 < x < dimension - 2 and 1 < y < dimension - 2: 
        if p <= 0.25:
            y += 1
        elif 0.25 < p <= 0.5:
            y -= 1
        elif 0.5 < p <= 0.75:
            x += 1
        else:
            x -= 1
    # Se a partícula estiver na borda esquerda e de cima:
    elif x == 1 and y == 1:
        if p <= 0.25:
            y += 1
        elif 0.25 < p <= 0.5:
            x += 1
    # Se a partícula estiver na borda esquerda e de baixo:
    elif x == 1 and y == dimension - 2:
        if p <= 0.25:
            y -= 1
        elif 0.25 < p <= 0.5:
            x += 1
    # Se a partícula estiver na borda direita e de cima:
    elif x == dimension - 2 and y == 1:
        if p <= 0.25:
            y += 1
        elif 0.25 < p <= 0.50:
            x -= 1
    # Se a partícula estiver na borda direita e de baixo:
    elif x == dimension - 2 and y == dimension - 2:
        if p <= 0.25:
            y -= 1
        elif 0.25 < p <= 0.50:
            x -= 1
    # Se a partícula estiver na borda esquerda e longe das bordas de cima e baixo:
    elif x == 1: 
        if p <= 0.25:
            y += 1
        elif 0.25 < p <= 0.50:
            y -= 1
        elif 0.50 < p <= 0.75:
            x += 1
    # Se a partícula estiver na borda direita e longe das de cima e baixo:
    elif x == dimension - 2: 
        if p <= 0.25:
            y += 1
        elif 0.25 < p <= 0.50:
            y -= 1
        elif 0.50 < p <= 0.75:
            x -= 1
    # Se a partícula estiver na borda de baixo e longe das demais:
    elif y == dimension - 2:
        if p <= 0.25:
            y -= 1
        elif 0.25 < p <= 0.50:
            x -= 1
        elif 0.50 < p <= 0.75:
            x += 1
    # Se a partícula estiver na borda de cima e longe das demais:
    elif y == 1:
        if p <= 0.25:
            y += 1
        elif 0.25 < p <= 0.50:
            x -= 1
        elif 0.50 < p <= 0.75:
            x += 1
    if x == 1 and y == 1:
        matrix[y][x] = box_symb[8] + " "
    elif x == dimension - 2 and y == 1:
        matrix[y][x] = " " + box_symb[8]
    elif x == dimension - 2 and y == dimension - 2:
        matrix[y][x] = " " + box_symb[7]
    elif x == 1 and y == dimension - 2:
        matrix[y][x] = box_symb[7] + " "
    elif x == 1:
        matrix[y][x] = box_symb[6] + " "
    elif x == dimension - 2:
        matrix[y][x] = " " + box_symb[6]
    else:
        matrix[y][x] = box_symb[6] + " "
    loc_fin_part = [y,x]
    if loc_fin_part != loc_init_part:
        steps += 1
    time.sleep(tm)
    draw(matrix)
input()

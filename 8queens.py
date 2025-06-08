# define o tamanho do tabuleiro (nesse caso 8x8)
N = 8
board = [[0] * N for _ in range(N)]

# printa o resultado
def print_solution(board):
    for row in board:
        print(' '.join('Q' if x else '.' for x in row))
    print()  # printa uma linha vazia pra ficar melhor de ver

# func pra checar se uma rainha pode ser colocada no tabuleiro[row][col]
def is_safe(board, row, col):
    # Check the column on the left
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # checa na diagonal superior esquerda
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # checa na diagonal inferior esquerda
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # a posicao eh valida pra colocar uma rainha
    return True

# func recursiva pra resolver o nqueens
def solve_nq_util(board, col):
    # caso base: se todas as rainhas tiverem posicionadas return true
    if col >= N:
        return True
    
    # considera essa coluna e tenta encaixar a rainha linha por linha
    for i in range(N):
        if is_safe(board, i, col):
            # encaixa a rainha na posicao board[i][col]
            board[i][col] = 1
            
            # recursividade pra encaixar o resto das rainhas
            if solve_nq_util(board, col + 1):
                return True
            
            # se nao der pra encaixar a rainha em board[i][col] entao da backtrack
            board[i][col] = 0
            print(f"backtrack from ({i}, {col})")
    
    # se a rainha nao encaixar em nenhuma linha nessa coluna retorna false
    return False

# func pra resolver nqueens usando backtracking
def solve_nq():
    if not solve_nq_util(board, 0):
        print("Solution does not exist")
        return False
    
    print_solution(board)
    return True

# executa
solve_nq()

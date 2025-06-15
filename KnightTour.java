public class KnightTour {
    
    // define o tamanho do tabuleiro
    private static final int N = 8;

    // todos os movimentos possiveis do cavalo
    private static final int[] movex = {2,1,-1,-2,-2,-1,1,2};
    private static final int[] movey = {1,2,2,1,-1,-2,-2,-1};

    // tabuleiro
    private int[][] tabuleiro;

    public KnightTour(){
        tabuleiro = new int[N][N];
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                tabuleiro[i][j] = -1;
            }
        }
    }

    // verifica se a posicao eh valida
    private boolean isValid(int x, int y){
        return (x >= 0 && x < N && y >= 0 && y < N && tabuleiro[x][y] == -1);
    }

    private boolean solveKnightTourUtil(int currentX, int currentY, int moveCount){
        int nextX, nextY;

        tabuleiro[currentX][currentY] = moveCount - 1;

        if (moveCount == N*N){
            return true; //solucao encontrada
        }

        for (int k = 0; k < 8; k++){
            nextX = currentX + movex[k];
            nextY = currentY + movey[k];

            if (isValid(nextX, nextY)){
                if (solveKnightTourUtil(currentX, currentY, moveCount + 1)){
                    return true;
                }
            }
        }

        tabuleiro[currentX][currentY] = -1; //backtrack
        return false;
    }

    public boolean solveKnightTour(int startX, int startY){
        if (!solveKnightTourUtil(startX, startY, 1)){
            System.out.println("solucao nao existe para o tabuleiro " + N + "x" + N + " começando em (" + startX + ", " + startY + ")");
            return false;
        } else {
            System.out.println("solucao encontrada para o tabuleiro " + N + "x" + N + " começando em (" + startX + ", " + startY + ")");
        }

        return true;
    }

    public void printSolution() {
        System.out.println("\nsolucao do passeio do cavalo (" + N + "x" + N + "):");

        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                System.out.printf("%2d ", tabuleiro[i][j]);
            }

            System.out.println();
        }

        System.out.println("------------------------------------------------");
    }

    public static void main(String[] args) {

        KnightTour knight = new KnightTour();

        knight.solveKnightTour(0, 0); // comeca do canto superior esquerdo

        knight.printSolution();
    }

}

public class N_damas {
    public static void main(String[] args) {
        int n = 8;

        int[][] tabuleiro = new int[n][n];

        if (resolver(tabuleiro, 0)){
            System.out.println("tabuleiro " + n + "x" + n + " criado:");
            System.out.println(" ");

            for (int i = 0; i < n; i++){

                for (int j = 0; j<n; j++){
                    System.out.print(tabuleiro[i][j] + " ");
                }

                System.out.println();
            }
        } else {
            System.out.println("nao foi possivel encontrar uma solucao com backtracking");
        }
    }

    static boolean resolver(int[][] tabuleiro, int coluna){
        
        int n = tabuleiro.length;

        if (coluna == n){
            return true;
        }

        for (int linha = 0; linha < n; linha++){
            if (podeColocar(tabuleiro, linha, coluna)){
                tabuleiro[linha][coluna] = 1;

                if (resolver(tabuleiro, coluna+1)){
                    return true;
                }

                //backtracking
                System.out.println("backtrack de: (" + linha + ", " + coluna + ")");
                tabuleiro[linha][coluna] = 0;
            }
        }

        //caso base de fracasso
        return false;
    }

    static boolean podeColocar(int[][] tabuleiro, int linha, int coluna){
        
        for (int j = 0; j < coluna; j++){

            if (tabuleiro[linha][j] == 1){

                return false;
            }
        }

        for(int i = linha, j = coluna; i >= 0 && j >=0; i--, j--){
                if (tabuleiro[i][j] == 1){
                    return false;
                }
            }

        for(int i = linha, j = coluna; i < tabuleiro.length && j >= 0; i++, j--){
                
                if (tabuleiro[i][j] == 1){

                    return false;
                }
            }

            return true;
    }
}
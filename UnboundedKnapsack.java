import java.util.*;

public class UnboundedKnapsack {
    
    public static class Result{
        int maxValue;
        List<Integer> chosenItems;

        Result(int maxValue, List<Integer> chosenItems){
            this.maxValue = maxValue;
            this.chosenItems = chosenItems;
        }
    }

    public static Result unboundedKnapsack(int[] weights, int[] values, int capacity, boolean debug){
        int n = weights.length;
        int[] dp = new int[capacity + 1];
        int[] prevChoice = new int[capacity + 1];
        Arrays.fill(prevChoice, -1);

        for(int w = 1; w <= capacity; w++){
            for(int i = 0; i < n; i++){

                // aqui decide usar um item de novo se valer a pena
                if(weights[i] <= w && dp[w - weights[i]] + values[i] > dp[w]){
                    dp[w] = dp[w - weights[i]] + values[i];
                    prevChoice[w] = i;
                }
            }

            if (debug) {
                System.out.printf("w=%d: %s\n", w, Arrays.toString(Arrays.copyOf(dp, Math.min(dp.length, 60))));
            }
        }

        List<Integer> chosen = new ArrayList<>();
        int w = capacity;
        
        //aqui reconstroi a lista de itens usados repetidamente
        while (w > 0 && prevChoice[w] != -1){
            int i = prevChoice[w];
            chosen.add(i);
            w -= weights[i];
        }

        Collections.reverse(chosen);
        return new Result(dp[capacity], chosen);
    }


    public static void main(String[] args) {
        
        int[] weights = {5,3,4};
        int[] values = {10,4,7};
        int capacity = 10;
        boolean debug = false;

        Result result = unboundedKnapsack(weights, values, capacity, debug);

        System.out.println("valor maximo obtido: " + result.maxValue);
        System.out.print("itens escolhidos (indices 0-based, repeticoes possiveis): " + result.chosenItems + "\n");

        System.out.print("pesos -> ");
        for (int i : result.chosenItems){
            System.out.println(weights[i] + " ");
        }

        System.out.print("\nvalores -> ");
        for (int i : result.chosenItems){
            System.out.println(values[i] + " ");
        }
    }
}

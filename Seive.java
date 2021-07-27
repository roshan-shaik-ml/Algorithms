import java.util.*;

public class Seive {
    
    public static void main(String[] args) {
        
        int N = 100000;
        boolean [] prime = new boolean[N+1];
        Arrays.fill(prime, Boolean.TRUE);

        ArrayList<Integer> primeNumbers = new ArrayList<Integer>();

        for(int number = 2; number <= Math.sqrt(N); number++) {

            if (prime[number] == true) {
                

                for(int next = number * number; next <= N; next += number ) {
                    
                    prime[next] = false;
                }
            }
        }
        for(int index = 2; index < prime.length; index++) {
                
            if(prime[index] == true) {

                primeNumbers.add(index);
            }
        }
        for(int index = 0; index < primeNumbers.size(); index++) {

            System.out.print(primeNumbers.get(index) + " ");
        }
    }
}

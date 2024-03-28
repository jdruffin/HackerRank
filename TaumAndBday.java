import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class TaumAndBdayResult {

    /*
     * Complete the 'taumBday' function below.
     *
     * The function is expected to return a LONG_INTEGER.
     * The function accepts following parameters:
     * 1. INTEGER b
     * 2. INTEGER w
     * 3. INTEGER bc
     * 4. INTEGER wc
     * 5. INTEGER z
     */

    public static long taumBday(int b, int w, int bc, int wc, int z) {
        // Write your code here
        long minCostWhite = Math.min(wc, bc + z);
        long minCostBlack = Math.min(bc, wc + z);

        return (minCostBlack * b) + (minCostWhite * w);
    }

}

public class TaumAndBday {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter bufferedWriter = new BufferedWriter(new
        // FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                int b = Integer.parseInt(firstMultipleInput[0]);

                int w = Integer.parseInt(firstMultipleInput[1]);

                String[] secondMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                int bc = Integer.parseInt(secondMultipleInput[0]);

                int wc = Integer.parseInt(secondMultipleInput[1]);

                int z = Integer.parseInt(secondMultipleInput[2]);

                long result = TaumAndBdayResult.taumBday(b, w, bc, wc, z);

                System.out.println(result);

                // bufferedWriter.write(String.valueOf(result));
                // bufferedWriter.newLine();

            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        // bufferedWriter.close();
    }
}

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

class KaprekarNumbersResult {

    /*
     * Complete the 'kaprekarNumbers' function below.
     *
     * The function accepts following parameters:
     * 1. INTEGER p
     * 2. INTEGER q
     */

    public static void kaprekarNumbers(int p, int q) {
        StringBuilder result = new StringBuilder();
        for (int i = p; i <= q; i++) {
            double squaredValue= Math.pow(i, 2);;
            int r = (int) (Math.log10(i) + 1);

            double rightValue = (squaredValue) % ( Math.pow(10, r));
            double leftValue = Math.floor((squaredValue) / ( Math.pow(10, r)));

            if (leftValue + rightValue == i) {
                result.append(i + " ");
            }
        }
        System.out.println(result.length() == 0 ? "INVALID RANGE" : result);
    }
}

public class KaprekarNumbers {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int p = Integer.parseInt(bufferedReader.readLine().trim());

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        KaprekarNumbersResult.kaprekarNumbers(p, q);

        bufferedReader.close();
    }
}

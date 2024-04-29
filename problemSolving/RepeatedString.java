package HackerRank;

import java.io.*;

class Result {

    /*
     * Complete the 'repeatedString' function below.
     *
     * The function is expected to return a LONG_INTEGER.
     * The function accepts following parameters:
     * 1. STRING s
     * 2. LONG_INTEGER n
     */

    public static long repeatedString(String s, long n) {
        long aCount = s.chars().filter(ch -> ch == 'a').count();

        long returnValue = aCount * (n / s.length());
        System.out.println("first pass" + returnValue);

        long mod = n % s.length();

        long aRemainder = s.substring(0, (int) mod)
                .chars().filter(ch -> ch == 'a')
                .count();
        System.out.println("aRemainder" + aRemainder);

        returnValue = returnValue + aRemainder;

        System.out.println("returnValue" + returnValue);

        return returnValue;
    }

}

public class RepeatedString {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter bufferedWriter = new BufferedWriter(new
        // FileWriter(System.getenv("OUTPUT_PATH")));SA

        String s = bufferedReader.readLine();

        long n = Long.parseLong(bufferedReader.readLine().trim());

        long result = Result.repeatedString(s, n);
        System.out.println(result);

        // bufferedWriter.write(String.valueOf(result));
        // bufferedWriter.newLine();

        bufferedReader.close();
        // bufferedWriter.close();
    }
}

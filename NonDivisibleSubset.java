package HackerRank;

import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class NonDivisibleSubsetResult {
    /*
     * Complete the 'nonDivisibleSubset' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     * 1. INTEGER k
     * 2. INTEGER_ARRAY s
     */

    public static int nonDivisibleSubset(int k, List<Integer> s) {
        for (int i = 0; i < s.size(); i++) {
            s.set(i, s.get(i) % k);
        }

        List<Integer> frequencies = new ArrayList<Integer>();
        for (int i = 0; i < k; i++) {
            frequencies.add(Collections.frequency(s, i));
        }

        int sumCount = Math.min(frequencies.get(0), 1);
        for (int i = 1; i <= (frequencies.size() - 1) / 2; i++) {
            sumCount = sumCount + Math.max(frequencies.get(i), frequencies.get(frequencies.size() - i));
        }

        if (k % 2 == 0) {
            sumCount = sumCount + Math.min(frequencies.get(frequencies.size() / 2), 1);
        }

        return sumCount;
    }
}

public class NonDivisibleSubset {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter bufferedWriter = new BufferedWriter(new
        // FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int k = Integer.parseInt(firstMultipleInput[1]);

        List<Integer> s = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int result = NonDivisibleSubsetResult.nonDivisibleSubset(k, s);
        System.out.println(result);

        // bufferedWriter.write(String.valueOf(result));
        // bufferedWriter.newLine();

        // bufferedReader.close();
        // bufferedWriter.close();
    }
}

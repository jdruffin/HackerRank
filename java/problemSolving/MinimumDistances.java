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

class MinimumDistancesResult {

    /*
     * Complete the 'minimumDistances' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY a as parameter.
     */

    public static int minimumDistances(List<Integer> a) {
        // Write your code here
        Set<Integer> distinctValues = new HashSet<>(a);
        List<Integer> minValues = new ArrayList<>();
        for (Integer distinctValue : distinctValues) {
            int currPosition = a.indexOf(distinctValue);
            List<Integer> positions = new ArrayList<>();

            positions.add(currPosition);
            while (currPosition < a.lastIndexOf(distinctValue)) {
                currPosition = a.subList(currPosition + 1, a.size()).indexOf(distinctValue) + currPosition + 1;
                positions.add(currPosition);
            }

            int diff = Integer.MAX_VALUE;
            for (int i = 0; i < positions.size() - 1; i++) {
                if (positions.get(i + 1) - positions.get(i) < diff) {
                    diff = positions.get(i + 1) - positions.get(i);
                }
            }
            minValues.add(diff);
        }

        Collections.sort(minValues);

        return minValues.get(0) == Integer.MAX_VALUE ? -1 : minValues.get(0);
    }
}

public class MinimumDistances {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> a = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int result = MinimumDistancesResult.minimumDistances(a);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

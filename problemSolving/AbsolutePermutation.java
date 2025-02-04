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

class AbsolutePermutationResult {

    /*
     * Complete the 'absolutePermutation' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     * 1. INTEGER n
     * 2. INTEGER k
     */

    public static List<Integer> absolutePermutation(int n, int k) {
        // Write your code here
        List<Integer> range = new ArrayList<>();
        List<Integer> returnList = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            range.add(i);
        }

        if(k == 0){
            return range;
        }

        if(n%k != 0){
            return Arrays.asList(-1);
        }

        for (int i = 1; i <= n; i++) {
            if(range.contains(i-k) && !returnList.contains(i-k)) {
                returnList.add(i-k);
                continue;
            }
            else if(range.contains(i+k)&& !returnList.contains(i+k)) {
                returnList.add(i+k);
                continue;
            }
            else {
                return Arrays.asList(-1);
            }

        }

        return returnList;

    }

}

public class AbsolutePermutation {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                int n = Integer.parseInt(firstMultipleInput[0]);

                int k = Integer.parseInt(firstMultipleInput[1]);

                List<Integer> result = AbsolutePermutationResult.absolutePermutation(n, k);
                System.out.println(result);
                bufferedWriter.write(
                result.stream()
                .map(Object::toString)
                .collect(joining(" "))
                + "\n"
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

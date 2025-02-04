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

class GridSearchResult {

    /*
     * Complete the 'gridSearch' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     * 1. STRING_ARRAY G
     * 2. STRING_ARRAY P
     */

    public static String gridSearch(List<String> G, List<String> P) {
        // Write your code here
        boolean skipIteration = false;
        for (int row = 0; row <= G.size() - P.size(); row++) {
            for (int col = 0; col <= G.get(0).length() - P.get(0).length(); col++) {
                skipIteration = false;

                for (int patternRow = 0; patternRow < P.size(); patternRow++) {
                    if (skipIteration) {
                        break;
                    }
                    for (int patternCol = 0; patternCol < P.get(0).length(); patternCol++) {
                        if (G.get(row + patternRow).charAt(col + patternCol) != P.get(patternRow).charAt(patternCol)) {
                            skipIteration = true;
                            break;
                        }
                        if (patternRow == P.size() - 1 && patternCol == P.get(0).length() - 1) {
                            return "YES";
                        }
                    }
                }
            }
        }
        return "NO";
    }

}

public class GridSearch {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                int R = Integer.parseInt(firstMultipleInput[0]);

                int C = Integer.parseInt(firstMultipleInput[1]);

                List<String> G = IntStream.range(0, R).mapToObj(i -> {
                    try {
                        return bufferedReader.readLine();
                    } catch (IOException ex) {
                        throw new RuntimeException(ex);
                    }
                })
                        .collect(toList());

                String[] secondMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                int r = Integer.parseInt(secondMultipleInput[0]);

                int c = Integer.parseInt(secondMultipleInput[1]);

                List<String> P = IntStream.range(0, r).mapToObj(i -> {
                    try {
                        return bufferedReader.readLine();
                    } catch (IOException ex) {
                        throw new RuntimeException(ex);
                    }
                })
                        .collect(toList());

                String result = GridSearchResult.gridSearch(G, P);
                System.out.println(result);

                bufferedWriter.write(result);
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

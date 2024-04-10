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

class SurfaceAreaResult {

    /*
     * Complete the 'surfaceArea' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY A as parameter.
     */

    public static int surfaceArea(List<List<Integer>> A) {
        // Write your code here
        int totalFaces = 0;
        int stackDuplicates = 0;
        int rowDuplicates = 0;
        int colDuplicates = 0;

        for (List<Integer> row : A) {
            for (Integer height : row) {
                totalFaces = totalFaces + (6 * height);
                stackDuplicates = stackDuplicates + ((height - 1) * 2);
            }
        }

        for (List<Integer> list : A) {
            for (int i = 0; i < list.size() - 1; i++) {
                rowDuplicates = rowDuplicates + (2 * Math.min(list.get(i), list.get(i + 1)));
            }
        }

        for (int i = 0; i < A.size() - 1; i++) {
            for (int j = 0; j < A.get(i).size(); j++) {
                colDuplicates = colDuplicates + (2 * Math.min(A.get(i).get(j), A.get(i + 1).get(j)));
            }
        }

        return totalFaces - stackDuplicates - rowDuplicates - colDuplicates;
    }

}

public class SurfaceArea {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter bufferedWriter = new BufferedWriter(new
        // FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int H = Integer.parseInt(firstMultipleInput[0]);

        int W = Integer.parseInt(firstMultipleInput[1]);

        List<List<Integer>> A = new ArrayList<>();

        IntStream.range(0, H).forEach(i -> {
            try {
                A.add(
                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                .map(Integer::parseInt)
                                .collect(toList()));
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int result = SurfaceAreaResult.surfaceArea(A);
        System.out.println(result);

        // bufferedWriter.write(String.valueOf(result));
        // bufferedWriter.newLine();

        bufferedReader.close();
        // bufferedWriter.close();
    }
}

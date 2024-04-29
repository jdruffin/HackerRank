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

class MatrixRotationResult {

    /*
     * Complete the 'matrixRotation' function below.
     *
     * The function accepts following parameters:
     * 1. 2D_INTEGER_ARRAY matrix
     * 2. INTEGER r
     */

    public static void matrixRotation(List<List<Integer>> matrix, int r) {
        // Write your code here
        int rows = matrix.size();
        int cols = matrix.get(0).size();
        int minSide = Math.min(rows, cols);
        int circles = minSide / 2;

        List<List<Integer>> newMatrix = new ArrayList<>();
        List<List<Integer>> finalArray = new ArrayList<>();
        for (int i = 0; i < rows; i++) {
            List<Integer> newSubMatrix = new ArrayList<>(matrix.get(i).stream().collect(Collectors.toList()));
            List<Integer> newSubMatrix2 = new ArrayList<>(newSubMatrix);
            newMatrix.add(newSubMatrix);
            finalArray.add(newSubMatrix2);
        }

        for (int i = 0; i < circles; i++) {
            int rotations = (r % ((2 * ((rows - (2*i)) + (cols - (2*i)))) - 4));
            for (int rotation = 0; rotation < rotations; rotation++) {
                for (int j = (0+i); j < (rows-i); j++) {
                    for (int k = (0+i); k < (cols-i); k++) {
                        boolean cond1 = j == i && k > i && k < (cols - i);
                        boolean cond2 = j == (rows - i - 1) && k >= i && k < (cols - i - 1);
                        boolean cond3 = k == i && j < (rows - i - 1) && j >= i;
                        boolean cond4 = k == (cols - i - 1) && j < (rows - i) && j > i;
                        boolean cond5 = rotation % 2 == 1;
                        if (rotation == rotations - 1) {
                            if (cond5) {
                                if (cond1) {
                                    finalArray.get(j).set(k - 1, newMatrix.get(j).get(k));
                                }
                                else if (cond2) {
                                    finalArray.get(j).set(k + 1, newMatrix.get(j).get(k));
                                }
                                else if (cond3) {
                                    finalArray.get(j + 1).set(k, newMatrix.get(j).get(k));
                                }
                                else if (cond4){
                                    finalArray.get(j - 1).set(k, newMatrix.get(j).get(k));
                                }
                            } else {
                                if (cond1) {
                                    finalArray.get(j).set(k - 1, matrix.get(j).get(k));
                                }
                                else if (cond2) {
                                    finalArray.get(j).set(k + 1, matrix.get(j).get(k));
                                }
                                else if (cond3) {
                                    finalArray.get(j + 1).set(k, matrix.get(j).get(k));
                                }
                                else if (cond4){
                                    finalArray.get(j - 1).set(k, matrix.get(j).get(k));
                                }
                            }
                        } else {
                            if (cond5) {
                                if (cond1) {
                                    matrix.get(j).set(k - 1, newMatrix.get(j).get(k));
                                }
                                else if (cond2) {
                                    matrix.get(j).set(k + 1, newMatrix.get(j).get(k));
                                }
                                else if (cond3) {
                                    matrix.get(j + 1).set(k, newMatrix.get(j).get(k));
                                }
                                else if (cond4) {
                                    matrix.get(j - 1).set(k, newMatrix.get(j).get(k));
                                }
                            } else {
                                if (cond1) {
                                    newMatrix.get(j).set(k - 1, matrix.get(j).get(k));
                                }
                                else if (cond2) {
                                    newMatrix.get(j).set(k + 1, matrix.get(j).get(k));
                                }
                                else if (cond3) {
                                    newMatrix.get(j + 1).set(k, matrix.get(j).get(k));
                                }
                                else if (cond4){
                                    newMatrix.get(j - 1).set(k, matrix.get(j).get(k));
                                }
                            }
                        }

                    }
                }
            }
        }

        for (List<Integer> list : finalArray) {
            StringBuilder row = new StringBuilder();
            for (Integer value : list) {
                row.append(value + " ");
            }
            System.out.println(row);
        }
    }
}

public class MatrixRotation {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int m = Integer.parseInt(firstMultipleInput[0]);

        int n = Integer.parseInt(firstMultipleInput[1]);

        int r = Integer.parseInt(firstMultipleInput[2]);

        List<List<Integer>> matrix = new ArrayList<>();

        IntStream.range(0, m).forEach(i -> {
            try {
                matrix.add(
                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                .map(Integer::parseInt)
                                .collect(toList()));
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        MatrixRotationResult.matrixRotation(matrix, r);

        bufferedReader.close();
    }
}

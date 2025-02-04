import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'bomberMan' function below.
     *
     * The function is expected to return a STRING_ARRAY.
     * The function accepts following parameters:
     * 1. INTEGER n
     * 2. STRING_ARRAY grid
     */

    public static List<String> bomberMan(int n, List<String> grid) {
        // Write your code here
        for (int i = 0; i < grid.size(); i++) {
            grid.set(i, grid.get(i).replaceAll("O", "3"));
        }

        int iterations = 0;
        if (n == 0 || n == 1) {
            iterations = 0;
        } else if (n % 2 == 0) {
            iterations = 2;
        } else if (n == 3 || n % 4 == 3) {
            iterations = 3;
        } else if (n == 5 || n % 4 == 1) {
            iterations = 5;
        }

        for (int i = 0; i < iterations; i++) {
            if (i == 0) {
                decrementBombs(grid);
            } else if (i % 2 == 1) {
                decrementBombs(grid);
                explodeBombs(grid);
                plantBombs(grid);
            } else if (i % 2 == 0) {
                decrementBombs(grid);
                explodeBombs(grid);
            }
        }

        for (int i = 0; i < grid.size(); i++) {
            grid.set(i, grid.get(i).replaceAll("3|2|1", "O"));
        }
        return grid;
    }

    public static List<String> decrementBombs(List<String> grid) {
        for (int i = 0; i < grid.size(); i++) {
            grid.set(i, grid.get(i).replaceAll("1", "*"));
            grid.set(i, grid.get(i).replaceAll("2", "1"));
            grid.set(i, grid.get(i).replaceAll("3", "2"));
        }
        return grid;
    }

    public static List<String> explodeBombs(List<String> grid) {
        for (int row = 0; row < grid.size(); row++) {
            for (int col = 0; col < grid.get(0).length(); col++) {
                if (grid.get(row).charAt(col) == '*') {
                    if (row >= 1 && grid.get(row - 1).charAt(col) != '*') {
                        grid.set(row - 1, grid.get(row - 1).substring(0, col) + "." +
                                grid.get(row - 1).substring(col + 1));
                    }
                    if (row <= grid.size() - 2 && grid.get(row + 1).charAt(col) != '*') {
                        grid.set(row + 1, grid.get(row + 1).substring(0, col) + "." +
                                grid.get(row + 1).substring(col + 1));
                    }
                    if (col >= 1 && grid.get(row).charAt(col - 1) != '*') {
                        grid.set(row, grid.get(row).substring(0, col - 1) + "." +
                                grid.get(row).substring(col));
                    }
                    if (col <= grid.get(0).length() - 2 && grid.get(row).charAt(col + 1) != '*') {
                        grid.set(row, grid.get(row).substring(0, col + 1) + "." +
                                grid.get(row).substring(col + 2));
                    }
                    grid.set(row, grid.get(row).substring(0, col) + "." +
                            grid.get(row).substring(col + 1));
                }
            }
        }
        return grid;
    }

    public static List<String> plantBombs(List<String> grid) {
        for (int i = 0; i < grid.size(); i++) {
            grid.set(i, grid.get(i).replaceAll("\\.", "3"));
        }
        return grid;
    }

}

public class BomberMan {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int r = Integer.parseInt(firstMultipleInput[0]);

        int c = Integer.parseInt(firstMultipleInput[1]);

        int n = Integer.parseInt(firstMultipleInput[2]);

        List<String> grid = IntStream.range(0, r).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .collect(toList());

        List<String> result = Result.bomberMan(n, grid);

        bufferedWriter.write(
                result.stream()
                        .collect(joining("\n"))
                        + "\n");

        bufferedReader.close();
        bufferedWriter.close();
    }
}

import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'twoPluses' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING_ARRAY grid as parameter.
     */

    public static int twoPluses(List<String> grid) {
        // Write your code here
        List<List<Integer>> iterationGrid = new ArrayList<>();
        for (int row = 0; row < grid.size(); row++) {
            List<Integer> iterationRow = new ArrayList<>();
            for (int col = 0; col < grid.get(0).length(); col++) {
                if (grid.get(row).charAt(col) == 'G') {
                    int currArea = 1;
                    int iteration = 1;
                    while (canPlusExpand(grid, row, col, iteration) == true) {
                        currArea = currArea + 4;
                        iteration = iteration + 1;
                    }
                    iterationRow.add(iteration - 1);
                } else {
                    iterationRow.add(-1);
                }
            }
            iterationGrid.add(iterationRow);
        }

        List<Integer> finalAreas = new ArrayList<>();
        for (int row = 0; row < iterationGrid.size(); row++) {
            for (int col = 0; col < iterationGrid.get(0).size(); col++) {
                if (iterationGrid.get(row).get(col) != -1) {
                    for (int plus1Offset = 0; plus1Offset <= iterationGrid.get(row).get(col); plus1Offset++) {

                        for (int row2 = 0; row2 < iterationGrid.size(); row2++) {
                            for (int col2 = 0; col2 < iterationGrid.get(0).size(); col2++) {
                                if (iterationGrid.get(row2).get(col2) != -1) {
                                    for (int plus2Offset = 0; plus2Offset <= iterationGrid.get(row2)
                                            .get(col2); plus2Offset++) {

                                        if (row != row2 && col != col2) {
                                            if (plusesDontOverlap(iterationGrid, row, col, row2, col2, plus1Offset,
                                                    plus2Offset)) {

                                                finalAreas.add((1
                                                        + (4 * (iterationGrid.get(row).get(col) - plus1Offset)))
                                                        * (1 + (4
                                                                * (iterationGrid.get(row2).get(col2) - plus2Offset))));
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        Collections.sort(finalAreas, Collections.reverseOrder());
        return finalAreas.get(0);
    }

    public static boolean canPlusExpand(List<String> grid, int row, int col, int iterations) {
        if (!(row - iterations >= 0 && grid.get(row - iterations).charAt(col) == 'G')) {
            return false;
        }
        if (!(row + iterations < grid.size() && grid.get(row + iterations).charAt(col) == 'G')) {
            return false;
        }
        if (!(col - iterations >= 0 && grid.get(row).charAt(col - iterations) == 'G')) {
            return false;
        }
        if (!(col + iterations < grid.get(0).length() && grid.get(row).charAt(col + iterations) == 'G')) {
            return false;
        }
        return true;
    }

    public static boolean plusesDontOverlap(List<List<Integer>> iterationGrid, int row, int col, int row2, int col2,
            int plus1Offset, int plus2Offset) {
        List<String> list1 = new ArrayList<>();
        List<String> list2 = new ArrayList<>();

        list1.add(row + "" + col);
        for (int i = 1; i <= iterationGrid.get(row).get(col) - plus1Offset; i++) {
            list1.add(row + i + "" + col);
            list1.add(row - i + "" + col);
            list1.add(row + "" + (col + i));
            list1.add(row + "" + (col - i));
        }

        list2.add(row2 + "" + col2);
        for (int i = 1; i <= iterationGrid.get(row2).get(col2) - plus2Offset; i++) {
            list2.add(row2 + i + "" + col2);
            list2.add(row2 - i + "" + col2);
            list2.add(row2 + "" + (col2 + i));
            list2.add(row2 + "" + (col2 - i));
        }

        for (String string : list2) {
            if (list1.contains(string)) {
                return false;
            }
        }
        return true;
    }
}

public class TwoPluses {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int m = Integer.parseInt(firstMultipleInput[1]);

        List<String> grid = IntStream.range(0, n).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .collect(toList());

        int result = Result.twoPluses(grid);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

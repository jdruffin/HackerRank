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

class BomberManResult {

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
        for (String string : grid) {
            string.replaceAll("O", "2");
        }

        for (int i = 1; i < n; i++) {
            if (i %2 == 1){

            }
            else{

            }

        }

    //     for (int i = 0; i < n; i++) {
    //         if (n % 3 == 1) {
    //             for (String row : grid) {
    //                 row.replaceAll("R", "O");
    //             }
    //         }
    //         if (n % 3 == 2) {
    //             for (String row : grid) {
    //                 row.replaceAll(".", "R");
    //             }
    //         }
    //         if (n % 3 == 0) {
    //             for (int row = 0; row < grid.size(); row++) {
    //                 for (int col = 0; col < grid.get(0).length(); col++) {
    //                     if (grid.get(row).charAt(col) == 'O') {
    //                         // explosion time (:
    //                         if (row + 1 <= grid.size()) {// bottom row

    //                             if (col + 1 <= grid.get(0).length()) {// right col
    //                                 String afterExplosionUp = grid.get(row - 1).substring(0, col) + '.'
    //                                         + grid.get(row - 1).substring(col + 1);
    //                                 grid.set(row - 1, afteafterExplosionUpExplosion);

    //                                 String afterExplosionLeft = grid.get(row).substring(0, col) + '.'
    //                                         + grid.get(row).substring(col - 1);
    //                                 grid.set(row, afterExplosionLeft);

    //                             }
    //                             if (col - 1 >= 0) {// left col
                                    
    //                             }

    //                         }
    //                         if (row - 1 >= 0) {// top row
                                
    //                         }
    //                         if (col + 1 <= grid.get(0).length()) {// right col
                                
    //                         }
    //                         if (col - 1 >= 0) {// left col
                                
    //                         }
    //                     }
    //                 }
    //             }
    //         }
    //     }
    // }
    }

public class BomberMan {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter bufferedWriter = new BufferedWriter(new
        // FileWriter(System.getenv("OUTPUT_PATH")));

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

        List<String> result = BomberManResult.bomberMan(n, grid);
        System.out.println(result);
        // bufferedWriter.write(
        // result.stream()
        // .collect(joining("\n"))
        // + "\n"
        // );

        bufferedReader.close();
        // bufferedWriter.close();
    }
}
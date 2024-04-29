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

class SparseArraysResult {

    /*
     * Complete the 'matchingStrings' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     * 1. STRING_ARRAY stringList
     * 2. STRING_ARRAY queries
     */

    public static List<Integer> matchingStrings(List<String> stringList, List<String> queries) {
        // Write your code here
        // List<Integer> count = new ArrayList<>();

        // for (String queryString : queries) {
        //     int currentCount = 0;
        //     for (String string : stringList) {
        //         int currentIndex = 0;

        //         while (currentIndex != -1) {
        //             currentIndex = string.indexOf(queryString, currentIndex+1);
        //             currentCount = currentCount + 1;
        //         }
        //     }
        //     count.add(currentCount);
        // }

        // return count;


        List<Integer> count = new ArrayList<>();

        for (String queryString : queries) {
            int currentCount = 0;

            for (String string : stringList) {
                if (string.equals(queryString)) {
                    currentCount = currentCount + 1;
                }
            }
            count.add(currentCount);
        }

        return count;
    }

}

public class SparseArrays {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter bufferedWriter = new BufferedWriter(new
        // FileWriter(System.getenv("OUTPUT_PATH")));

        int stringListCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> stringList = IntStream.range(0, stringListCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .collect(toList());

        int queriesCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> queries = IntStream.range(0, queriesCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .collect(toList());

        List<Integer> res = SparseArraysResult.matchingStrings(stringList, queries);
        System.out.println(res);

        // bufferedWriter.write(
        // res.stream()
        // .map(Object::toString)
        // .collect(joining("\n"))
        // + "\n"
        // );

        bufferedReader.close();
        // bufferedWriter.close();
    }
}

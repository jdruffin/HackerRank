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

class AlmostSortedResult {

    /*
     * Complete the 'almostSorted' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void almostSorted(List<Integer> arr) {
        // Write your code here
        if (arr.stream().sorted().collect(Collectors.toList()).equals(arr)) {
            System.out.println("yes");
            return;
        }

        int firstIndex = 0;
        int lastIndex = arr.size();
        int currMinValue = Integer.MIN_VALUE;
        int currMaxValue = Integer.MAX_VALUE;

        for (int i = 0; i < arr.size(); i++) {
            if (currMinValue > arr.get(i)) {
                firstIndex = i;
                break;
            }
            currMinValue = arr.get(i);
        }

        for (int i = arr.size() - 1; i >= 0; i--) {
            if (currMaxValue < arr.get(i)) {
                lastIndex = i;
                break;
            }
            currMaxValue = arr.get(i);
        }

        Collections.swap(arr, firstIndex - 1, lastIndex + 1);

        if (arr.stream().sorted().collect(Collectors.toList()).equals(arr)) {
            System.out.println("yes");
            System.out.println("swap " + (firstIndex - 1 + 1) + " " + (lastIndex + 1 + 1));
            return;
        }

        Collections.swap(arr, firstIndex - 1, lastIndex + 1);
        Collections.reverse(arr.subList(firstIndex - 1, lastIndex + 2));

        if (arr.stream().sorted().collect(Collectors.toList()).equals(arr)) {
            System.out.println("yes");
            System.out.println("reverse " + (firstIndex - 1 + 1) + " " + (lastIndex + 1 + 1));
            return;
        }

        System.out.println("no");
    }
}

public class AlmostSorted {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        AlmostSortedResult.almostSorted(arr);

        bufferedReader.close();
    }
}

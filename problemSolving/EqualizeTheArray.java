import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class EqualizeTheArrayResult {

    /*
     * Complete the 'equalizeArray' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static int equalizeArray(List<Integer> arr) {
        // Write your code her
        HashMap<Integer, Integer> frequencyMap = new HashMap<>();
        for (Integer integer : arr) {
            if (!frequencyMap.containsKey(integer)) {
                frequencyMap.put(integer, Collections.frequency(arr, integer));
            }
        }
        int maxValue = Collections.max(frequencyMap.values());
        return arr.size() - maxValue;
    }

}

public class EqualizeTheArray {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int result = EqualizeTheArrayResult.equalizeArray(arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

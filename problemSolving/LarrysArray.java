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

class LarrysArrayResult {

    /*
     * Complete the 'larrysArray' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts INTEGER_ARRAY A as parameter.
     */

    public static String larrysArray(List<Integer> A) {
        for (int i = 0; i < A.size(); i++) {
            if (A.get(i) != i+1){
                if(i + 2 < A.size()) {
                    while(A.get(i) != i+1){
                        if(A.indexOf(i+1) -2 < i){
                            Collections.rotate(A.subList(A.indexOf(i+1) -1, A.indexOf(i+1)+2), -1);

                        } else {
                            Collections.rotate(A.subList(A.indexOf(i+1) -2, A.indexOf(i+1)+1), -1);
                        }

                    }
                } else {
                    return "NO";
                }
            }
        }
        return "YES";
    }
}

public class LarrysArray {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                int n = Integer.parseInt(bufferedReader.readLine().trim());

                List<Integer> A = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList());

                String result = LarrysArrayResult.larrysArray(A);

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

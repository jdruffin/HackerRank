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

class BiggerIsGreaterResult {

    /*
     * Complete the 'biggerIsGreater' function below.
     *
     * The function is expected to return a STRING.
     * The function acc-epts STRING w as parameter.
     */

    // 834221
    // 841223

    public static String biggerIsGreater(String w) {
        // Write your code here

        char currValue = w.charAt(w.length() - 1);
        int index = w.length() - 1;

        List<Character> charsToBeSorted = new ArrayList<Character>();

        for (int i = w.length() - 1; i >= 0; i--) {
            if (w.charAt(i) >= currValue) {

                charsToBeSorted.add(w.charAt(i));
                currValue = w.charAt(i);
            } else {
                index = i;
                break;
            }
        }

        Collections.sort(charsToBeSorted);

        if (index == w.length() - 1) {
            return "no answer";
        } else {
            StringBuilder returnString = new StringBuilder();
            returnString.append(w.substring(0, index));

            for (int i = 0; i < charsToBeSorted.size(); i++) {
                if (((int) charsToBeSorted.get(i) > (int) w.charAt(index))) {
                    returnString.append(charsToBeSorted.get(i));
                    charsToBeSorted.set(i, w.charAt(index));
                    break;
                }
            }

            StringBuilder sb = new StringBuilder();
            for (Character ch : charsToBeSorted) {
                sb.append(ch);
            }

            returnString.append(sb.toString());

            return returnString.toString();
        }

    }

    public class BiggerIsGreater {
        public static void main(String[] args) throws IOException {
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

            int T = Integer.parseInt(bufferedReader.readLine().trim());

            IntStream.range(0, T).forEach(TItr -> {
                try {
                    String w = bufferedReader.readLine();

                    String result = BiggerIsGreaterResult.biggerIsGreater(w);

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
}
package HackerRank;

import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class AcmIcpcTeamResult {

    /*
     * Complete the 'acmTeam' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts STRING_ARRAY topic as parameter.
     */

    public static List<Integer> acmTeam(List<String> topic) {
        // Write your code here
        int numberOfTopics = topic.get(0).length();
        List<Integer> combinations = new ArrayList<>();

        for (int i = 0; i < topic.size(); i++) {
            for (int j = i + 1; j < topic.size(); j++) {
                int curValue = 0;
                for (int k = 0; k < numberOfTopics; k++) {
                    if (topic.get(i).charAt(k) == '1' || topic.get(j).charAt(k) == '1') {
                        curValue = curValue + 1;
                    }
                }
                combinations.add(curValue);
            }
        }

        List<Integer> frequencies = new ArrayList<Integer>();
        for (int i = 0; i <= numberOfTopics; i++) {
            frequencies.add(Collections.frequency(combinations, i));
        }

        List<Integer> returnList = new ArrayList<Integer>();
        returnList.add(Collections.max(combinations));
        returnList.add(frequencies.get(Collections.max(combinations)));

        return returnList;
    }

}

public class AcmIcpcTeam {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter bufferedWriter = new BufferedWriter(new
        // FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int m = Integer.parseInt(firstMultipleInput[1]);

        List<String> topic = IntStream.range(0, n).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .collect(toList());

        List<Integer> result = AcmIcpcTeamResult.acmTeam(topic);
        System.out.println(result);

        // bufferedWriter.write(
        // result.stream()
        // .map(Object::toString)
        // .collect(joining("\n"))
        // + "\n"
        // );

        bufferedReader.close();
        // bufferedWriter.close();
    }
}

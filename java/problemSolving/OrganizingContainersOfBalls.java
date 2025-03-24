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

class OrganizingContainersOfBallsResult {

    /*
     * Complete the 'organizingContainers' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts 2D_INTEGER_ARRAY container as parameter.
     */

    public static String organizingContainers(List<List<Integer>> containers) {
        // Write your code here
        long[] sortedContainerCounts = containers
                .stream()
                .mapToLong(container -> container.stream().mapToLong(Integer::longValue).sum())
                .sorted()
                .toArray();
        long[] sortedTypeCounts = IntStream
                .range(0, containers.size())
                .mapToLong(index -> containers
                        .stream()
                        .mapToLong(container -> container.get(index).longValue())
                        .sum())
                .sorted()
                .toArray();

        return Arrays.equals(sortedContainerCounts, sortedTypeCounts) ? "Possible" : "Impossible";
    }
}

public class OrganizingContainersOfBalls {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, q).forEach(qItr -> {
            try {
                int n = Integer.parseInt(bufferedReader.readLine().trim());

                List<List<Integer>> container = new ArrayList<>();

                IntStream.range(0, n).forEach(i -> {
                    try {
                        container.add(
                                Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                        .map(Integer::parseInt)
                                        .collect(toList()));
                    } catch (IOException ex) {
                        throw new RuntimeException(ex);
                    }
                });

                String result = OrganizingContainersOfBallsResult.organizingContainers(container);

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

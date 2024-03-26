package HackerRank;

import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'queensAttack' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     * 1. INTEGER n
     * 2. INTEGER k
     * 3. INTEGER r_q
     * 4. INTEGER c_q
     * 5. 2D_INTEGER_ARRAY obstacles
     */

    public static int queensAttack(int n, int k, int r_q, int c_q, List<List<Integer>> obstacles) {
        HashMap<Integer, Integer> closestObstacles = initObstacleMap(n, r_q, c_q);

        System.out.println(closestObstacles);

        for (List<Integer> obstacle : obstacles) {

            int x = obstacle.get(1) - c_q;
            int y = obstacle.get(0) - r_q;

            if (x >= 1 && y == 0) {
                int distance = distanceToQueen(obstacle, r_q, c_q, 0);
                if (closestObstacles.get(0) > distance) {
                    closestObstacles.put(0, distance);
                }
            }
            if (x >= 1 && y <= -1 && (Math.abs(x) == Math.abs(y))) {
                int distance = distanceToQueen(obstacle, r_q, c_q, 1);
                if (closestObstacles.get(1) > distance) {
                    closestObstacles.put(1, distance);
                }
            }
            if (x == 0 && y <= -1) {
                int distance = distanceToQueen(obstacle, r_q, c_q, 0);
                if (closestObstacles.get(2) > distance) {
                    closestObstacles.put(2, distance);
                }
            }
            if (x <= -1 && y <= -1 && (Math.abs(x) == Math.abs(y))) {
                int distance = distanceToQueen(obstacle, r_q, c_q, 1);
                if (closestObstacles.get(3) > distance) {
                    closestObstacles.put(3, distance);
                }
            }
            if (x <= -1 && y == 0) {
                int distance = distanceToQueen(obstacle, r_q, c_q, 0);
                if (closestObstacles.get(4) > distance) {
                    closestObstacles.put(4, distance);
                }
            }
            if (x <= -1 && y >= 1 && (Math.abs(x) == Math.abs(y))) {
                int distance = distanceToQueen(obstacle, r_q, c_q, 1);
                if (closestObstacles.get(5) > distance) {
                    closestObstacles.put(5, distance);
                }
            }
            if (x == 0 && y >= 1) {
                int distance = distanceToQueen(obstacle, r_q, c_q, 0);
                if (closestObstacles.get(6) > distance) {
                    closestObstacles.put(6, distance);
                }
            }
            if (x >= 1 && y >= 1 && (Math.abs(x) == Math.abs(y))) {
                int distance = distanceToQueen(obstacle, r_q, c_q, 1);
                if (closestObstacles.get(7) > distance) {
                    closestObstacles.put(7, distance);
                }
            }
        }

        int possibleMovments = 0;
        for (Map.Entry<Integer, Integer> set : closestObstacles.entrySet()) {
            possibleMovments = possibleMovments + set.getValue();
        }

        return possibleMovments;
    }

    public static HashMap<Integer, Integer> initObstacleMap(int size, int r_q, int c_q) {
        HashMap<Integer, Integer> closestObstacles = new HashMap<>(8);

        int right = size + -c_q;
        int down = r_q - 1;
        int left = c_q - 1;
        int up = size - r_q;

        closestObstacles.put(0, right);
        closestObstacles.put(1, Math.min(down, right));

        closestObstacles.put(2, down);
        closestObstacles.put(3, Math.min(down, left));

        closestObstacles.put(4, left);
        closestObstacles.put(5, Math.min(left, up));

        closestObstacles.put(6, up);
        closestObstacles.put(7, Math.min(up, right));

        return closestObstacles;
    }

    public static int distanceToQueen(List<Integer> obstacle, int r_q, int c_q, int directionality) {
        if (directionality == 0) {
            return Math.max(Math.abs(obstacle.get(0) - r_q) - 1, Math.abs(obstacle.get(1) - c_q) - 1);
        } else {
            return Math.abs(obstacle.get(0) - r_q) - 1;
        }
    }

}

public class QueensAttack {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter bufferedWriter = new BufferedWriter(new
        // FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int k = Integer.parseInt(firstMultipleInput[1]);

        String[] secondMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int r_q = Integer.parseInt(secondMultipleInput[0]);

        int c_q = Integer.parseInt(secondMultipleInput[1]);

        List<List<Integer>> obstacles = new ArrayList<>();

        IntStream.range(0, k).forEach(i -> {
            try {
                obstacles.add(
                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                .map(Integer::parseInt)
                                .collect(toList()));
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int result = Result.queensAttack(n, k, r_q, c_q, obstacles);

        System.out.println("REUSLT IS:" + result);

        // bufferedWriter.write(String.valueOf(result));
        // bufferedWriter.newLine();

        bufferedReader.close();
        // bufferedWriter.close();
    }
}

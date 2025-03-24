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

class Result {
    public static class Edge {
        private Vertex start;
        private Vertex end;
        private Integer weight;

        public Edge(Vertex startV, Vertex endV, Integer weight) {
            this.start = startV;
            this.end = endV;
            this.weight = weight;
        }

        public Vertex getStart() {
            return this.start;
        }

        public Vertex getEnd() {
            return this.end;
        }

        public Integer getWeight() {
            return this.weight;
        }
    }

    public static class Vertex {
        private ArrayList<Integer> fishTypes;
        private ArrayList<Edge> edges;

        public Vertex(ArrayList<Integer> fishTypes) {
            this.fishTypes = fishTypes;
            this.edges = new ArrayList<Edge>();
        }

        public void addEdge(Vertex endVertex, Integer weight) {
            this.edges.add(new Edge(this, endVertex, weight));
        }

        public ArrayList<Edge> getEdges() {
            return this.edges;
        }

        public ArrayList<Integer> getFishTypes() {
            return this.fishTypes;
        }
    }

    public static class Graph {
        private ArrayList<Vertex> vertices;

        public Graph() {
            this.vertices = new ArrayList<Vertex>();
        }

        public Vertex addVertex(ArrayList<Integer> fishTypes) {
            Vertex newVertex = new Vertex(fishTypes);
            this.vertices.add(newVertex);
            return newVertex;
        }

        public void addEdge(Vertex vertex1, Vertex vertex2, Integer weight) {

            vertex1.addEdge(vertex2, weight);

            vertex2.addEdge(vertex1, weight);
        }

        public ArrayList<Vertex> getVertices() {
            return this.vertices;
        }

    }

    /*
     * Complete the 'shop' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     * 1. INTEGER n
     * 2. INTEGER k
     * 3. STRING_ARRAY centers
     * 4. 2D_INTEGER_ARRAY roads
     */

    public static int shop(int n, int k, List<String> centers, List<List<Integer>> roads) {
        // Write your code here

        Graph map = new Graph();
        for (String center : centers) {
            ArrayList<Integer> fishTypes = new ArrayList<>();
            String[] stringFishTypes = center.split(" ");
            for (int i = 1; i < stringFishTypes.length; i++) {
                fishTypes.add(Integer.valueOf(stringFishTypes[i]));
            }
            map.addVertex(fishTypes);
        }

        // find all possible paths with no path taken twice the same direction that end at the last center
        // for each possible pair of paths, check if they include all different types of
        // fish
        // select pair with lowest higher distance

        return 3;
    }

}

public class SynchronousShopping {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int m = Integer.parseInt(firstMultipleInput[1]);

        int k = Integer.parseInt(firstMultipleInput[2]);

        List<String> centers = IntStream.range(0, n).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .collect(toList());

        List<List<Integer>> roads = new ArrayList<>();

        IntStream.range(0, m).forEach(i -> {
            try {
                roads.add(
                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                .map(Integer::parseInt)
                                .collect(toList()));
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int res = Result.shop(n, k, centers, roads);

        bufferedWriter.write(String.valueOf(res));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

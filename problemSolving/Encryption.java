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

class EncryptionResult {

    /*
     * Complete the 'encryption' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static String encryption(String s) {
        String removedSapces = s.replaceAll("\\s+", "");
        int characterCount = removedSapces.length();
        int columns = (int) Math.ceil(Math.sqrt(characterCount));
        int rows = (columns * (int) Math.floor(Math.sqrt(characterCount))) < characterCount ? columns
                : (int) Math.floor(Math.sqrt(characterCount));

        StringBuilder encryptedString = new StringBuilder("");

        if (characterCount % columns != 0) {
            for (int i = 0; i < characterCount % columns; i++) {
                for (int j = 0; j < rows; j++) {
                    encryptedString.append(removedSapces.charAt(i + (j * columns)));
                }
                encryptedString.append(" ");
            }

            for (int i = characterCount % columns; i < columns; i++) {
                for (int j = 0; j < rows - 1; j++) {
                    encryptedString.append(removedSapces.charAt(i + (j * columns)));
                }
                encryptedString.append(" ");

            }
        } else {
            for (int i = 0; i < columns; i++) {
                for (int j = 0; j < rows; j++) {
                    encryptedString.append(removedSapces.charAt(i + (j * columns)));
                }
                encryptedString.append(" ");

            }
        }

        return encryptedString.toString();
    }
}

public class Encryption {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        String s = bufferedReader.readLine();

        String result = EncryptionResult.encryption(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

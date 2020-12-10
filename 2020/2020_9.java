import static java.util.Arrays.copyOfRange;
import static java.util.Arrays.stream;

import java.io.File;
import java.io.IOException;
import java.util.HashSet;
import java.util.*;
import java.util.Set;

public class AdventOfCode {
    static ArrayList<Long> inputList = new ArrayList<>();
    static int PREAMBLE = 25;
    static long rogueNumber;

    public static void main(String[] args) throws IOException {
        File filePath = new File("/Users/vrashabhirde/Desktop/aoc/input.txt");
        Scanner input = new Scanner(filePath);
        readIntegersFromFile(input);
    }

    public static void readIntegersFromFile(Scanner scanner) {
        while (scanner.hasNext()) {
            inputList.add(Long.parseLong(scanner.nextLine()));
        }
        long[] inputArray = inputList.stream().mapToLong(i -> i).toArray();
        rogueNumber = rogueNumber(inputArray);
        System.out.println(rogueNumber);
        System.out.println(encryptionWeakness(inputArray));
    }

    static long rogueNumber(long[] input) {
        for (int i = 0; i < input.length - PREAMBLE; i++) {
            //For every 25 numbers, put all combinationSums in a set
            Set<Long> combinationSums = new HashSet<>();
            for (int j = i; j < i + PREAMBLE; j++) {
                for (int k = j + 1; k < i + PREAMBLE; k++) {
                    combinationSums.add(input[j] + input[k]);
                }
            }
            //check if number not present in set
            if (!combinationSums.contains(input[i + PREAMBLE])) {
                return input[i + PREAMBLE];
            }
        }
        return -1;
    }

    static long encryptionWeakness(long[] input) {
        for (int i = 2; i < input.length; i++) {
            for (int j = 0; j <= input.length - i; j++) {
                if (stream(input, j, j + i).sum() == rogueNumber) {
                    //create sliding window of numbers that sum to rogue using streams
                    long[] slidingWindow = copyOfRange(input, j, j + i);
                    long maxInWindow = stream(slidingWindow).max().getAsLong();
                    long minInWindow = stream(slidingWindow).min().getAsLong();
                    long result = maxInWindow + minInWindow;
                    return result;
                }
            }
        }
        return -1;

    }


}

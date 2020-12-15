import java.util.*;

public class AdventOfCode {

    static int[] input = new int[]{8, 0, 17, 4, 1, 12};
    static HashMap<Integer, Integer> lastSpokenMap = new HashMap<>();
    static int numberOfTurns = input.length + 1;
    static int lastSpokenNumber = 0;

    public static void main(String[] args) {
        for (int i = 0; i < input.length; i++) {
            lastSpokenMap.put(input[i], i);
        }
        //part1
        getLastSpokenNumber(2020);
        //part2
        getLastSpokenNumber(30000000);
    }

    private static void getLastSpokenNumber(int part) {
        while (numberOfTurns < part) {
            if (!lastSpokenMap.containsKey(lastSpokenNumber)) {
                lastSpokenMap.put(lastSpokenNumber, numberOfTurns - 1);
                lastSpokenNumber = 0;
            } else {
                int previousNumber = lastSpokenMap.get(lastSpokenNumber);
                lastSpokenMap.put(lastSpokenNumber, numberOfTurns - 1);
                lastSpokenNumber = numberOfTurns - 1 - previousNumber;
            }
            numberOfTurns++;
        }
        System.out.println(lastSpokenNumber);

    }
}

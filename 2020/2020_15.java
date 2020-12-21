import java.util.*;

public class AdventOfCode {

    static int[] INPUT = new int[]{8, 0, 17, 4, 1, 12};
    static int NUMBER_OF_TURNS = INPUT.length + 1;
    static int PART1_TIMES = 2020;
    static int PART2_TIMES = 30000000;
    static int lastSpokenNumber = 0;

    public static void main(String[] args) {
        HashMap<Integer, Integer> lastSpokenMap = new HashMap<>();
        for (int i = 0; i < INPUT.length; i++) {
            lastSpokenMap.put(INPUT[i], i);
        }
        //part1
        getLastSpokenNumber(PART1_TIMES, lastSpokenMap);
        //part2
        getLastSpokenNumber(PART2_TIMES, lastSpokenMap);
    }

    private static void getLastSpokenNumber(int part, HashMap<Integer, Integer> lastSpokenMap) {
        while (NUMBER_OF_TURNS < part) {
            if (!lastSpokenMap.containsKey(lastSpokenNumber)) {
                lastSpokenMap.put(lastSpokenNumber, NUMBER_OF_TURNS - 1);
                lastSpokenNumber = 0;
            } else {
                int previousNumber = lastSpokenMap.get(lastSpokenNumber);
                lastSpokenMap.put(lastSpokenNumber, NUMBER_OF_TURNS - 1);
                lastSpokenNumber = NUMBER_OF_TURNS - 1 - previousNumber;
            }
            NUMBER_OF_TURNS++;
        }
        System.out.println(lastSpokenNumber);

    }
}

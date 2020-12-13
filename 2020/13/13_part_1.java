import java.io.File;
import java.io.IOException;
import java.util.*;

import static java.util.Arrays.stream;

public class AdventOfCode {
    static int time;
    static int finalBus;

    public static void main(String[] args) throws IOException {
        File filePath = new File("/Users/vrashabhirde/Desktop/Desk/aoc1/input.txt");
        Scanner scanner = new Scanner(filePath);
        findEarliestBus(scanner);
    }

    public static void findEarliestBus(Scanner scanner) {
        time = Integer.parseInt(scanner.nextLine());
        String[] busID = scanner.nextLine().split(",");
        int closestBus = Integer.MAX_VALUE;
        for (String s : busID) {
            if (s.equals("x"))
                continue;
            int bus = Integer.parseInt(s);
            int nearestMultiple = (int) (bus * Math.floor(time / bus)) + bus;
            int diff = nearestMultiple - time;
            if (diff < closestBus) {
                closestBus = Math.min(closestBus, diff);
                finalBus = bus;
            }

        }
        System.out.println(finalBus * closestBus);
    }
}

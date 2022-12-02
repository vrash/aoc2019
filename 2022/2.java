import java.io.File;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        //part 1 - handwritten ugh
        HashMap<String, Integer> part1_map = new HashMap<>();
        part1_map.put("AX", 4);
        part1_map.put("AY", 8);
        part1_map.put("AZ", 3);
        part1_map.put("BX", 1);
        part1_map.put("BY", 5);
        part1_map.put("BZ", 9);
        part1_map.put("CX", 7);
        part1_map.put("CY", 2);
        part1_map.put("CZ", 6);

        //part 1
        Scanner scanner = new Scanner(new File("/Users/.../Desktop/Advent-Of-Code/2022/input.txt"));
        int sum = 0;
        int part2sum = 0;
        while (scanner.hasNext()) {
            String roundStrat = scanner.nextLine().toString().replaceAll("\\s", "");
            sum = sum + part1_map.get(roundStrat);
            part2sum = part2sum + simulateGame(roundStrat.split("")[0].toString(), roundStrat.split("")[1].toString());
        }
        System.out.println(sum);
        System.out.println(part2sum);
    }

    //part 2 - also ugh I miss python
    public static int simulateGame(String opponent, String outcome) {
        if (outcome.equals("X")) {
            if (opponent.equals("A"))
                return 3;
            else if (opponent.equals("B"))
                return 1;
            else return 2;
        } else if (outcome.equals("Y")) {
            if (opponent.equals("A"))
                return 4;
            else if (opponent.equals("B"))
                return 5;
            else return 6;

        } else {
            if (opponent.equals("A"))
                return 8;
            else if (opponent.equals("B"))
                return 9;
            else return 7;
        }
    }
}

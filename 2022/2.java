import java.io.File;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        //part 1
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
        //part 2
        HashMap<String, Integer> part2_map = new HashMap<>();
        part2_map.put("AX", 3);
        part2_map.put("AY", 4);
        part2_map.put("AZ", 8);
        part2_map.put("BX", 1);
        part2_map.put("BY", 5);
        part2_map.put("BZ", 9);
        part2_map.put("CX", 2);
        part2_map.put("CY", 6);
        part2_map.put("CZ", 7);
        Scanner scanner = new Scanner(new File("/Users/.../Desktop/Advent-Of-Code/2022/input.txt"));
        int part1sum = 0;
        int part2sum = 0;
        while (scanner.hasNext()) {
            String roundStrat = scanner.nextLine().toString().replaceAll("\\s", "");
            part1sum = part1sum + part1_map.get(roundStrat);
            part2sum = part2sum + part2_map.get(roundStrat);
        }
        System.out.println(part1sum);
        System.out.println(part2sum);
    }
}

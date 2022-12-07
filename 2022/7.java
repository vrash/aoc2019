import java.io.File;
import java.io.IOException;
import java.util.*;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(new File("/Users/../Desktop/Advent-Of-Code/2022/input.txt"));
        List<String> input = new ArrayList<>();
        while (scanner.hasNext()) {
            String word = scanner.nextLine();
            input.add(word);
        }

        Map<String, Integer> has = new HashMap<>();
        String currentDir = "";
        for (String line : input) {
            if (line.startsWith("$ cd ..")) currentDir = currentDir.substring(0, currentDir.lastIndexOf("/"));
            else if (line.startsWith("$ cd")) currentDir = currentDir + "/" + line.substring(5);
            else if (isNumeric(line.substring(0, 1))) {
                int size = Integer.parseInt(line.split(" ")[0]);
                String path = currentDir;
                while (path.length() > 0) {
                    has.merge(path, size, Integer::sum);
                    path = path.substring(0, path.lastIndexOf("/"));
                }
            }

        }
        Collection<Integer> sizes = has.values();
        int part1sum = 0;
        int part2 = Integer.MAX_VALUE;
        for (int i : sizes) {
            if (i < 100000)
                part1sum += i;
            if (i > (has.get("/") - 40000000))
                part2 = Math.min(part2, i);
        }
        System.out.println("part1: " + part1sum);
        System.out.println("part2: " + part2);
    }

    private static Pattern pattern = Pattern.compile("-?\\d+(\\.\\d+)?");

    public static boolean isNumeric(String strNum) {
        if (strNum == null) {
            return false;
        }
        return pattern.matcher(strNum).matches();
    }
}

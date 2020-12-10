import java.io.File;
import java.io.IOException;
import java.util.*;

public class AdventOfCode {
    static String[] inputLine;
    static int lowerbound;
    static int upperbound;
    static String key;
    static String pwd;
    static int validPasswordCount = 0;
    static File filePath = new File("/Users/vrashabhirde/Desktop/aoc/input.txt");

    public static void main(String[] args) throws IOException {
        //part 1
        Scanner scanner = new Scanner(filePath);
        while (scanner.hasNext()) {
            manipulateInput(scanner);
            int countChar = pwd.length() - pwd.replace(key, "").length();
            if (countChar >= lowerbound && countChar <= upperbound)
                validPasswordCount++;
        }
        System.out.println(validPasswordCount);

        //part2
        Scanner scanner2 = new Scanner(filePath);
        validPasswordCount = 0;
        while (scanner2.hasNext()) {
            manipulateInput(scanner2);
            final boolean isKeyAtLowerBound = pwd.charAt(lowerbound - 1) == key.charAt(0);
            final boolean isKeyAtUpperBound = pwd.charAt(upperbound - 1) == key.charAt(0);
            if ((isKeyAtLowerBound || isKeyAtUpperBound) && !(isKeyAtLowerBound && isKeyAtUpperBound))
                validPasswordCount++;
        }
        System.out.println(validPasswordCount);

    }

    public static void manipulateInput(Scanner scanner) {
        inputLine = scanner.nextLine().split(" ");
        String[] first = inputLine[0].toString().trim().split("-");
        lowerbound = Integer.parseInt(first[0]);
        upperbound = Integer.parseInt(first[1]);
        key = String.valueOf(inputLine[1].toCharArray()[0]);
        pwd = inputLine[2];
    }
}

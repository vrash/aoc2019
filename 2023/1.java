import java.io.File;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        //part 1
        Scanner scanner = new Scanner(new File("/Users/.../Desktop/Advent-Of-Code/2022/input.txt"));
        int mostCalories = 0;
        int elfCalSum = 0;
        TreeSet<Integer> treeSet = new TreeSet<Integer>();
        while (scanner.hasNext()) {
            int nextInt = Integer.parseInt("0" + scanner.nextLine());
            elfCalSum = elfCalSum + nextInt;
            treeSet.add(elfCalSum);
            if (nextInt == 0) {
                mostCalories = Math.max(mostCalories, elfCalSum);
                elfCalSum = 0;
            }
        }
        //part 1
        System.out.println(mostCalories);

        //part 2
        TreeSet<Integer> forPart2 = (TreeSet<Integer>) treeSet.descendingSet();
        int part2 = 0;
        int topThree = 1;
        for (int i : forPart2) {
            if (topThree++ <= 3)
                part2 = part2 + i;

        }
        //part 2
        System.out.println(part2);
    }
}

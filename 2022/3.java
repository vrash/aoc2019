import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        part1();
        part2();

    }

    public static void part1() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("/Users/../Desktop/Advent-Of-Code/2022/input.txt"));
        int part1Sum = 0;
        while (scanner.hasNext()) {
            String word = scanner.nextLine();
            String firstHalf = word.substring(0, (word.length() / 2));
            String secondHalf = word.substring(word.length() / 2);
            Set<Character> ss1 = toSet(firstHalf);
            ss1.retainAll(toSet(secondHalf));
            part1Sum += partialSum(new ArrayList<>(ss1));
        }
        System.out.println(part1Sum);
    }

    public static void part2() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("/Users/../Desktop/Advent-Of-Code/2022/input.txt"));
        int part2Sum = 0;
        int wordCount = 0;
        Set<Character> commonSet = new HashSet<>();
        while (scanner.hasNext()) {
            String word = scanner.nextLine();
            if (commonSet.size() == 0) {
                commonSet = toSet(word);
            } else {
                commonSet.retainAll(toSet(word));
            }
            if (wordCount++ == 2) {
                int partialSum = partialSum(new ArrayList<>(commonSet));
                part2Sum += partialSum;
                commonSet.clear();
                wordCount=0;
            }
        }
        System.out.println(part2Sum);
    }


    public static int partialSum(List<Character> list) {
        int partialsum = 0;
        for (char c : list) {
            partialsum += Character.isUpperCase(c) ? (int) c - 38 : (int) c - 96;
        }
        return partialsum;
    }

    public static Set<Character> toSet(String s) {
        Set<Character> ss = new HashSet<Character>(s.length());
        for (char c : s.toCharArray())
            ss.add(Character.valueOf(c));
        return ss;
    }
}

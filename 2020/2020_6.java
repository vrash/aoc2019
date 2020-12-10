import java.io.File;
import java.io.IOException;
import java.util.*;

public class AdventOfCode {
    static HashMap<Character, Integer> entriesMap = new HashMap<Character, Integer>();
    static TreeSet<Character> entries = new TreeSet<Character>();
    static String entry;

    public static void main(String[] args) throws IOException {
        File filePath = new File("/Users/vrashabhirde/Desktop/aoc/input.txt");
        Scanner part1 = new Scanner(filePath);
        Scanner part2 = new Scanner(filePath);
        //part1
        getSumOfAnyoneYes(part1);
        //part2
        getSumOfEveryYes(part2);
    }

    public static void getSumOfEveryYes(Scanner scanner) {
        int sumOfEveryYes = 0;
        int numberOfPeople = 0;
        while (scanner.hasNext()) {
            entry = scanner.nextLine();
            if (entry.equals("")) {
                for (int peopleWhoChecked : entriesMap.values()) {
                    if (peopleWhoChecked == numberOfPeople)
                        sumOfEveryYes = sumOfEveryYes + 1;
                }
                numberOfPeople = 0;
                entriesMap.clear();
            } else {
                numberOfPeople++;
                for (char c : entry.toCharArray()) {
                    entriesMap.put(c, entriesMap.getOrDefault(c,0) + 1);
                }
            }

        }
        for (int peopleWhoChecked : entriesMap.values()) {
            if (peopleWhoChecked == numberOfPeople)
                sumOfEveryYes = sumOfEveryYes + 1;
        }
        System.out.println("Sum of Every Yes: " + sumOfEveryYes);

    }

    public static void getSumOfAnyoneYes(Scanner scanner) {
        int sumOfAnyYes = 0;
        while (scanner.hasNext()) {
            entry = scanner.nextLine();
            if (entry.equals("")) {
                sumOfAnyYes = sumOfAnyYes + entries.size();
                entries = new TreeSet<>();
            } else {
                for (char c : entry.toCharArray()) {
                    entries.add(c);
                }
            }

        }
        sumOfAnyYes = sumOfAnyYes + entries.size();
        System.out.println("Sum of Any Yes: " + sumOfAnyYes);

    }
}

import java.io.File;
import java.io.IOException;
import java.util.*;

public class AdventOfCode {
    static HashMap<String, ArrayList<String>> listOfBagsInOtherBags = new HashMap<>();
    static HashMap<String, ArrayList<Bag>> listOfBagsInThisBag = new HashMap<>();
    static HashSet<String> bagsContainedWithinOtherBags = new HashSet<>();
    static String MY_BAG = "shinygoldbag";

    public static void main(String[] args) throws IOException {
        File filePath = new File("/Users/vrashabhirde/Desktop/aoc/input.txt");
        Scanner part1 = new Scanner(filePath);
        Scanner part2 = new Scanner(filePath);
        //part 1
        getShinyGoldBagNumbers(part1);

        //part 2
        findBags();
        System.out.println(findBagsCount(MY_BAG) - 1);
    }

     static class Bag {
        int number;
        String colour;

        Bag(int number, String colour) {
            this.number = number;
            this.colour = colour;
        }
    }

     static void getShinyGoldBagNumbers(Scanner scanner) {
        String entry;
        while (scanner.hasNext()) {
            ArrayList<String> bagContentList = new ArrayList<>();
            entry = scanner.nextLine();
            String[] entrySplit = entry.split(" ");
            String aNode = entrySplit[0] + entrySplit[1] + entrySplit[2].substring(0, entrySplit[2].length() - 1);
            String bNode = entrySplit[0] + entrySplit[1] + entrySplit[2].substring(0, entrySplit[2].length() - 1);

            if (entrySplit[entrySplit.length - 3].equals("no"))
                continue;

            int parseLength = 4;
            int numberToAppend = 1;

            while (parseLength < entrySplit.length) {
                String bagContent = sanitizeInput(entrySplit[parseLength]) + sanitizeInput(entrySplit[parseLength + 1]) + sanitizeInput(entrySplit[parseLength + 2]) + sanitizeInput(entrySplit[parseLength + 3]);
                //part 1
                if (listOfBagsInOtherBags.get(bagContent) == null)
                    listOfBagsInOtherBags.put(bagContent, new ArrayList<>());
                listOfBagsInOtherBags.get(bagContent).add(aNode);
                //part 2
                if (entrySplit[parseLength].substring(0, 1).matches("[0-9]"))
                    numberToAppend = Integer.parseInt(entrySplit[parseLength].substring(0, 1));
                if (listOfBagsInThisBag.get(bNode) == null)
                    listOfBagsInThisBag.put(bNode, new ArrayList<>());
                listOfBagsInThisBag.get(bNode).add(new Bag(numberToAppend, bagContent));
                parseLength = parseLength + 4;
            }
        }
    }

    // Your most inefficientness, Sir sanitizeInput
     static String sanitizeInput(String s) {
        s = s.trim();
        if (s.endsWith("."))
            s = s.substring(0, s.length() - 1);
        if (s.endsWith(","))
            s = s.substring(0, s.length() - 1);
        if (s.endsWith("s"))
            return s.substring(0, s.length() - 1);
        if (s.substring(0, 1).matches("[0-9]"))
            s = s.substring(1);
        return s;
    }

    //Recursive DFS
     static int findBagsCount(String myBag) {
        int ans = 1;
        if (listOfBagsInThisBag.get(myBag) == null)
            return ans;
        for (Bag bag : listOfBagsInThisBag.get(myBag)) {
            ans = ans + bag.number * findBagsCount(bag.colour);
        }
        return ans;

    }

    //BFS on bags list with my bag as graph starting point
     static void findBags() {
        Deque<String> q = new LinkedList<>();
        q.add(MY_BAG);
        while (!q.isEmpty()) {
            String bag = q.pop();
            if (bagsContainedWithinOtherBags.contains(bag))
                continue;
            bagsContainedWithinOtherBags.add(bag);
            if (listOfBagsInOtherBags.get(bag) == null) {
                continue;
            }
            for (String bags : listOfBagsInOtherBags.get(bag)) {
                q.add(bags);
            }
        }
        System.out.println(bagsContainedWithinOtherBags.size() - 1);
    }
}

import java.io.File;
import java.io.IOException;
import java.util.*;

public class Main {

    static int WINDOW_PART1 = 4;
    static int WINDOW_PART2 = 14;

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(new File("/Users/vrashabh.irde@carwow.co.uk/Desktop/Advent-Of-Code/2022/input.txt"));
        while (scanner.hasNext()) {
            String inputWords = scanner.nextLine();
            //toggle part1/2 depending on need
            int SLIDING_WINDOW = WINDOW_PART1;
            for (int i = 0; i <= inputWords.length() - SLIDING_WINDOW; i++) {
                HashSet<Character> unique = new HashSet<>();
                if (i == 0)
                    unique.add(inputWords.charAt(i));
                else unique.clear();
                for (int j = 0; j < SLIDING_WINDOW; j++) {
                    unique.add(inputWords.charAt(i + j));
                }
                if (unique.size() == SLIDING_WINDOW) {
                    System.out.println(i + SLIDING_WINDOW);
                    break;
                }
            }
        }
    }
}

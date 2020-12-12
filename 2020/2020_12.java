import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class AdventOfCode {
    static int[] X = new int[]{0, 1, 0, -1};
    static int[] Y = new int[]{1, 0, -1, 0};
    static int x = 0;
    static int y = 0;
    static int rotate_x = 10;
    static int rotate_y = 1;
    static int direction = 1;

    public static void main(String[] args) throws IOException {
        File filePath = new File("/Users/vrashabhirde/Desktop/aoc1/input.txt");
        Scanner scanner = new Scanner(filePath);
        //part 1
        printCo_Ordinate_Sum(scanner);
        //part 2
        Scanner scanner1 = new Scanner(filePath);
        printManhattanDistance(scanner1);
    }


    public static void printCo_Ordinate_Sum(Scanner scanner) {
        while (scanner.hasNext()) {
            String input = scanner.nextLine();
            String cmd = input.substring(0, 1);
            int n = Integer.parseInt(input.substring(1));
            int rotation = n / 90;
            if (cmd.equals("N"))
                y = y + n;
            else if (cmd.equals("S"))
                y = y - n;
            else if (cmd.equals("E"))
                x = x + n;
            else if (cmd.equals("W"))
                x = x - n;
            else if (cmd.equals("L")) {

                direction = (direction + 3 * rotation) % 4;
            } else if (cmd.equals("R")) {

                direction = (direction + 1 * rotation) % 4;
            } else if (cmd.equals("F")) {
                x += X[direction] * n;
                y += Y[direction] * n;

            }

        }
        System.out.println(Math.abs(x) + Math.abs(y));

    }

    public static void printManhattanDistance(Scanner scanner) {
        x = 0;
        y = 0;
        while (scanner.hasNext()) {
            String input = scanner.nextLine();
            String cmd = input.substring(0, 1);
            int n = Integer.parseInt(input.substring(1));
            int rotation = n / 90;
            if (cmd.equals("N"))
                rotate_y = rotate_y + n;
            else if (cmd.equals("S"))
                rotate_y = rotate_y - n;
            else if (cmd.equals("E"))
                rotate_x = rotate_x + n;
            else if (cmd.equals("W"))
                rotate_x = rotate_x - n;
            else if (cmd.equals("L")) {
                for (int i = 0; i < rotation; i++) {
                    int temp = rotate_x;
                    rotate_x = -rotate_y;
                    rotate_y = temp;
                }

            } else if (cmd.equals("R")) {
                for (int i = 0; i < rotation; i++) {
                    int temp = rotate_x;
                    rotate_x = rotate_y;
                    rotate_y = -temp;
                }

            } else if (cmd.equals("F")) {
                x += n * rotate_x;
                y += n * rotate_y;

            }

        }
        System.out.println(Math.abs(x) + Math.abs(y));

    }
}

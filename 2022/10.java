import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Main {

    static int cycle = 0;
    static int X = 1;
    static int totalSignalStrength = 0;

    static int CRT_BOUND = 40;

    static int spritePosition = 0;

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("/Users/../Desktop/Advent-Of-Code/2022/input.txt"));
        while (scanner.hasNext()) {
            String[] command = scanner.nextLine().split(" ");
            if (command[0].equals("noop")) {
                cycle++;
                printCRT();
                getTotalSignalStrength(cycle);

            } else if (command[0].equals("addx")) {
                for (int i = 1; i <= 2; i++) {
                    cycle++;
                    printCRT();
                    if (i == 2) {
                        X = X + Integer.parseInt(command[1]);
                        spritePosition = X % 40;
                    }
                    getTotalSignalStrength(cycle);
                }
            }
        }
        System.out.println("");
        System.out.println("Part 1:" + totalSignalStrength);
    }

    public static void printCRT() {
        if ((cycle - 1) % CRT_BOUND == 0) {
            System.out.println("");
        }
        if ((cycle - 1) % CRT_BOUND == spritePosition || (cycle - 1) % CRT_BOUND == (spritePosition - 1) || (cycle - 1) % CRT_BOUND == spritePosition + 1)
            System.out.print("# ");
        else System.out.print(". ");
    }

    public static void getTotalSignalStrength(int cycle) {
        if (cycle == 19 || cycle == 59 || cycle == 99 || cycle == 139 || cycle == 179 || cycle == 219) {
            {
                totalSignalStrength = totalSignalStrength + ((cycle + 1) * X);
            }

        }
    }

}

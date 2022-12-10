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
        int prevCycle = cycle - 1;
        if ((prevCycle) % CRT_BOUND == 0) {
            System.out.println("");
        }
        if ((prevCycle) % CRT_BOUND == spritePosition || (prevCycle) % CRT_BOUND == (spritePosition - 1) || (prevCycle) % CRT_BOUND == spritePosition + 1)
            System.out.print("# ");
        else System.out.print(". ");
    }

    public static void getTotalSignalStrength(int cycle) {
        int during = cycle + 1;
        if (during == 20 || during == 60 || during == 100 || during == 140 || during == 180 || during == 220) {
            {
                totalSignalStrength = totalSignalStrength + ((during) * X);
            }

        }
    }

}

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.Objects;

import static java.lang.Math.abs;

public class Main {

    public static int hx = 0;
    public static int hy = 0;
    public static int tx = 0;
    public static int ty = 0;

    public static class location {
        int x;
        int y;

        location(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {

            if (o == this) return true;
            if (!(o instanceof location)) {
                return false;
            }

            location l = (location) o;

            return l.x == x && l.y == y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    static HashSet<location> setter = new HashSet<>();

    public static void main(String[] args) throws FileNotFoundException {

        Scanner scanner = new Scanner(new File("/Users/../Desktop/Advent-Of-Code/2022/input.txt"));
        while (scanner.hasNext()) {
            String[] command = scanner.nextLine().split(" ");
            simulateRope(command[0].charAt(0), Integer.parseInt(command[1]));
        }

        System.out.println(setter.size());

    }

    public static void simulateRope(char direction, int number) {

        for (int i = 1; i <= number; i++) {
            if (direction == 'D') {
                hy += 1;
            } else if (direction == 'L') {
                hx -= 1;
            } else if (direction == 'R') {
                hx += 1;
            } else if (direction == 'U') {
                hy -= 1;
            }

            if (abs(tx - hx) <= 1 && abs(ty - hy) <= 1) {
                //do nothing
            } else if (tx == hx) {
                if (ty < hy) ty += 1;
                else ty -= 1;
            } else if (ty == hy) {
                if (tx < hx) tx += 1;
                else tx -= 1;
            } else {
                if (tx < hx) tx += 1;
                else tx -= 1;
                if (ty < hy) ty += 1;
                else ty -= 1;
            }
            setter.add(new location(tx, ty));
        }

    }

}

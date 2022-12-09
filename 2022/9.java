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
    static location[] rope = new location[10];

    public static void main(String[] args) throws FileNotFoundException {

        //part 1
        Scanner scanner = new Scanner(new File("/Users/../Desktop/Advent-Of-Code/2022/input.txt"));
        while (scanner.hasNext()) {
            String[] command = scanner.nextLine().split(" ");
            int number = Integer.parseInt(command[1]);
            for (int i = 1; i <= number; i++) {
                simulateRope(command[0].charAt(0));
            }
        }

        System.out.println(setter.size());
        setter.clear();

        for (int i = 0; i < 10; i++) {
            rope[i] = new location(0, 0);
        }
        //part 2
        Scanner scanner1 = new Scanner(new File("/Users/../Desktop/Advent-Of-Code/2022/input.txt"));
        while (scanner1.hasNext()) {
            String[] command = scanner1.nextLine().split(" ");
            int number = Integer.parseInt(command[1]);
            for (int i = 1; i <= number; i++) {
                simulateBiggerRope(0, 1, command[0].charAt(0));
                for (int j = 1; j < rope.length - 1; j++)
                    simulateBiggerRope(j, j + 1, 'X');
            }
        }

        System.out.println(setter.size());
    }

    public static void simulateBiggerRope(int headi, int taili, char direction) {

        hx = rope[headi].x;
        hy = rope[headi].y;
        tx = rope[taili].x;
        ty = rope[taili].y;
        move(direction);
        rope[headi] = new location(hx, hy);
        rope[taili] = new location(tx, ty);
        setter.add(new location(rope[rope.length - 1].x, rope[rope.length - 1].y));
    }

    public static void move(char direction) {
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
    }

    public static void simulateRope(char direction) {
        move(direction);
        setter.add(new location(tx, ty));
    }


}

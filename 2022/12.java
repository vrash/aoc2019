import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Main {
    static int ROWS = 0;
    static int COLS = 0;
    static int endx = 0;
    static int endy = 0;

    public static void main(String[] args) throws FileNotFoundException {
        int[][] input = build2DArrayinput();
        System.out.println("Part 1: " + (calculatePath(input, new int[ROWS][COLS], endx, endy, 27) - 2));
        System.out.println("Part 2: " + (calculatePath(input, new int[ROWS][COLS], endx, endy, 26) - 2));
    }

    public static int calculatePath(final int[][] map, final int[][] minKnownPath, final int x, final int y, int goal) {
        int pathToThisSquare = minKnownPath[x][y] + 1;

        int lowestSteps = Integer.MAX_VALUE;
        for (int direction = 1; direction <= 7; direction += 2) {
            int nx = x + ((direction % 3) - 1);
            int ny = y + ((direction / 3) - 1);

            if (nx >= 0 && nx < map.length && ny >= 0 && ny < map[0].length) {
                boolean canMakeStep = map[nx][ny] <= map[x][y] + 1;
                boolean isShorterPath = (minKnownPath[nx][ny] == 0 || pathToThisSquare < minKnownPath[nx][ny]);
                if (canMakeStep && isShorterPath) {
                    minKnownPath[nx][ny] = pathToThisSquare;
                    if (map[nx][ny] == goal) {
                        return pathToThisSquare;
                    }
                    lowestSteps = Math.min(lowestSteps, calculatePath(map, minKnownPath, nx, ny, goal));
                }
            }
        }
        return lowestSteps;
    }

    public static int[][] build2DArrayinput() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("/Users/../Desktop/Advent-Of-Code/2022/input.txt"));
        Scanner scanner1 = new Scanner(new File("/Users/../Desktop/Advent-Of-Code/2022/input.txt"));
        int r = 0;
        int c = 0;
        while (scanner.hasNext()) {
            String s = scanner.nextLine();
            if (r == 0) {
                c = s.length();
            }
            r++;
        }
        ROWS = r;
        COLS = c;
        int[][] input = new int[ROWS][COLS];
        while (scanner1.hasNext()) {
            for (int i = 0; i < r; i++) {
                String s = scanner1.nextLine();

                for (int j = 0; j < c; j++) {
                    char matcher = s.split("")[j].charAt(0);
                    if (matcher == 'S') {
                        input[i][j] = 27;
                    } else if (matcher == 'E') {
                        endx = i;
                        endy = j;
                        input[i][j] = 0;
                    } else
                        input[i][j] = (int) 'z' + 1 - matcher;
                }

            }
        }
        return input;
    }
}

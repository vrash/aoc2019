import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.*;
import java.util.stream.Stream;

public class Main {
    static int ROWS = 0;
    static int COL = 0;
    static int part2 = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        int[][] input = build2DArrayinput();
        int part1 = 0;
        char[][] visibility = new char[ROWS][COL];
        for (int i = 0; i < ROWS; i++)
            for (int j = 0; j < COL; j++)
                visibility[i][j] = 'y';

        for (int i = 0; i < ROWS - 1; i++) {
            for (int j = 0; j < COL - 1; j++) {
                setVisibility(input, i, j, visibility);
            }
        }
        for (int i = 0; i < ROWS; i++)
            for (int j = 0; j < COL; j++)
                if (visibility[i][j] == 'y') part1++;

        System.out.println(part1);
        System.out.println(part2);

    }

    public static void setVisibility(int[][] input, int row, int col, char[][] visibility) {
        boolean lflag = true;
        boolean rflag = true;
        boolean tflag = true;
        boolean bflag = true;
        int tDist = 1;
        int lDist = 1;
        int rDist = 1;
        int bDist = 1;


        for (int i = row - 1; i >= 0; i--) {
            if (input[row][col] <= input[i][col]) {
                tflag = false;
                break;
            } else
                tDist++;
        }
        if (tflag)
            tDist--;
        for (int i = col + 1; i <= COL - 1; i++) {
            if (input[row][col] <= input[row][i]) {
                rflag = false;
                break;
            } else
                rDist++;
        }
        if (rflag)
            rDist--;
        for (int i = col - 1; i >= 0; i--) {
            if (input[row][col] <= input[row][i]) {
                lflag = false;
                break;
            } else
                lDist++;
        }
        if (lflag)
            lDist--;
        for (int i = row + 1; i <= ROWS - 1; i++) {
            if (input[row][col] <= input[i][col]) {
                bflag = false;
                break;
            } else
                bDist++;
        }
        if (bflag)
            bDist--;

        if (Stream.of(lflag, rflag, tflag, bflag).anyMatch(x -> x))
            visibility[row][col] = 'y';
        else visibility[row][col] = 'n';

        part2 = Math.max(part2, (tDist * rDist * lDist * bDist));
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
        COL = c;
        int[][] input = new int[r][c];
        while (scanner1.hasNext()) {
            for (int i = 0; i < r; i++) {
                String s = scanner1.nextLine();
                for (int j = 0; j < c; j++)
                    input[i][j] = Integer.parseInt(s.split("")[j]);
            }
        }
        return input;
    }
}

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.stream.Stream;

public class Main {
    static int ROWS = 0;
    static int COLS = 0;
    static int part2 = Integer.MIN_VALUE;

    public static void main(String[] args) throws FileNotFoundException {
        int[][] input = build2DArrayinput();


    }

    public enum DIRECTION {
        LEFT, RIGHT, TOP, BOTTOM
    }

    public static void setVisibility(int[][] input, int row, int col, boolean[][] visibility) {
        boolean[] flags = {true, true, true, true};
        int[] distArray = {1, 1, 1, 1};

        for (int i = row - 1; i >= 0; i--) {
            if (input[row][col] <= input[i][col]) {
                flags[DIRECTION.TOP.ordinal()] = false;
                break;
            } else distArray[DIRECTION.TOP.ordinal()]++;
        }
        if (flags[DIRECTION.TOP.ordinal()]) distArray[DIRECTION.TOP.ordinal()]--;


        for (int i = col + 1; i <= COLS - 1; i++) {
            if (input[row][col] <= input[row][i]) {
                flags[DIRECTION.RIGHT.ordinal()] = false;
                break;
            } else distArray[DIRECTION.RIGHT.ordinal()]++;
        }
        if (flags[DIRECTION.RIGHT.ordinal()]) distArray[DIRECTION.RIGHT.ordinal()]--;


        for (int i = col - 1; i >= 0; i--) {
            if (input[row][col] <= input[row][i]) {
                flags[DIRECTION.LEFT.ordinal()] = false;
                break;
            } else distArray[DIRECTION.LEFT.ordinal()]++;
        }
        if (flags[DIRECTION.LEFT.ordinal()]) distArray[DIRECTION.LEFT.ordinal()]--;


        for (int i = row + 1; i <= ROWS - 1; i++) {
            if (input[row][col] <= input[i][col]) {
                flags[DIRECTION.BOTTOM.ordinal()] = false;
                break;
            } else distArray[DIRECTION.BOTTOM.ordinal()]++;
        }
        if (flags[DIRECTION.BOTTOM.ordinal()]) distArray[DIRECTION.BOTTOM.ordinal()]--;

        //part 1
        visibility[row][col] = Stream.of(flags[DIRECTION.LEFT.ordinal()], flags[DIRECTION.RIGHT.ordinal()], flags[DIRECTION.TOP.ordinal()], flags[DIRECTION.BOTTOM.ordinal()]).anyMatch(x -> x);

        //part 2
        part2 = Math.max(part2, (distArray[DIRECTION.BOTTOM.ordinal()] * distArray[DIRECTION.LEFT.ordinal()] * distArray[DIRECTION.RIGHT.ordinal()] * distArray[DIRECTION.TOP.ordinal()]));
    }


}

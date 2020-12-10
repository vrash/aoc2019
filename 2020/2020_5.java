import java.io.File;
import java.io.IOException;
import java.util.*;

public class AdventOfCode {
    static File filePath = new File("/Users/vrashabhirde/Desktop/aoc/input.txt");
    static String seat;
    static TreeSet<Integer> setOfSeats = new TreeSet<Integer>(Collections.reverseOrder());

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(filePath);
        //part1
        processSeatNumbersAndFindHighestSeatID(in);
        //part2
        findMySeat();
    }

    public static void processSeatNumbersAndFindHighestSeatID(Scanner scanner) {
        int i = 0;
        while (scanner.hasNext()) {
            seat = scanner.nextLine();

            //USING RECURSION - MORE READABLE
            int row = findSeatRow(seat, 0, 0, 127);
            int col = findSeatCol(seat.substring(7), 0, 0, 7);
            int seatNumber = row * 8 + col;
            setOfSeats.add(seatNumber);

            //USING BIT TWIDDLING - LESS READABLE
            findSeatRowAndColUsingBitTwiddle(seat);

        }
        System.out.println("Highest Seat Number:" + setOfSeats.first());

    }
    public static void findMySeat()
    {
        Iterator<Integer> itr = setOfSeats.iterator();
        int nextSeat = 0;
        while(itr.hasNext())
        {
            int currentSeat = itr.next();
            if(currentSeat == nextSeat - 2)
                System.out.println("My Seat : " + currentSeat+1);
            else
                nextSeat = currentSeat;
        }

    }

    public static void findSeatRowAndColUsingBitTwiddle(String s)
    {
        int row = 0;
        int rowBin = 64;
        int col = 0;
        int colBin = 4;
        for(char c: s.toCharArray())
        {
            if(c=='B')
            {
                row += rowBin;
                rowBin= rowBin/2;
            }
            else if(c=='F')
                rowBin= rowBin/2;
            if(c=='R')
            {
                col += colBin;
                colBin = colBin/2;
            }
            else if(c=='L')
                colBin = colBin/2;

        }
       // System.out.println("Row: " + row + " Col: " + col);
    }

    public static int findSeatRow(String s, int i, int low, int high) {
        if (i == 7) {
            return s.charAt(i) == 'F' ? low : high;
        } else if (s.charAt(i) == 'F')
            return findSeatRow(s, ++i, low, (low + high) / 2);
        else
            return findSeatRow(s, ++i, (low + high) / 2 + 1, high);
    }


    public static int findSeatCol(String s, int i, int low, int high) {
        if (i == 2) {
            return s.charAt(i) == 'L' ? low : high;
        } else if (s.charAt(i) == 'L')
            return findSeatCol(s, ++i, low, (low + high) / 2);
        else
            return findSeatCol(s, ++i, (low + high) / 2 + 1, high);
    }
}

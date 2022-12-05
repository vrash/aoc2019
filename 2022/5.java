import java.io.File;
import java.io.IOException;
import java.util.*;

public class Main {
    static int LINEFEED = 10;

    public static void main(String[] args) throws IOException {
        int lf = 1;

        Stack[] part1 = buildInput();
        Stack[] part2 = buildInput();
        Scanner scanner = new Scanner(new File("/Users/../Desktop/Advent-Of-Code/2022/input.txt"));
        while (scanner.hasNext()) {
            if (lf++ <= LINEFEED) {
                scanner.nextLine();
                continue;
            } else {
                //part1
                String[] inputCommand = scanner.nextLine().split(" ");
                int numberOfBoxes = Integer.parseInt(inputCommand[1]);
                int from = Integer.parseInt(inputCommand[3]);
                int to = Integer.parseInt(inputCommand[5]);
                while (numberOfBoxes-- > 0) {
                    part1[to - 1].push(part1[from - 1].pop());
                }

                //part2
                numberOfBoxes = Integer.parseInt(inputCommand[1]);
                ArrayList<Character> topOfStack = new ArrayList<>();
                while (numberOfBoxes-- > 0) {

                    topOfStack.add((char) part2[from - 1].pop());
                }
                Collections.reverse(topOfStack);
                for (char c : topOfStack) {
                    part2[to - 1].push(c);
                }

            }
        }
        for (int x = 0; x < part1.length; x++)
            System.out.print(part1[x].peek());
        System.out.println("");
        for (int x = 0; x < part2.length; x++)
            System.out.print(part2[x].peek());

    }

    public static Stack[] buildInput() {
        Stack<Character> stack1 = new Stack<>();
        stack1.push('F');
        stack1.push('C');
        stack1.push('J');
        stack1.push('P');
        stack1.push('H');
        stack1.push('T');
        stack1.push('W');

        Stack<Character> stack2 = new Stack<>();
        stack2.push('G');
        stack2.push('R');
        stack2.push('V');
        stack2.push('F');
        stack2.push('Z');
        stack2.push('J');
        stack2.push('B');
        stack2.push('H');

        Stack<Character> stack3 = new Stack<>();
        stack3.push('H');
        stack3.push('P');
        stack3.push('T');
        stack3.push('R');

        Stack<Character> stack4 = new Stack<>();
        stack4.push('Z');
        stack4.push('S');
        stack4.push('N');
        stack4.push('P');
        stack4.push('H');
        stack4.push('T');


        Stack<Character> stack5 = new Stack<>();
        stack5.push('N');
        stack5.push('V');
        stack5.push('F');
        stack5.push('Z');
        stack5.push('H');
        stack5.push('J');
        stack5.push('C');
        stack5.push('D');

        Stack<Character> stack6 = new Stack<>();
        stack6.push('P');
        stack6.push('M');
        stack6.push('G');
        stack6.push('F');
        stack6.push('W');
        stack6.push('D');
        stack6.push('Z');

        Stack<Character> stack7 = new Stack<>();
        stack7.push('M');
        stack7.push('V');
        stack7.push('Z');
        stack7.push('W');
        stack7.push('S');
        stack7.push('J');
        stack7.push('D');
        stack7.push('P');

        Stack<Character> stack8 = new Stack<>();
        stack8.push('N');
        stack8.push('D');
        stack8.push('S');

        Stack<Character> stack9 = new Stack<>();
        stack9.push('D');
        stack9.push('Z');
        stack9.push('S');
        stack9.push('F');
        stack9.push('M');

        Stack[] arr = new Stack[]{stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9};
        return arr;
    }
}

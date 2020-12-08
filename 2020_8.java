import java.io.File;
import java.io.IOException;
import java.util.*;

public class AdventOfCode {
    static List<OpCode> listOfCodes = new LinkedList<>();
    static List<OpCode> listOfCodes2 = new LinkedList<>();
    static int accumulator = 0;
    static HashSet<OpCode> map = new HashSet<>();

    public static void main(String[] args) throws IOException {
        File filePath = new File("/Users/vrashabhirde/Desktop/aoc/input.txt");
        Scanner part1 = new Scanner(filePath);
        Scanner part2 = new Scanner(filePath);
        //part 1
        inputInstructions(part1);
        walkThroughOpCodes();
        //part 2
        accumulator = 0;
        changeOneInstruction();

    }

    static class OpCode {
        String instruction;
        char sign;
        int num;

        OpCode(String instruction, char sign, int num) {
            this.instruction = instruction;
            this.sign = sign;
            this.num = num;
        }
    }

    static void inputInstructions(Scanner scanner) {
        String entry;
        while (scanner.hasNext()) {
            entry = scanner.nextLine();
            String[] opcodes = entry.split(" ");
            OpCode op = new OpCode(opcodes[0], opcodes[1].charAt(0), Integer.parseInt(String.valueOf(opcodes[1].substring(1))));
            listOfCodes.add(op);
        }
    }

    static void changeOneInstruction() {
        //n2 brute force, flip every line and loop. Run a rate limiter to prevent infinite loop
        for (int i = 0; i < listOfCodes.size(); i++) {
            ArrayList<OpCode> listOfCodes2 = new ArrayList<OpCode>(listOfCodes);
            if (listOfCodes2.get(i).instruction.equals("nop")) {
                OpCode x = new OpCode("jmp", listOfCodes2.get(i).sign, listOfCodes2.get(i).num);
                listOfCodes2.set(i, x);
            } else if (listOfCodes2.get(i).instruction.equals("jmp")) {
                OpCode x = new OpCode("nop", listOfCodes2.get(i).sign, listOfCodes2.get(i).num);
                listOfCodes2.set(i, x);
            } else
                continue;

            int j = 0;
            int rateLimiter = 0;
            accumulator = 0;
            while (j >= 0 && j < listOfCodes2.size() && rateLimiter<500) {
                rateLimiter = rateLimiter + 1;
                OpCode nextInst = listOfCodes2.get(j);
                j = operations(nextInst, j);

            }
            //rate limit to a 500 instruction run and check if length matches i.e. reached end
            // of instruction set
            if (j == listOfCodes2.size())
                System.out.println(accumulator);

        }
    }

    static int operations(OpCode nextInst, int i) {
        if (nextInst.instruction.equals("nop"))
            i = i + 1;
        else if (nextInst.instruction.equals("jmp")) {
            i = nextInst.sign == '+' ? i + nextInst.num : i - nextInst.num;
        } else {
            i = i + 1;
            accumulator = nextInst.sign == '+' ? accumulator + nextInst.num : accumulator - nextInst.num;
        }
        return i;

    }

    static void walkThroughOpCodes() {
        int i = 0;
        while (true) {
            OpCode nextInst = listOfCodes.get(i);
            if (map.contains(nextInst))
                break;
            map.add(nextInst);
            i = operations(nextInst, i);

        }
        System.out.println(accumulator);
    }
}

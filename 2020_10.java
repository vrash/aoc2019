import java.io.File;
import java.io.IOException;
import java.util.*;

public class AdventOfCode {
    static ArrayList<Integer> inputList = new ArrayList<>();
    static int[] inputArray;

    public static void main(String[] args) throws IOException {
        File filePath = new File("/Users/vrashabhirde/Desktop/aoc/input.txt");
        Scanner input = new Scanner(filePath);
        readIntegersFromFile(input);
        //part 1
        int part1 = joltageDiffMux();
        System.out.println(part1);
        //part 2
        long part2 = setNumberOfWaysOfArrangingAdapter();
        System.out.println(part2);
    }

    public static void readIntegersFromFile(Scanner scanner) {
        while (scanner.hasNext()) {
            inputList.add(Integer.parseInt(scanner.nextLine()));
        }
        //outlet
        inputList.add(0);
        //device built in
        inputList.add(Collections.max(inputList) + 3);

        inputArray = inputList.stream().mapToInt(i -> i).toArray();
        Arrays.sort(inputArray);

    }

    public static int joltageDiffMux() {
        int oneDiffJolt = 0;
        int threeDiffJolt = 0;
        for (int i = 0; i < inputArray.length - 1; i++) {
            int diff = inputArray[i + 1] - inputArray[i];
            if (diff == 1)
                oneDiffJolt++;
            else if (diff == 3)
                threeDiffJolt++;
        }
        return oneDiffJolt * threeDiffJolt;
    }

    public static long setNumberOfWaysOfArrangingAdapter() {
        long[] numberOfWaysOfArrangingAdapter = new long[inputArray.length];
        numberOfWaysOfArrangingAdapter[0] = 1;
        for (int i = 0; i < numberOfWaysOfArrangingAdapter.length - 1; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i + j >= numberOfWaysOfArrangingAdapter.length)
                    continue;
                if (inputArray[i + j] <= inputArray[i] + 3)
                    numberOfWaysOfArrangingAdapter[i + j] += numberOfWaysOfArrangingAdapter[i];
            }
        }
        return numberOfWaysOfArrangingAdapter[numberOfWaysOfArrangingAdapter.length - 1];

    }

}

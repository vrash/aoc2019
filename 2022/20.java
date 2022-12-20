import java.io.File;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        // Read the numbers from the file
        Scanner sc = new Scanner(new File("/Users/../Desktop/Advent-Of-Code/2022/input.txt"));
        List<String> nrs = new ArrayList<>();
        while (sc.hasNext()) {
            nrs.add(sc.nextLine());
        }
        int rounds = 1; // number of rounds
        long multiplier = 1; //add the multiplier


        List<Number> numbers = IntStream.range(0, nrs.size())
                .mapToObj(i -> new Number(Long.parseLong(nrs.get(i)) * multiplier, i))
                .collect(Collectors.toList());
              
        List<Number> processOrder = new ArrayList<>(numbers);

        for (int times = 0; times < rounds; times++) {
            for (Number toMove : processOrder) {
                //Dont need to use pos anywhere directly since the equals takes care of duplicates
                int currentIndex = numbers.indexOf(toMove);
                numbers.remove(currentIndex);
                numbers.add(Math.floorMod(toMove.value + currentIndex, numbers.size()), toMove);
            }
        }

        int fromIndex = numbers.indexOf(numbers.stream().filter(n -> n.value == 0).findFirst().get());
        long v1 = numbers.get((fromIndex + 1000) % numbers.size()).value;
        long v2 = numbers.get((fromIndex + 2000) % numbers.size()).value;
        long v3 = numbers.get((fromIndex + 3000) % numbers.size()).value;

        System.out.println(v1+v2+v3);
    }

    record Number(long value, int pos) {
        //created to tackle duplicates
        // If the list was all unique you could use long instead, but since there are duplicates
        // maintaining original index is used for equals comparison when searching for item from
        // processorder in numbers, and while picking up first occurence of 0
    }
}

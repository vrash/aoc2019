import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.*;

public class AdventOfCode  {
    public static void main(String[] args) throws IOException {
        //part 1
        Scanner scanner = new Scanner(new File("/Users/vrashabhirde/Desktop/aoc/input.txt"));
        HashSet<Integer> setter = new HashSet<>();
        List<Integer> inp = new ArrayList<>();
        while (scanner.hasNext())
        {
            int nextInt = Integer.parseInt(scanner.nextLine());
            if(setter.contains(Math.abs(nextInt-2020))) {
                System.out.println(nextInt * Math.abs(nextInt - 2020));
                break;
            }
            else
                setter.add(nextInt);
        }
        //part 2
        Scanner scanner2 = new Scanner(new File("/Users/vrashabhirde/Desktop/aoc/input.txt"));
        while (scanner2.hasNext())
        {
            inp.add(Integer.parseInt(scanner2.nextLine()));
        }

        int[] A = inp.stream().mapToInt(i -> i).toArray();
        Arrays.sort(A);
        for (int i = 0; i < inp.size() - 2; i++) {
            HashSet<Integer> s = new HashSet<Integer>();
            int curr_sum = 2020 - A[i];
            for (int j = i + 1; j < inp.size(); j++)
            {
                if (s.contains(curr_sum - A[j]))
                {
                    System.out.print(A[i] *
                            A[j] *  (curr_sum - A[j]));
                }
                s.add(A[j]);
            }
        }

    }
}

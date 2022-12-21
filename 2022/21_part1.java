import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    private Map<String, String> monkeyJobs = new HashMap<>();
    private Map<String, BigDecimal> monkeyNumbers = new HashMap<>();

    private BigDecimal calculateNumber(String monkeyName) {
        if (monkeyNumbers.containsKey(monkeyName)) {
            return monkeyNumbers.get(monkeyName);
        }
        String job = monkeyJobs.get(monkeyName);
        if (job.matches("^-?\\d+(\\.\\d+)?$")) {
            BigDecimal number = new BigDecimal(job);
            monkeyNumbers.put(monkeyName, number);
            return number;
        }
        Pattern pattern = Pattern.compile("(\\S+)\\s+(\\S+)\\s+(\\S+)");
        Matcher matcher = pattern.matcher(job);
        if (!matcher.matches()) {
            throw new IllegalArgumentException("Invalid job format: " + job);
        }
        String operand1 = matcher.group(1);
        String operator = matcher.group(2);
        String operand2 = matcher.group(3);

        BigDecimal number1 = calculateNumber(operand1);
        BigDecimal number2 = calculateNumber(operand2);
        BigDecimal result;
        switch (operator) {
            case "+":
                result = number1.add(number2);
                break;
            case "-":
                result = number1.subtract(number2);
                break;
            case "*":
                result = number1.multiply(number2);
                break;
            case "/":
                result = number1.divide(number2, RoundingMode.HALF_UP);
                break;
            default:
                throw new IllegalArgumentException("Invalid operator: " + operator);
        }
        monkeyNumbers.put(monkeyName, result);
        return result;
    }

    public static void main(String[] args) {
        Main riddle = new Main();
        File inputFile = new File("/Users/../Desktop/Advent-Of-Code/2022/input.txt");
        try (Scanner scanner = new Scanner(inputFile)) {
            // Read each line of the file
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();

                // Split the line into the monkey's name and its job
                String[] parts = line.split(": ");
                String monkeyName = parts[0];
                String job = parts[1];

                // Add the monkey and its job to the map
                riddle.monkeyJobs.put(monkeyName, job);
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        System.out.println(riddle.calculateNumber("root"));

    }
}

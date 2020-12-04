import java.io.File;
import java.io.IOException;
import java.util.*;

public class AdventOfCode {
    static HashMap<String, String> passport = new HashMap<String, String>();
    static File filePath = new File("/Users/vrashabhirde/Desktop/aoc/input.txt");
    static int validPassportCount = 0;

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(filePath);
        createInputMatrixFromFile(in);
        System.out.println(validPassportCount);
    }

    static public void createInputMatrixFromFile(Scanner in) throws IOException {
        while (in.hasNextLine()) {
            String[] pTemp = in.nextLine().split(" ");
            if (pTemp[0].equals("")) {
                if (passport.size() == 8 || (passport.size() == 7 && !passport.containsKey("cid"))) {
                    if (byr(passport.get("byr")) && iyr(passport.get("iyr"))
                            && eyr(passport.get("eyr")) && hgt(passport.get("hgt"))
                            && hcl(passport.get("hcl"))
                            && ecl(passport.get("ecl"))
                            && pid(passport.get("pid"))
                    )
                        validPassportCount++;

                }
                passport = new HashMap<String, String>();
            } else {
                for (int i = 0; i < pTemp.length; i++) {
                    String key = pTemp[i].split(":")[0];
                    String value = pTemp[i].split(":")[1];
                    passport.put(key, value);
                }
            }
        }
    }

    public static boolean byr(String nu) {
        int n = Integer.parseInt(nu);
        return (int) (Math.log10(n) + 1) == 4 && n <= 2002 && n >= 1920;
    }

    public static boolean iyr(String nu) {
        int n = Integer.parseInt(nu);
        return (int) (Math.log10(n) + 1) == 4 && n >= 2010 && n <= 2020;
    }

    public static boolean eyr(String nu) {
        int n = Integer.parseInt(nu);
        return (int) (Math.log10(n) + 1) == 4 && n >= 2020 && n <= 2030;
    }

    public static boolean hgt(String nu) {
        int n = Integer.parseInt(nu.substring(0, nu.length() - 2));
        if (nu.contains("cm")) {
            return n >= 150 && n <= 193;
        } else {
            return n >= 59 && n <= 76;
        }
    }

    public static boolean hcl(String nu) {
        return nu.matches("#[0-9a-f]{6}");
    }

    public static boolean ecl(String nu) {
        return nu.equals("amb") || nu.equals("blu") || nu.equals("brn") || nu.equals("gry") || nu.equals("grn") || nu.equals("hzl") || nu.equals("oth");
    }

    public static boolean pid(String nu) {
        return nu.matches("\\d{9}");
    }

}

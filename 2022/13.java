import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("/Users/../Desktop/Advent-Of-Code/2022/input.txt"));
        part1(scanner);
        part2();
    }

    public static List<Packet> packets = new ArrayList<>();

    public static void part1(Scanner in) {
        int part1 = 0;
        int index = 1;
        while (in.hasNext()) {
            Packet packet1 = new Packet(in.nextLine());
            Packet packet2 = new Packet(in.nextLine());
            packets.add(packet1);
            packets.add(packet2);
            if (in.hasNext()) in.nextLine();
            part1 += (packet1.compareTo(packet2) > 0) ? index : 0;
            index++;

        }
        System.out.println("" + part1);
    }

    public static void part2() {
        int part2 = 1;
        packets.add(new Packet("[[2]]"));
        packets.add(new Packet("[[6]]"));
        Collections.sort(packets, Collections.reverseOrder());
        for (int i = 0; i < packets.size(); i++) {
            if (packets.get(i).str.equals("[[2]]") || packets.get(i).str.equals("[[6]]")) {
                part2 *= (i + 1);
            }
        }
        System.out.println("" + part2);
    }


    static class Packet implements Comparable<Packet> {
        List<Packet> tokens;
        int value;
        boolean isInteger = true;
        String str;

        public Packet(String packet) {
            str = packet;
            tokens = new ArrayList<>();
            if (packet.equals("[]")) {
                value = -1;
            }
            if (!packet.startsWith("[")) {
                value = Integer.parseInt(packet);
            } else {
                packet = packet.substring(1, packet.length() - 1);
                int level = 0;
                String tmp = "";
                for (char c : packet.toCharArray()) {
                    if (c == ',' && level == 0) {
                        tokens.add(new Packet(tmp));
                        tmp = "";
                    } else {
                        level += (c == '[') ? 1 : (c == ']') ? -1 : 0;
                        tmp += c;
                    }
                }
                if (!tmp.equals("")) {
                    tokens.add(new Packet(tmp));
                }
                isInteger = false;
            }
        }

        public int compareTo(Packet other) {
            if (isInteger && other.isInteger) {
                return other.value - value;
            }
            if (!isInteger && !other.isInteger) {
                for (int i = 0; i < Math.min(tokens.size(), other.tokens.size()); i++) {
                    int val = tokens.get(i).compareTo(other.tokens.get(i));
                    if (val != 0) {
                        return val;
                    }
                }
                return other.tokens.size() - tokens.size();
            }
            Packet p1 = isInteger ? new Packet("[" + value + "]") : this;
            Packet p2 = other.isInteger ? new Packet("[" + other.value + "]") : other;
            return p1.compareTo(p2);
        }
    }

}

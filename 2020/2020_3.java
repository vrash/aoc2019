import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Stream;

public class AdventOfCode {
    static char[][] cMatrix;
    static File filePath = new File("/Users/vrashabhirde/Desktop/aoc/input.txt");
    static int _3_1_trees = 0;
    static int _1_1_trees = 0;
    static int _5_1_trees = 0;
    static int _7_1_trees = 0;
    static int _1_2_trees = 0;
    static int numberOfRowsInForest;
    static int numberOfColsInForest;

    public static void main(String[] args) throws IOException {
        //part 1
        Scanner fileScan = new Scanner(filePath);
        createInputMatrixFromFile(fileScan);
        right3Down1();
        System.out.println(_3_1_trees);
        //part 2
        right1Down1();
        right5Down1();
        right7Down1();
        right1Down2();
        System.out.println(_3_1_trees * _1_1_trees  * _5_1_trees * _7_1_trees * _1_2_trees);
    }

    static public void right3Down1()
    {
        int treeRow=0;
        int treeCol=0;
        while(treeRow <= numberOfRowsInForest)
        {
            treeCol=treeCol+3; // 3 right
            if(treeCol>=numberOfColsInForest) {
                treeCol = treeCol % numberOfColsInForest; //wrap around
            }
            treeRow++;  // 1 down
            if(treeRow==numberOfRowsInForest) //break
                break;
            if(cMatrix[treeRow][treeCol]=='#') {
                _3_1_trees++;
            }
        }
    }
    static public void right1Down1()
    {
        int treeRow=0;
        int treeCol=0;
        while(treeRow <= numberOfRowsInForest)
        {
            treeCol=treeCol+1; // 1 right
            if(treeCol>=numberOfColsInForest) {
                treeCol = treeCol % numberOfColsInForest; //wrap around
            }
            treeRow++;  // 1 down
            if(treeRow==numberOfRowsInForest) //break
                break;
            if(cMatrix[treeRow][treeCol]=='#') {
                _1_1_trees++;
            }
        }
    }
    static public void right5Down1()
    {
        int treeRow=0;
        int treeCol=0;
        while(treeRow <= numberOfRowsInForest)
        {
            treeCol=treeCol+5; // 5 right
            if(treeCol>=numberOfColsInForest) {
                treeCol = treeCol % numberOfColsInForest; //wrap around
            }
            treeRow++;  // 1 down
            if(treeRow==numberOfRowsInForest) //break
                break;
            if(cMatrix[treeRow][treeCol]=='#') {
                _5_1_trees++;
            }
        }

    }
    static public void right7Down1()
    {
        int treeRow=0;
        int treeCol=0;
        while(treeRow <= numberOfRowsInForest)
        {
            treeCol=treeCol+7; // 7 right
            if(treeCol>=numberOfColsInForest) {
                treeCol = treeCol % numberOfColsInForest; //wrap around
            }
            treeRow++;  // 1 down
            if(treeRow==numberOfRowsInForest) //break
                break;
            if(cMatrix[treeRow][treeCol]=='#') {
                _7_1_trees++;
            }
        }

    }
    static public void right1Down2()
    {
        int treeRow=0;
        int treeCol=0;
        while(treeRow <= numberOfRowsInForest)
        {
            treeCol=treeCol+1; // 1 right
            if(treeCol>=numberOfColsInForest) {
                treeCol = treeCol % numberOfColsInForest; //wrap around
            }
            treeRow = treeRow + 2;  // 2 down
            if(treeRow>=numberOfRowsInForest) //break
                break;
            if(cMatrix[treeRow][treeCol]=='#') {
                _1_2_trees++;
            }
        }
    }
    static public void createInputMatrixFromFile(Scanner in) throws IOException {
        int i=0;
        ArrayList<char[]> chars = new ArrayList<>();
        while (in.hasNext()){
            chars.add(in.nextLine().toCharArray());
        }
        cMatrix = chars.toArray(new char[chars.size()][]);
        numberOfRowsInForest = cMatrix.length;
        numberOfColsInForest = cMatrix[0].length;
    }

}

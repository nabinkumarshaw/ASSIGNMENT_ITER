Q24)Write a Java program to demonstrate a checked exception (e.g.,
FileNotFoundException) being thrown and caught using try-catch block.

//code
package Assignment_5;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Q24 {
    public static void main(String[] args) {
        String filename = "nonexistentfile.txt";

        try {
            File file = new File(filename);
            Scanner sc = new Scanner(file);
            while (sc.hasNextLine()) {
                System.out.println(sc.nextLine());
            }
            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
        }
    }
}


//output
File not found: nonexistentfile.txt (The system cannot find the file specified)

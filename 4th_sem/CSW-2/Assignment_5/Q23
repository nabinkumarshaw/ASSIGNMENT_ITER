Q23)Write a program that reads data from a file and performs some processing. Handle 
checked IOException by using try-catch block to catch and handle the exception.

//code
package Assignment_5;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Q23 {
    public static void main(String[] args) {
        String f_name = "data.txt";
        try {
            BufferedReader reader = new BufferedReader(new FileReader(f_name));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            reader.close();
        } catch (IOException e) {
            System.out.println("An error occurred while reading the file: " + e.getMessage());
            e.printStackTrace();
        }
    }
}

//output
An error occurred while reading the file: data.txt (The system cannot find the file specified)
java.io.FileNotFoundException: data.txt (The system cannot find the file specified)

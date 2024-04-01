8. Write a Java program to find the quare root of integer numbers. Demonstrate the use of 
try-catch block to handle ArithmeticException.


//code
import java.util.Scanner;

public class Q08 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter an integer number : ");
        int number = sc.nextInt();
        try {
            double sqRoot = calculateSquareRoot(number);
            System.out.println("Square root of " + number + " is: " + sqRoot);
        } catch (ArithmeticException e) {
            System.err.println("ArithmeticException occurred: " + e.getMessage());
        }
        sc.close();
    }

    public static double calculateSquareRoot(int number) {
        if (number < 0) {
            throw new ArithmeticException("Cannot calculate square root of a negative number!");
        }
        return Math.sqrt(number);
    }
}

/**
 * OUTPUT
 // Enter an integer number :
 * 67
 * Square root of 67 is: 8.18535277187245

//Enter an integer number : 
-90
ArithmeticException occurred: java.lang.ArithmeticException: Cannot calculate square root of a negative number!
 */

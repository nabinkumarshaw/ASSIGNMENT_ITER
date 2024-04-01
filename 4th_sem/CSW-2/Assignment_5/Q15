15. Demonstration of use nested try-catch block. Write a Java program to handle 
NumberFormatException in outer try-catch block and ArithmeticException inside 
the inner try-catch block.

//code
package Assignment_5;

import java.util.Scanner;

public class Q15 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
            System.out.print("Enter a number: ");
            String input = sc.nextLine();
            try {
                int num = Integer.parseInt(input);
                try {
                    int result = 10 / num;
                    System.out.println("Result: " + result);
                }
                catch (ArithmeticException e) {
                    System.out.println("Error: ArithmeticException - Division by zero");
                }
            }
            catch (NumberFormatException e) {
                System.out.println("Error: NumberFormatException - Invalid input");
            }
    }
}



//output
Enter a number: jcfv
Error: NumberFormatException - Invalid input
Enter a number: 0
Error: ArithmeticException - Division by zero

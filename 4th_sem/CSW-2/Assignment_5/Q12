12)Create a Java application that calculates the value of the expression sqrt(abs(sin(x) * 
cos(x))) / (tan(x) + 1) for a given value of x. Handle cases where x leads to division 
by zero or negative values inside the square root function.

//code
package Assignment_5;

import java.util.Scanner;

public class Q12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Enter the value of x in degrees: ");
            double x_deg = sc.nextDouble();
            double x_rad = Math.toRadians(x_deg);

            double sinX = Math.sin(x_rad);
            double cosX = Math.cos(x_rad);

            double num = Math.sqrt(Math.abs(sinX * cosX));
            double den = Math.tan(x_rad) + 1;

            if (den == 0 || Double.isNaN(num)) {
                throw new ArithmeticException("Invalid mathematical operation");
            }

            double result = num / den;
            System.out.println("Result: " + result);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            sc.close();
        }
    }
}

//output
Enter the value of x in degrees: 78
Result: 0.07905223669134548

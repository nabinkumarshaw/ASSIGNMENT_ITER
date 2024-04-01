11. Write a Java program that computes the value of the function log(sin(x) + cos(x)) / 
(tan(x) - cot(x)) for a given value of x. Ensure proper handling of exceptions that may 
occur due to invalid mathematical operations

//code

import java.util.Scanner;

public class Q11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Enter the value of x in degrees: ");
            double x_deg = sc.nextDouble();
            double x_rad = Math.toRadians(x_deg);

            double res = Math.log((Math.sin(x_rad) + Math.cos(x_rad))/Math.tan(x_rad) - (1 / Math.tan(x_rad)));
            if (Double.isNaN(res)) {
                throw new ArithmeticException("Invalid mathematical operation");
            }
            System.out.println("Result: " + res);
        }
        catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

    }
}

//output
Enter the value of x in degrees: 78
Result: 0.03798608602161271
Enter the value of x in degrees: 0
Error: Invalid mathematical operation


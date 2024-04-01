10. Implement a Java program that calculates the value of the expression (sin(x) + cos(x)) 
/ tan(x) for a given value of x. Handle scenarios where x is close to multiples of π/2 to 
avoid division by zero errors.

//code
import java.util.Scanner;

public class Q10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.println("Enter the value of x in radians : ");
            double x = sc.nextDouble();
            double result = calculateExpressionValue(x);
            System.out.println("Result of (sin(x) + cos(x)) / tan(x) : "+result);
        } catch(Exception e) {
            System.err.println("An error occurred: "+e.getMessage());
        } finally {
            sc.close();
        }
    }

    public static double calculateExpressionValue(double x) {
        double sinX = Math.sin(x);
        double cosX = Math.cos(x);
        double tanX = Math.tan(x);
        if (Math.abs(tanX) < 1e-10) {
            throw new ArithmeticException("Division by zero is not allowed. x is close to a multiple of π/2.");
        }
        return (sinX + cosX) / tanX;
    }
}

/**
 * OUTPUT
 Enter the value of x in radians : 
 2 * MATH.PI
 Result of (sin(x) + cos(x)) / tan(x) : -0.22569409307820762
 */

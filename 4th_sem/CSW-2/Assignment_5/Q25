Q25) Implement a method that reads an integer from the user but handles
InputMismatchException using try-catch block

//code
package Assignment_5;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Q25 {
    public static void main(String[] args) {
        int user_inp = readIntegerFromUser();
        System.out.println("You entered: " + user_inp);
    }

    public static int readIntegerFromUser() {
        Scanner sc = new Scanner(System.in);
        int user_inp = 0;
        boolean valid_inp = false;

        do {
            try {
                System.out.print("Please enter an integer: ");
                user_inp = sc.nextInt();
                valid_inp = true;
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter an integer.");
                sc.nextLine();
            }
        } while (!valid_inp);

        sc.close();
        return user_inp;
    }
}

//output
Please enter an integer: 34
You entered: 34

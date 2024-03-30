Q28)Implement a Java program to handle StackOverflowError

//code
package Assignment_5;

public class Q28 {
    public static void main(String[] args) {
        try {
            rec(0);
        } catch (StackOverflowError e) {
            System.out.println("StackOverflowError caught: " + e.getMessage());
        }
    }
    public static void rec(int counter) {
        System.out.println("Counter: " + counter);
        rec(counter + 1);
    }
}

//output
Counter: 0
Counter: 1
Counter: 2
.....
....
....
...

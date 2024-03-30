Q27)Write a program to handle ClassCastException.

//code
package Assignment_5;

public class Q27 {
    public static void main(String[] args) {
        try {
            Object obj = "Hello";
            Integer num = (Integer) obj;
            System.out.println("Number: " + num);
        } catch (ClassCastException e) {
            System.out.println("ClassCastException caught: " + e.getMessage());
        }
    }
}


//output
ClassCastException caught: class java.lang.String cannot be cast to class java.lang.Integer (java.lang.String and java.lang.Integer are in module java.base of loader 'bootstrap')

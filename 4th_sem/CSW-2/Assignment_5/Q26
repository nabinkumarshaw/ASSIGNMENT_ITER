Q26) Implement try-catch-finally blocks to handle ClassNotFoundException and
MethodNotFoundException.

//code
package Assignment_5;

import java.lang.reflect.Method;

public class Q26 {
    public static void main(String[] args) {
        try {
            Class<?> cls = Class.forName("SomeClass");
            Method method = cls.getMethod("someMethod");
            method.invoke(null);
        } catch (ClassNotFoundException e) {
            System.out.println("Class not found: " + e.getMessage());
        } catch (NoSuchMethodException e) {
            System.out.println("Method not found: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            System.out.println("Finally block executed");
        }
    }
}


//output
Class not found: SomeClass
Finally block executed

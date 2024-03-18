Q1. Write a program to create a Student class that has members, name, roll
number, and age. Design the Student class in such a way that it can take
the roll number as an integer or string. Create a driver class that creates
student objects and invokes the methods.


//code

package Assignment_3_Generics_Collections;

class Students {
     String name;
     Object rollNumber;
     int age;

     Students(String name, Object rollNumber, int age) {
        this.name = name;
        this.rollNumber = rollNumber.toString();    // Convert roll number to string
        this.age = age;
    }

    public void display() {
        System.out.println("Name: " + name);
        System.out.println("Roll Number: " + rollNumber);
        System.out.println("Age: " + age);
    }

}
public class AssignmentQ1 {
    public static void main(String[] args) {
        Students student1 = new Students("Nabin", 62, 20);
        Students student2 = new Students("Rishab", "23", 27);

        student1.display();
        System.out.println();
        student2.display();
    }
}

//output
Name: Nabin
Roll Number: 62
Age: 20

Name: Rishab
Roll Number: 23
Age: 27


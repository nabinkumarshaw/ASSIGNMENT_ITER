Q4. Write a program to create a Student class with members name, rn, and
totalMark. Create an array of student objects and search a student object
using linear search from the array.
Note: Overload compareTo method of Comparable interface

//code
package Assignment_3_Generics_Collections;

class Student implements Comparable <Student> {
    private String name;
    private int rn;
    private int totalMark;

    Student(String name, int rn, int totalMark) {
        this.name = name;
        this.rn = rn;
        this.totalMark = totalMark;
    }
    public String getName() {
        return name;
    }
    public int getRollNumber() {
        return rn;
    }
    public int getTotalMark() {
        return totalMark;
    }
    @Override
    public int compareTo(Student otherStudent) {
        return Integer.compare(this.rn, otherStudent.rn);
    }

    @Override
    public String toString() {
        return "Name: " + name + ", Roll Number: " + rn + ", Total Marks: " + totalMark;
    }
}
public class AssignmentQ4 {
    public static void main(String[] args) {
        Student[] students = new Student[3];
        students[0] = new Student("Prithvi saw", 101, 85);
        students[1] = new Student("Axar patel", 102, 75);
        students[2] = new Student("Rishab pant", 103, 90);
        int search = 102; // Example roll number to search
        boolean found = false;
        for (Student stu : students) {
            if (stu.getRollNumber() == search) {
                System.out.println("Student found:");
                System.out.println(stu);
                found = true;
                break;
            }
        }
        if (found==false) {
            System.out.println("Student with roll number " + search + " not found.");
        }
    }
}


output
Name: Axar patel, Roll Number: 102, Total Marks: 75

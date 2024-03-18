Q5. Write a program to create a Student class with members name, rn, and
total mark. Create an array of student objects and sort it using Bubble
sort according to its rn.
Note: Overload compareTo method of Comparable interface.

//code
package Assignment_3_Generics_Collections;

class Student1 implements Comparable <Student1> {
    private String name;
    private int rn;
    private int totalMark;

    Student1(String name, int rn, int totalMark) {
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
    public int compareTo(Student1 otherStudent) {
        return Integer.compare(this.rn, otherStudent.rn);
    }
    @Override
    public String toString() {
        return "Name: " + name + ", Roll Number: " + rn + ", Total Marks: " + totalMark;
    }
    public static void bubbleSort(Student1[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
                if (arr[j].compareTo(arr[j+1]) > 0) {
                    Student1 temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
}

public class AssignmentQ5 {
    public static void main(String[] args) {
        Student1[] students = new Student1[5];
        students[0] = new Student1("Rohit", 105, 85);
        students[1] = new Student1("Hardik", 102, 75);
        students[2] = new Student1("Ishan", 103, 90);
        students[3] = new Student1("Bumrha", 101, 80);
        students[4] = new Student1("Suryakumar", 104, 95);

        Student1.bubbleSort(students);
        System.out.println("Sorted Students (by roll number):");
        for (Student1 student : students) {
            System.out.println(student);
        }
    }
}



//output
Sorted Students (by roll number):
Name: Bumrha, Roll Number: 101, Total Marks: 80
Name: Hardik, Roll Number: 102, Total Marks: 75
Name: Ishan, Roll Number: 103, Total Marks: 90
Name: Suryakumar, Roll Number: 104, Total Marks: 95
Name: Rohit, Roll Number: 105, Total Marks: 85

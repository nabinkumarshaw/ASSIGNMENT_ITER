Q2. Write a program to create a Book class with member variables bookId,
bookName, and price. Add the respective method and constructor to it.
Create a driver class in that class and create two book objects. Compare
the book objects according to their price. Print the details of the book
objects.
Note: Overload toString and equals method.


//code

package Assignment_3_Generics_Collections;

class Book {
    private int bookId;
    private String bookName;
    private double price;

     Book(int bookId, String bookName, double price) {
        this.bookId = bookId;
        this.bookName = bookName;
        this.price = price;
    }
    public int getBookId() {
        return bookId;
    }

    public String getBookName() {
        return bookName;
    }
    public double getPrice() {
        return price;
    }
    @Override
    public String toString() {
        return "Book ID: " + bookId + ", Book Name: " + bookName + ", Price: $" + price;
    }
    @Override
    public boolean equals(Object obj) {
        Book b = (Book) (obj);
        return this.bookId == b.bookId && this.bookName.equals(b.bookName) && this.price == b.price;
    }
}
public class AssignmentQ2 {
    public static void main(String[] args) {
        Book book1 = new Book(101, "Java Programming", 300.50);
        Book book2 = new Book(102, "DSA", 295.75);

        System.out.println("Details of Book 1:");
        System.out.println(book1);

        System.out.println("Details of Book 2:");
        System.out.println(book2);

        if (book1.getPrice() < book2.getPrice()) {    // Comparing books prices
            System.out.println("Book 1 is cheaper than Book 2.");
        } else if (book1.getPrice() > book2.getPrice()) {
            System.out.println("Book 2 is cheaper than Book 1.");
        } else {
            System.out.println("Both books have the same price.");
        }
    }
}


//output
Details of Book 1:
Book ID: 101, Book Name: Java Programming, Price: $300.5
Details of Book 2:
Book ID: 102, Book Name: DSA, Price: $295.75
Book 2 is cheaper than Book 1.

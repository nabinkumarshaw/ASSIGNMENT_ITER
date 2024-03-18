Q3. Write a program to create a Car class with member variables model, color,
and speed. Add the respective method and constructor to it. Create a
driver class in that class and create two car objects. Compare the car
objects according to their speed and print the details of the car that has
a greater speed.
Note: Overload compareTo method of Comparable interface.


//code

package Assignment_3_Generics_Collections;

class Car implements Comparable <Car> {
    private String model;
    private String color;
    private double speed;

     Car(String model, String color, double speed) {
        this.model = model;
        this.color = color;
        this.speed = speed;
    }

    public String getModel() {
        return model;
    }
    public String getColor() {
        return color;
    }
    public double getSpeed() {
        return speed;
    }

    @Override
    public int compareTo(Car otherCar) {
        return Double.compare(this.speed, otherCar.speed);
    }

    @Override
    public String toString() {
        return "Model: " + model + ", Color: " + color + ", Speed: " + speed + " mph";
    }
}

public class AssignmentQ3 {
    public static void main(String[] args) {
        Car car1 = new Car("Audi", "Black", 120.5);
        Car car2 = new Car("BMW", "White", 115.0);

        System.out.println("Details of Car 1:");
        System.out.println(car1);

        System.out.println("Details of Car 2:");
        System.out.println(car2);

        // Comparing cars speeds
        int Result = car1.compareTo(car2);
        if (Result > 0) {
            System.out.println("Car 1 has a greater speed than Car 2.");
            System.out.println("Details of Car with greater speed:" + car1);
        } else if (Result < 0) {
            System.out.println("Car 2 has a greater speed than Car 1.");
            System.out.println("Details of Car with greater speed:" + car2);
        } else {
            System.out.println("Both cars have the same speed.");
        }
    }
}


//output

Details of Car 1:
Model: Audi, Color: Black, Speed: 120.5 mph
Details of Car 2:
Model: BMW, Color: White, Speed: 115.0 mph
Car 1 has a greater speed than Car 2.
Details of Car with greater speed:Model: Audi, Color: Black, Speed: 120.5 mph

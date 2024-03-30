Q19)Implement a Java program that performs complex manipulations on an array of 
integers. The program should involve operations such as sorting, searching, and 
accessing elements at various indices. Introduce scenarios, where accessing elements 
beyond the bounds of the array leads to ArrayIndexOutOfBoundsException. Your 
task is to handle these exceptions gracefully and ensure the program continues 
execution without crashing.

//code
package Assignment_5;

import java.util.Arrays;

public class Q19 {
    public static void main(String[] args) {
        int[] arr = {5, 2, 8, 1, 3};
        try {
            Arrays.sort(arr);
            System.out.println("Sorted array: " + Arrays.toString(arr));
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Caught ArrayIndexOutOfBoundsException during sorting: " + e.getMessage());
        }
        try {
            int idx = bin_src(arr, 10);
            System.out.println("Element found at index: " + idx);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Caught ArrayIndexOutOfBoundsException during searching: " + e.getMessage());
        }
        try {
            System.out.println("Element at index 10: " + arr[10]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Caught ArrayIndexOutOfBoundsException while accessing element at index 10: " + e.getMessage());
        }
    }
    public static int bin_src(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
}

//output
Sorted array: [1, 2, 3, 5, 8]
Element found at index: -1
Caught ArrayIndexOutOfBoundsException while accessing element at index 10: Index 10 out of bounds for length 5

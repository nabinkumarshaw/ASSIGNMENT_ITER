Q18)Develop a recursive algorithm implemented in Java that traverses or manipulates 
arrays. Introduce scenarios where the recursion reaches beyond the bounds of the array, 
resulting in ArrayIndexOutOfBoundsException. Your task is to handle these 
exceptions within the recursive algorithm and ensure proper termination of recursion

//code
package Assignment_5;

public class Q18 {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int sum = cal_sum(arr, 0);
        System.out.println("Sum of array elements: " + sum);
    }
    public static int cal_sum(int[] arr, int idx) {
        if (idx == arr.length) {
            return 0;
        }
        int curr_ele = 0;
        try {
            curr_ele = arr[idx];
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Caught ArrayIndexOutOfBoundsException at index " + idx);
        }
        int sum = 0;
        try {
            sum = cal_sum(arr, idx + 1);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Caught ArrayIndexOutOfBoundsException during recursion at index " + (idx + 1));
        }
        return curr_ele + sum;
    }
}

//output
Sum of array elements: 15

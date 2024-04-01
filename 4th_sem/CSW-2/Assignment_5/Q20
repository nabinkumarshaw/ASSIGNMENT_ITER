Q20)Develop a recursive algorithm implemented in Java that traverses or manipulates 
arrays. Introduce scenarios where the recursion reaches beyond the bounds of the array, 
resulting in ArrayIndexOutOfBoundsException. Your task is to handle these 
exceptions within the recursive algorithm and ensure proper termination of recursion

//code

public class Q20 {
        public static void main(String[] args) {
            int[] arr = {1, 2, 3, 4, 5};
            traverseArray(arr, 0);
        }

        public static void traverseArray(int[] arr, int index) {
            try {
                System.out.println("Element at index " + index + ": " + arr[index]);
                traverseArray(arr, index + 1);
            }
            catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Reached end of array or index out of bounds.");
            }
        }
    }






//output
Element at index 0: 1
Element at index 1: 2
Element at index 2: 3
Element at index 3: 4
Element at index 4: 5
Reached end of array or index out of bounds.

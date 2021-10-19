public class RotateArray {

    public static void main(String[] args) {

        int[] arr = {10,20,30,40,50};

        // third arg is right rotate or left rotate by so many positions

        RotateArray.rotate(arr, 3, false);

    }




    // rotate left or right by num positions

    // there is a better algorithm using modulo operator as well.

    // Students please experiment with this code and find better ways to accomplish this

    public static void rotate(int[] arr, int num, boolean right)

    {

        int tmp = num;

        if (right == true) { // rotate to right

            while (tmp > 0) {

                int last = arr[arr.length - 1];

                for (int i = arr.length - 1; i > 0; i--) {

                    arr[i] = arr[i - 1];

                }

                arr[0] = last;

                tmp--;

            }

        } else // since while is one statement in else block we do not need a curly brace.

            while (tmp > 0) { // rotate to left

                int first = arr[0];

                for (int i =0; i<arr.length-1; i++) {

                    arr[i] = arr[i+1];

                }

                arr[arr.length -1 ] = first;

                tmp--;

            }

        printarr(arr);

    }




    public static void printarr(int[] arr)

    {

        for (int i =0; i < arr.length; i++)

            System.out.println("i = " + i + " " + arr[i]);

    }

}


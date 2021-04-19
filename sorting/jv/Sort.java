import java.util.Arrays;
public class Sort {
    
    public static int[] bubble(int[] arr) {
        for (int i = 0; i < arr.length -1; i++) {
            boolean finished = true;
            for (int j = 0; j < arr.length -i -1; j++) {
                if (arr[j] > arr[j+1]) {
                    finished = false;
                    int temp = arr[j+1];
                    arr[j+1] = arr[j];
                    arr[j] = temp;
                    System.out.println(Arrays.toString(arr));
                }
            }
            if (finished == true) {
                return arr;
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        int[] a = {5,3,6,2,8,1,2,5,2,8,4,9};
        a = Sort.bubble(a);
        System.out.print(Arrays.toString(a));
    }
}

public class Search {
    
    public static Integer binary(int[] arr, int val) {
        boolean found = false;
        int start = 0;
        int end = arr.length - 1;
        Integer mid = -1;
        while ((start <= end) && (found == false)) {
            mid = (start + end) / 2;
            
            if (arr[mid] == val) {
                found = true;
            } else if (arr[mid] > val) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return (found == true) ? mid : null;
    }


    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7,8,9};
        Integer a = Search.binary(arr, 6);
        Integer b = Search.binary(arr, 10);
        System.out.println(a);
        System.out.println(b);
    }
}

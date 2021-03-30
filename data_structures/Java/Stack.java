package Java;
import java.util.Arrays;
import java.util.ArrayList;

public class Stack <T>{
    private Node start;
    private int size;

    class Node {
        private T data;
        private Node pointer;

        Node(T data) {
            this.data = data;
            pointer = null;
        }

        public T getData() {
            return data;
        }

        public Node getPointer() {
            return pointer;
        }

        public void setPointer(Node node) {
            pointer = node;
        }
    }

    Stack() {
        start = null;
        size = 0;
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<Integer>();
        Integer[] items = {1,2,3,4,5,6,7,8,9,10};
        for (Integer i : items) {
            stack.push(i);
        }
        System.out.println(stack.peek());
        System.out.println(stack.pop());
        ArrayList<Integer> contents = stack.empty();
        System.out.println(Arrays.toString(contents.toArray(new Integer[0])));

        System.out.println(stack.size);

    }

    public void push(T data) {
        Node new_node = new Node(data);
        new_node.setPointer(start);
        start = new_node;
        size ++;
    }

    public T pop() {
        if (start != null) {
            T popped = start.data;
            start = start.pointer;
            size --;
            return popped;
        } else {
            return null;
        }
    }

    public T peek() {
        if (start != null) {
            return start.data;
        } else {
            return null;
        }
    }

    public ArrayList<T> empty() {
        ArrayList<T> contents = new ArrayList<T>();
        int s = size;
        for (int i = 0; i < s; i++) {
            T val = this.pop();
            contents.add(val);
        }
        return contents;
    }
}

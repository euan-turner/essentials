package Java;
import java.util.Arrays;

public class Stack {
    private Node start;
    private int size;

    static class Node {
        private int data;
        private Node pointer;

        Node(int data) {
            this.data = data;
            pointer = null;
        }

        public int getData() {
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
        Stack stack = new Stack();
        int[] items = {1,2,3,4,5,6,7,8,9,10};
        for (int i : items) {
            stack.push(i);
        }
        System.out.println(stack.peek());
        System.out.println(stack.pop());
        int[] contents = stack.empty();
        System.out.println(Arrays.toString(contents));

        System.out.println(stack.size);

    }

    public void push(int data) {
        Node new_node = new Node(data);
        new_node.setPointer(start);
        start = new_node;
        size ++;
    }

    public Integer pop() {
        if (start != null) {
            Integer popped = start.data;
            start = start.pointer;
            size --;
            return popped;
        } else {
            return null;
        }
    }

    public Integer peek() {
        if (start != null) {
            return start.data;
        } else {
            return null;
        }
    }

    public int[] empty() {
        int[] contents = new int[size];
        int s = size;
        for (int i = 0;i < s;i++) {
            Integer val = this.pop();
            contents[i] = val;
        }
        return contents;
    }
}

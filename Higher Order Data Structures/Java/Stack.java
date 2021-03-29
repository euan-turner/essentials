package Java;

public class Stack {
    private Node start;
    private int size;

    static class Node {
        private int data;
        private Node pointer;

        Node(int value) {
            this.data = value;
            this.pointer = null;
        }
    }

    Stack() {
        this.start = null;
        this.size = 0;
    }

    public static void main(String[] args) {
        Stack stack = new Stack();
        int[] items = {1,2,3,4,5,6,7,8,9,10};
        for (int i : items) {
            stack.push(i);
        }
        System.out.println(stack.peek());
        int[] contents = stack.empty();
        for (int c : contents) {
            System.out.println(c);
        }
        System.out.println(stack.size);

    }

    public void push(int data) {
        Node new_node = new Node(data);
        new_node.pointer = this.start;
        this.start = new_node;
        this.size ++;
    }

    public int pop() {
        if (this.start != null) {
            int popped = this.start.data;
            this.start = this.start.pointer;
            this.size --;
            return popped;
        } else {
            return -1;
        }
    }

    public Integer peek() {
        if (this.start != null) {
            return this.start.data;
        } else {
            return null;
        }
    }

    public int[] empty() {
        int[] contents = new int[this.size];
        int s = this.size;
        for (int i = 0;i < s;i++) {
            contents[i] = this.pop();
        }
        return contents;
    }
}

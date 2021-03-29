package Java;

public class Queue {
    
    private Node front_pointer;
    private Node back_pointer;
    private int size;

    static class Node {
        private int value;
        private Node next;

        Node(int value) {
            this.value = value;
            next = null;
        }

        public int getValue() {
            return value;
        }

        public Node getNext() {
            return next;
        }

        public void setNext(Node node) {
            next = node;
        }

    }

    Queue() {
        Node front_pointer = null;
        Node back_pointer = null;
        int size = 0;
    }

    public static void main(String[] args) {
        int[] data = {25, 39, 46, 20, 3, 23, 35, 32, 8, 16, 12, 33, 36, 31, 49, 41, 2, 4, 6, 9, 17, 34, 24, 13, 0, 42, 37, 40, 44, 30};
        Queue queue = new Queue();
        for (int d : data) {
            queue.enqueue(d);
        }
        System.out.println(queue.get_head().value);
        System.out.println(queue.get_tail().value);
        do {
            System.out.println(queue.dequeue());
        } 
        while (queue.size>0);
    }

    public Node get_head() {
        return front_pointer;
    }

    public Node get_tail() {
        return back_pointer;
    }

    public void enqueue(int data) {
        Node new_node = new Node(data);
        //Check if queue is empty
        if (back_pointer == null) {
            front_pointer = new_node;
        } else {
            back_pointer.next = new_node;
        }

        back_pointer = new_node;
        size ++;
    }

    public Integer dequeue() {
        //Check for queue underflow
        if (front_pointer != null) {
            Integer popped = front_pointer.value;
            front_pointer = front_pointer.next;
            size --;

            //Check if last item was popped
            if (front_pointer == null) {
                back_pointer = null;
            }
            return popped;
        } else {
            return null;
        }
    }
}

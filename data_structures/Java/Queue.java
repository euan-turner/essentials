package Java;

public class Queue<T> {
    
    private Node front_pointer;
    private Node back_pointer;
    private int size;

    class Node {
        private T value;
        private Node next;

        Node(T value) {
            this.value = value;
            next = null;
        }

        public T getValue() {
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
        Integer[] data = {25, 39, 46, 20, 3, 23, 35, 32, 8, 16, 12, 33, 36, 31, 49, 41, 2, 4, 6, 9, 17, 34, 24, 13, 0, 42, 37, 40, 44, 30};
        Queue<Integer> queue = new Queue<Integer>();
        for (int d : data) {
            queue.enqueue(d);
        }
        System.out.println(queue.get_head());
        System.out.println(queue.get_tail());
        do {
            System.out.println(queue.dequeue());
        } 
        while (queue.size>0);
    }

    public T get_head() {
        return front_pointer.value;
    }

    public T get_tail() {
        return back_pointer.value;
    }

    public void enqueue(T data) {
        Node new_node = new Node(data);
        //Check if queue is empty
        if (back_pointer == null) {
            front_pointer = new_node;
        } else {
            back_pointer.setNext(new_node);
        }

        back_pointer = new_node;
        size ++;
    }

    public T dequeue() {
        //Check for queue underflow
        if (front_pointer != null) {
            T popped = front_pointer.value;
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

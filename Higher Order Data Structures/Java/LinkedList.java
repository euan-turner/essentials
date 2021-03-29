package Java;
import java.util.Arrays;

public class LinkedList {
    private Node start_pointer;
    private int size;
    

    static class Node {
        private int data;
        private Node pointer;

        Node(int data){
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

    LinkedList() {
        Node start_pointer = null;
        int size = 0;
    }

    public static void main(String[] args) {
        int[] vals = {5,3,7,1,6,3};
        LinkedList ll = new LinkedList();
        for (int val : vals) {
            ll.add_node(val);
        }
        int[] output = ll.traverse();
        System.out.println(Arrays.toString(output));

        ll.reverse();
        int[] new_out = ll.traverse();
        System.out.println(Arrays.toString(new_out));
    }

    public void add_node(int data) {
        Node new_node = new Node(data);
        Node current = start_pointer;
        if (current == null) {
            //Check if list is empty
            start_pointer = new_node;
        } else if (new_node.data < current.data) {
            //New node should be placed before first node
            new_node.setPointer(current);
            start_pointer = new_node;
        } else {
            Node previous = current;
            while ((current != null) && (new_node.data > current.data)) {
                previous = current;
                current = current.pointer;
            }
            new_node.setPointer(previous.pointer);
            previous.setPointer(new_node);
        }
        size ++;
    }

    public int[] traverse() {
        int[] arr = new int[size];
        Node current = start_pointer;
        //Return array of 0s if ll is empty
        if (current == null) {
            return arr;
        } else {
            for (int i = 0;i < arr.length;i++) {
                arr[i] = current.data;
                current = current.pointer;
            }
            return arr;
        }
    }

    public boolean delete_node(int val) {
        //Check if ll is empty
        if (start_pointer == null) {
            return false;
        } else if (start_pointer.data == val) {
            //Removing first item from ll
            start_pointer = start_pointer.pointer;
            size --;
            return true;
        } else {
            Node current = start_pointer;
            Node previous = current;
            while (current.data != val) {
                previous = current;
                current = current.pointer;
                if (current == null) {
                    //Item not in ll
                    return false;
                }
            }
            previous.setPointer(current.pointer);
            size --;
            return true;
        }
    }

    public void reverse() {
        Node current = start_pointer;
        Node next = current.pointer;
        while (next != null) {
            Node next_next = next.pointer;

            //Specific case for first node
            if (current == start_pointer) {
                current.pointer = null;
            }

            next.pointer = current;
            current = next;
            next = next_next;
        }
        start_pointer = current;
    }


}

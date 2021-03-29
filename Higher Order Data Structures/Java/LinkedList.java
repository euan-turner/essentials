package Java;

public class LinkedList {
    private Node start_pointer;
    private int size;
    

    static class Node {
        private int data;
        private Node pointer;

        Node(int data){
            this.data = data;
            this.pointer = null;
        }

        public int getData() {
            return this.data;
        }

        public Node getPointer() {
            return this.pointer;
        }

        public void setPointer(Node node) {
            this.pointer = node;
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
        Node[] output = ll.traverse();
        for (Node node : output) {
            System.out.println(node.data);
        }
        ll.reverse();
        Node[] new_out = ll.traverse();
        for (Node node : new_out) {
            System.out.println(node.data);
        }
    }

    public void add_node(int data) {
        Node new_node = new Node(data);
        Node current = this.start_pointer;
        if (current == null) {
            //Check if list is empty
            this.start_pointer = new_node;
        } else if (new_node.data < current.data) {
            //New node should be placed before first node
            new_node.pointer = current;
            this.start_pointer = new_node;
        } else {
            Node previous = current;
            while ((current != null) && (new_node.data > current.data)) {
                previous = current;
                current = current.pointer;
            }
            new_node.pointer = previous.pointer;
            previous.pointer = new_node;
        }
        this.size ++;
    }

    public Node[] traverse() {
        Node[] arr = new Node[this.size];
        Node current = this.start_pointer;
        //Return array of 0s if ll is empty
        if (current == null) {
            return arr;
        } else {
            for (int i = 0;i < arr.length;i++) {
                arr[i] = current;
                current = current.pointer;
            }
            return arr;
        }
    }

    public boolean delete_node(int val) {
        //Check if ll is empty
        if (this.start_pointer == null) {
            return false;
        } else if (this.start_pointer.data == val) {
            //Removing first item from ll
            this.start_pointer = this.start_pointer.pointer;
            this.size --;
            return true;
        } else {
            Node current = this.start_pointer;
            Node previous = current;
            while (current.data != val) {
                previous = current;
                current = current.pointer;
                if (current == null) {
                    //Item not in ll
                    return false;
                }
            }
            previous.pointer = current.pointer;
            this.size --;
            return true;
        }
    }

    public void reverse() {
        Node current = this.start_pointer;
        Node next = current.pointer;
        while (next != null) {
            Node next_next = next.pointer;

            //Specific case for first node
            if (current == this.start_pointer) {
                current.pointer = null;
            }

            next.pointer = current;
            current = next;
            next = next_next;
        }
        this.start_pointer = current;
    }


}

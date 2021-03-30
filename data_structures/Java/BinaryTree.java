package Java;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Vector;
import Queue;

public class BinaryTree {

    private Node head;
    private int size;

    BinaryTree() {
        head = null;
    }
    
    static class Node {
        private int value;
        private Node left;
        private Node right;

        Node(int value) {
            this.value = value;
            left = null;
            right = null;
        }

        public int getValue() {
            return value;
        }

        public Node getLeft() {
            return left;
        }

        public Node getRight() {
            return right;
        }

        public void setLeft(Node node) {
            left = node;
        }

        public void setRight(Node node) {
            right = node;
        }

    }

    public static void main(String[] args) {
        int[] data = {25, 39, 46, 20, 3, 23, 35, 32, 8, 16, 12, 33, 36, 31, 49, 41, 2, 4, 6, 9, 17, 34, 24, 13, 0, 42, 37, 40, 44, 30};
        BinaryTree bin_tree = new BinaryTree();

        for (int i : data){
            bin_tree.addNode(i);
        }
        Integer[] in_order = bin_tree.getInOrder();
        Integer[] pre_order = bin_tree.getPreOrder();
        Integer[] post_order = bin_tree.getPostOrder();
        System.out.println("In order: " + Arrays.toString(in_order));
        System.out.println("Pre order: " + Arrays.toString(pre_order));
        System.out.println("Post order: " + Arrays.toString(post_order));

        Integer[] bfs = bin_tree.breadth_first();
        System.out.println("Breadth first: " + Arrays.toString(bfs));
        // boolean success = bin_tree.deleteNode(23);
        // if (success == true) {
        //     in_order = bin_tree.getInOrder();
        //     System.out.println(in_order);
        // }
        // bin_tree.reverse();
        // int[] rev_in_order = bin_tree.getInOrder();
        // System.out.println(rev_in_order);
        // int height = bin_tree.getHeight();
        // System.out.println(height);
    }

    public void addNode(int new_value) {
        size = size+1;
        Node new_node = new Node(new_value);
        Node current_node = head;
        Node previous_node = current_node;
        //Binary Tree is current empty
        if (current_node == null) {
            head = new_node;
        } else {
            while (current_node != null) {
                previous_node = current_node;
                current_node = (new_value > current_node.value) ? current_node.right : current_node.left;
            }
            if (new_value < previous_node.value) {
                previous_node.setLeft(new_node);
            } else if (new_value > previous_node.value) {
                previous_node.setRight(new_node);
            }
        }
    }

    private void genInOrder(Node current_node, ArrayList<Integer> values) {
        if (current_node != null) {
            if (current_node.left != null) {
                genInOrder(current_node.left, values);
            }
            values.add(current_node.value);
            if (current_node.right != null) {
                genInOrder(current_node.right, values);
            }
        }
    }

    public Integer[] getInOrder() {
        ArrayList<Integer> output = new ArrayList<Integer>();
        //Vector<Integer> output = new Vector<>();
        genInOrder(head, output);
        Integer[] out = output.toArray(new Integer[0]);
        return out;
    }

    //Pre-Order generating [root, pre-order] values
    private void genPreOrder(Node current_node, ArrayList<Integer> values) {
        if (current_node != null) {
            values.add(current_node.value);
            if (current_node.left != null) {
                genPreOrder(current_node.left, values);
            }
            if (current_node.right != null) {
                genPreOrder(current_node.right, values);
            }
        }
    }

    public Integer[] getPreOrder() {
        ArrayList<Integer> output = new ArrayList<Integer>();
        genPreOrder(head, output);
        Integer[] out = output.toArray(new Integer[0]);
        return out;
    }

    private void genPostOrder(Node current_node, ArrayList<Integer> values) {
        if (current_node != null) {
            if (current_node.left != null) {
                genPostOrder(current_node.left, values);
            }
            if (current_node.left != null) {
                genPostOrder(current_node.right, values);
            }
            values.add(current_node.value);
        }
    }

    public Integer[] getPostOrder() {
        ArrayList<Integer> output = new ArrayList<Integer>();
        genPostOrder(head,output);
        Integer[] out = output.toArray(new Integer[0]);
        return out;
    }

    //add bfs when queue can be imported
    public Integer[] breadth_first() {
        Node current = head;
        Queue<Node> q = new Queue<Node>();
        ArrayList<Integer> output = new ArrayList<Integer>();
        while (current != null) {
            output.add(current.value);

            if (current.left != null) {
                q.enqueue(current.left);
            }
            if (current.right != null) {
                q.enqueue(current.right);
            }

            current = q.dequeue();
        }
        Integer[] out = output.toArray(new Integer[0]);
        return out;
    }

    private void reverseTree(Node current_node) {
        if (current_node == null) {
            return;
        }
        Node temp_left = current_node.left;
        current_node.setLeft(current_node.right);
        current_node.setRight(temp_left);
        reverseTree(current_node.left);
        reverseTree(current_node.right);
    }

    public void reverse() {
        reverseTree(head);
    }

    private int genHeight(Node current_node) {
        if (current_node != null) {
            return 1 + Math.max(genHeight(current_node.left),genHeight(current_node.right));   
        } else {
            return -1;
        }
    }

    public int getHeight() {
        int height = genHeight(head);
        return height;
    }

    public boolean deleteNode(int val) {
        boolean success;
        Node current = head;
        Node previous = current;
        while ((current != null) && (current.value != val)) {
            previous = current;
            if (val < current.value) {
                current = current.left;
            } else if (val > current.value) {
                current = current.right;
            }
        }
        if (current == null) {
            //Node to delete does not exist
            success = false;

        } else if ((current.left == null) && (current.right) == null) {
            //Node has no children
            if (current == head) {
                //Case for deleting head of tree
                head = null;
            } else if (previous.value > current.value) {
                previous.left = null;                
            } else {
                previous.right = null;
            }
            success =  true;

        } else if (current.right == null) {
            //Node only has a left child
            if (current == head) {
                //Case for deleting head of tree
                head = current.left;
            } else if (previous.value > current.value) {
                previous.left = current.left;
            } else {
                previous.right = current.right;
            }
            success =  true;

        } else if (current.left == null) {
            //Node only has a right child
            if (current == head) {
                //Case for deleting head of tree
                head = current.right;
            } else if (previous.value > current.value){
                previous.left = current.right;
            } else {
                previous.right = current.right;
            }
            success = true;

        } else {
            //Node exists and has two children - Hibbard deletion
            Node rightNode = current.right;
            if (rightNode.left != null) {
                //Right node has a left subtree
                Node min = rightNode;
                while (min.left != null) {
                    //Find smallest node in subtree
                    previous = min;
                    min = min.left;
                }
                current.value = min.value; //Overwrite deleting node
                previous.left = null; //Erase moved node
            } else {
                //Right node has no subtree
                current.value = rightNode.value;
                current.right = rightNode.right;
            }
            success = true;
        }
        return success;
    }
}



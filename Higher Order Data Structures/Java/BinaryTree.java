package Java;
import java.util.Vector;
 

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
        Vector<Integer> in_order = bin_tree.getInOrder();
        //Vector<Integer> pre_order = bin_tree.getPreOrder();
        //Vector<Integer> post_order = bin_tree.getPostOrder();
        System.out.println(in_order);
        //System.out.println(pre_order);
        //System.out.println(post_order);
        boolean success = bin_tree.deleteNode(23);
        if (success == true) {
            in_order = bin_tree.getInOrder();
            System.out.println(in_order);
        }
        bin_tree.reverse();
        Vector<Integer> rev_in_order = bin_tree.getInOrder();
        System.out.println(rev_in_order);
        int height = bin_tree.getHeight();
        System.out.println(height);
    }

    public void addNode(int value) {
        size = size+1;
        Node new_node = new Node(value);
        Node current_node = head;
        Node previous_node = current_node;
        //Binary Tree is current empty
        if (current_node == null) {
            head = new_node;
        } else {
            while (current_node != null) {
                previous_node = current_node;
                current_node = (value > current_node.getValue()) ? current_node.getRight() : current_node.getLeft();
            }
            if (value < previous_node.getValue()) {
                previous_node.setLeft(new_node);
            } else if (value > previous_node.getValue()) {
                previous_node.setRight(new_node);
            }
        }
    }

    private void genInOrder(Node current_node, Vector<Integer> values) {
        if (current_node != null) {
            if (current_node.getLeft() != null) {
                genInOrder(current_node.getLeft(), values);
            }
            values.add(values.size(),current_node.getValue());
            if (current_node.getRight() != null) {
                genInOrder(current_node.getRight(), values);
            }
        }
    }

    public Vector<Integer> getInOrder() {
        Vector<Integer> output = new Vector<>();
        genInOrder(head, output);
        return output;
    }

    //Pre-Order generating [root, pre-order] values
    private void genPreOrder(Node current_node, Vector<Integer> values) {
        if (current_node != null) {
            values.add(values.size(),current_node.getValue());
        
            if (current_node.getLeft() != null) {
                genPreOrder(current_node.getLeft(), values);
            }
            if (current_node.getRight() != null) {
                genPreOrder(current_node.getRight(), values);
            }
        }
    }

    public Vector<Integer> getPreOrder() {
        Vector<Integer> output = new Vector<>();
        genPreOrder(head, output);
        return output;
    }

    private void genPostOrder(Node current_node, Vector<Integer> values) {
        if (current_node != null) {
            if (current_node.getLeft() != null) {
                genPostOrder(current_node.getLeft(), values);
            }
            if (current_node.getRight() != null) {
                genPostOrder(current_node.getRight(), values);
            }
            values.add(values.size(),current_node.getValue());
        }
    }

    public Vector<Integer> getPostOrder() {
        Vector<Integer> output = new Vector<>();
        genPostOrder(head,output);
        return output;
    }

    //add bfs when queue can be imported

    private void reverseTree(Node current_node) {
        if (current_node == null) {
            return;
        }
        Node temp_left = current_node.getLeft();
        current_node.setLeft(current_node.getRight());
        current_node.setRight(temp_left);
        reverseTree(current_node.getLeft());
        reverseTree(current_node.getRight());
    }

    public void reverse() {
        reverseTree(head);
    }

    private int genHeight(Node current_node) {
        if (current_node != null) {
            return 1 + Math.max(genHeight(current_node.getLeft()),genHeight(current_node.getRight()));   
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
        Node current = this.head;
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
            if (current == this.head) {
                //Case for deleting head of tree
                this.head = null;
            } else if (previous.value > current.value) {
                previous.left = null;                
            } else {
                previous.right = null;
            }
            success =  true;

        } else if (current.right == null) {
            //Node only has a left child
            if (current == this.head) {
                //Case for deleting head of tree
                this.head = current.left;
            } else if (previous.value > current.value) {
                previous.left = current.left;
            } else {
                previous.right = current.right;
            }
            success =  true;

        } else if (current.left == null) {
            //Node only has a right child
            if (current == this.head) {
                //Case for deleting head of tree
                this.head = current.right;
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



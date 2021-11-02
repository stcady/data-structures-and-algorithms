    public  static class Node<T> {

        T data;

        Node next;




        Node(T value) {

            data = value;

            next = null;

        }




        public void printNode() {

            System.out.println("Value of the node is " + data);

            //print the node and its properties if any

            //this is useful of the T itself is a object and not a primitive type

        }

    }

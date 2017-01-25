// forked from Ryans Linked list breakdown:
function ListNode(value){
    this.val = value;
    this.next = null;
    };

var node1 = new ListNode("Node One");
var node2 = new ListNode("Node Two");
var node3 = new ListNode("Node Three");
node1.next = node2;
node2.next = node3;

function LinkedList(){
    this.head = null;
    this.isEmpty = function(){
        return !this.head;
    };

    this.addFront = function(value){
        var newNode = new ListNode(value);
        newNode.next = this.head;
        this.head = newNode;
    };

    this.length = function(){
        var currentNode = this.head;
        var len = 0;
        while(currentNode != null){
            len += 1;
            currentNode = currentNode.next;
        };
        return len;
    };


    this.getNode = function(num){
        var currentNode = this.head;
        var index = 1;
        while(currentNode != null){
            if(index == num){
                return currentNode;
            };
            index += 1;
            currentNode = currentNode.next;
        };
    };

    this.addBack = function(value){
        var currentNode = this.head;
        while(currentNode.next){
            currentNode = currentNode.next;
        };
        var newNode = new ListNode(value);
        currentNode.next = newNode;
    };

    this.removeFront = function(value){
        var currentNode = this.head;
        var tempNode = this.head;
        while(currentNode == this.head){
            console.log('currentNode is equal to head!')
            this.head = this.next;
            return this;
        };
        console.log('we made it out!');
    };
};

var Alpha_list = new LinkedList();
Alpha_list.head = node1;
// console.log(Alpha_list.length());
// console.log(Alpha_list.getNode(3).value);
console.log(Alpha_list.removeFront().value);

function Node(data){
    this.data = data;
    this.next = null;
}

function NodeStack() {
    this.data = null;
    this.isEmpty = function() {
        return !this._data;
    }
    this.top = function() {
        if (this.isEmpty()) {
            return null;
        }
        return this._data.data;
    };

this.pop = function(){

this.push = function(data) {
    var node = new Node(data);
    if (this.isEmpty()) {
        this._data = node;
    } else {
        node.next = this._data
        this.data = node;
    }
}
}

}


var ns1 = new NodeStack();
console.log(ns1.top());

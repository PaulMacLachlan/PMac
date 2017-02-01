function ArrStack(){
	var _data = [];
	this.show = function(){
		console.log(_data);
		return this;
	}
	this.push = function(val){
		_data.push(val);
		return this;
	}
	this.pop = function(){
		return _data.shift();
	}
	this.isEmpty = function(){
		return !_data.length;
	}
	this.size = function(){
		return _data.length;
	}
	this.top = function(){
		return _data[0];
	}
	this.contains = function(val){
		return _data.indexOf(val) > -1;
	}
}


var bob = new ArrStack();
bob.push('ross').show().pop()
bob.show()


// var something = boolean expression ? true : false;
// var pivot = !pivot ? pivot : stack.top();
// pivot = pivot || stack.top();
//

function pivot(stack, pivot) {
    if (stack.isEmpty()) {
        console.log('stack is empty');
        return stack;
    }
    pivot = pivot || stack.top();
    var helperStack = new Stack()
}

function pVal(str){
    var open = 0
    var close = 0
    var storage = []
    for (var idx = 0; idx < str.length; idx++)
        if (str[0] == ')') { //Fast-fail check
            return false;
        }

        if (str[idx] == '(') {
            open++;
            storage.push(str[idx]);
        }
        else if (str[idx] == ')') {
            close++;
            storage.push(str[idx]);

        }


    }
}

var ex1 = ')()()' //Starts with closed parens, should eval FALSE
var ex2 = '()' //Should eval TRUE, simple
var ex3 = '()()()' // Should eval TRUE, complex

pVal('ex1')

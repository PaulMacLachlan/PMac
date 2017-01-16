function pVal(str){
    var open = 0
    var close = 0
    var storage = []
    for (var idx = 0; idx < str.length; idx++){
        if (str[0] == ')') { //Fast-fail check
            console.log('Parens Invalid');
            return false;
        }

        if (str[idx] == '(') { //If str[idx] is an OPEN PARENS
            open++;
            storage.push(str[idx]);
        }

        else if (str[idx] == ')') { //If str[idx] is a CLOSED PARENS
            close++;
            storage.push(str[idx]);
        }
    }
    return (open === close); //Evals if entire storage array has eqivalent # of parens
}

// var ex1 = ')()()' //Starts with closed parens, should eval FALSE
// var ex2 = '()' //Should eval TRUE, simple
// var ex3 = '()()()' // Should eval TRUE, complex

pVal(')()')

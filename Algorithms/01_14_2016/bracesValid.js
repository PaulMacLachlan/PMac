function pVal(str){
    var open = 0, close = 0, storage = [], len = str.length
    // var valid ['(',')','{','}','[',']'], valIdx = 0
    for (var idx = 0; idx < len; idx++){
        //Fast-fail case checks first:
        if (str[0] == ')') {
            console.log('Invalid: First parens cannot be ")"!'); //define error codes
            return false;
        }

        if (len % 2 != 0) {
            console.log('Invalid: Number of parens cannot be uneven!');
            return false;
        }

        if (str[len - 1] == '(') {
            console.log('Invalid: Final parens cannot be "("!');
            return false;
        }

        // if (str.charAt(str[idx]) != '(' ||
        //     str.charAt(str[idx]) != ')' ||
        //     str.charAt(str[idx]) != '{' ||
        //     str.charAt(str[idx]) != '}' ||
        //     str.charAt(str[idx]) != '[' ||
        //     str.charAt(str[idx]) != ']') {
        //     console.log('Invalid characters!');
        //         return false;
        // }

        //if passes all initial checks:

        if (str[idx] == '(') { //If str[idx] is an OPEN PARENS
            open++;
            storage.push(str[idx]);
        }

        else if (str[idx] == ')') { //If str[idx] is a CLOSED PARENS
            close++;
            storage.push(str[idx]);
        }

    }

    /* console.log('SORTED:' + */storage.sort();
    console.log('Open Parens: ' + open + '\n' + 'Closed Parens: ' + close)
    if (open === close) {
        console.log("Parens Valid!");
    }; //Evals if entire storage array has eqivalent # of parens
}
    //Test Cases:
var ex1 = ')()()' //Starts with closed parens, should eval FALSE
var ex2 = '()' //Should eval TRUE, simple
var ex3 = '()()(()))()(()' // Should eval TRUE, complex
var ex4 = '()))))((()()))))(((()))((((((()())' // Should eval TRUE, very complex
var ex5 = '()))))((()()))))(((()))((((((()(' // Should eval FALSE, very complex

pVal(ex5)

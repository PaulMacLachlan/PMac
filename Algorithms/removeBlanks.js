function removeBlanks(str){
    var len = str.length - 1;
    var newStr = "";
    for (var i = 0; i <= len; i++){
        if (str[i] != ' ' && str[i] != '\t'){
            newStr = newStr + str[i];
        }
    }
    return newStr;
}
console.log(removeBlanks("BO    B"));

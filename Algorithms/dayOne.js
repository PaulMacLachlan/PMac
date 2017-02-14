function reverseString (str) {
  var temp;
  var front = 0;
  str[front]
  var back = str.length - 1
  console.log(str[back]);
    str[1] = "f";
      console.log(str);
  console.log("a" + "b" + "c");
}
reverseString ("abc");


function reverseString2(str) {
  var newString = "";
  for (var i = str.length - 1; i >= 0; i--) {
    newString += str[i]
  }
  return newString;
}
console.log(typeof reverseString2("abcd"));

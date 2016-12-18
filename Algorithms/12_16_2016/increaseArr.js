var arr = [];         // create empty array
for (var val = 3; val <= 99999; val += 3) // val will be 3,6,...99999
{
  arr.push(val);      // add each val to arr
}
console.log(arr);     // [3,6,9,12,..., 99999]

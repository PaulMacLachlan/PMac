//print the largest element in a given array.

function findAndPrintMax(arr){

for (var i = 0; i < arr.length; i++) {
    var max = arr[0]
    while (arr[i] > max){
        max = arr[i];
        console.log("Max is now " + max);
        }
    }
}

findAndPrintMax([20,40,70,5,100,101,31,5])

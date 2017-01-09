//print the largest element in a given array.

function findAndPrintMax(arr){

var max = arr[0]
for (var idx = 0; idx < arr.length; idx++) {
    if (arr[idx] > max){
        max = arr[idx];
        }
    }
    console.log("Max is now " + max);
}

findAndPrintMax([20,40,70,5,50,101,31,5,401,301,2000,200,6])

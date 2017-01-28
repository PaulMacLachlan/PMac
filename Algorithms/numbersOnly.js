// Make a function that copies an array, ONLY accepting the items that are numbers.
//
// IT SHOULD RETURN A NEW ARRAY
//
// ex:
//
// var newArray = numbersOnly([1, "apple", -3, "orange", 0.5]);
// // newArray is [1, -3, 0.5]
// HINT
//
// Use typeof to determine type (ex: typeof 24 === "number" would be true)


arr1 = ["fish",2,"Bats",17,"Hooray",21,23]
arr2 = []
for (i = 0; i < arr1.length; i++) {
    if (typeof arr1[i] === "number") {
        arr2.push(arr1[i]);
    }
    console.log(arr2);
}


// arr = ["fish",2,"bats",17,"army","hooray"]
//
// for (i = 0; i < arr.length ; i++) {
//     if (typeof arr[i] != "number") {
//         arr.pop(arr[i]);
//         i++
//     }
//     console.log("IM HERE");
//     console.log(arr);
// }

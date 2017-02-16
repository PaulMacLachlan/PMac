// console.clear();

function flat2(arr, newArr) {
    if (newArr === undefined) {
        newArr = []
    }
    for (var i = 0; i < arr.length; i++) {
        var el = arr[i]
        if (Array.isArray(el)) {
            flat2(el, newArr);
        }
        else {
            newArr.push(el);
        }
    }
    return newArr;
}
arr = [[4, [3], 5], [5, 9], 10]
console.log(flat2(arr));

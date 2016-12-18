arr = [ "James", "Jill", "Jane", "Jack" ]
function fancyArr(){
    for (var i = 0; i <= arr.length - 1 ; i++) {
        console.log(i + " -> " + arr[i])
    }
}

fancyArr()


//Let's make it look fancy! Write a function that will make it print like:
/*
0 -> James
1 -> Jill
2 -> Jane
3 -> Jack
*/

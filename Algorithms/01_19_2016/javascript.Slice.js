function jsSlice(str, start, end) { //is this required to list the string in accepted params?
    var l = str.length, slices = "" //declare necessary variables
    for (var s = start; s < end; s++) { //shile start index is less than end index, defines the "range"
        if (start < 0) { //how best to deal with negative ints? if were looping around to the back of the string, take the length and subtract the start argument.
            start = l + start;
        }

        if (end < 0) {
            end = l + end;
        }

        for (var i = start; i < l; i++) {
            slices += str[i]
            console.log(slices);
        }
    }
}

jsSlice('Hey there I like them strings', 4, 9) //slicing really cool due to being in the loop, but wrong lol

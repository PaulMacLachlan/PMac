//Let's take a really interesting look at recursion...
//Below is a traditional while loop...
/*
var i = 0;
while (i < 10) {
    console.log(i);
    i++;
}
console.log("Done!")
*/
//Now, we can call a function from within a function like this...
function one() {
    two();
}
function two() {
    console.log("This came from TWO, not one!!!");
}
//one();
//Now let's see if we can pass a count around!!
function three(i) {
    four(i);
}
function four(i) {
    console.log(i, "is being printed from four!!!");
}
//three();
//Now, let's extend the idea...
function five(i) {

    if (i < 10) {
        console.log(i);
        i++;
        six(i);
    }
    else {
        console.log("Done!");
        return; //As we know, return stops the function entirely.
    }
}
function six(i) {
    if (i < 10) {
        console.log(i);
        i++;
        five(i);
    }
    else {
        console.log("Done!");
        return; //As we know, return stops the function entirely.
    }
}
//six(0);
//At this point, we have successfully duplicated our while loop....using if/elses and function calls.
//Now, as I'm sure you've noticed...five() and six() are essentially duplicates.  The only difference is that they call eachother.
//It is possible to call a function, inside of its own declaration (calling itself).
//Putting these ideas together...
function seven(i) {
    if (i < 10) {
        console.log(i);
        i++;
        seven(i);
    }
    else {
        console.log("Done!");
        return;
    }

}
//seven(0);
//Now, let's make some minor changes to make it a little more logical.
function eight(i) {

    if (i < 10) {
        console.log(i);
        // i++; Is this really necessary, why not increment it when we pass it, like so...
        eight(i+1);
    }
    else {
        console.log("Done!");
        //return; Is this really necessary?  If we just stop calling ourselves, won't the invocations stop?
    }
}
//eight(0);
//Oh, but now! What if we wanted the value of i when it was done?  What do we do then...This gets a bit trickier!
/* Let's visualize this with the above function ^ eight.
1. Eight checks i < 10.
2. If true, calls eight again, with i = i + 1.
3. If not true, console logs "Done!"
Now, let's see here, to return i, we'de probably want to alter this to do something similar to this..
1. Eight checks i < 10.
2. If true, calls eight again, with i = i + 1.
3. If not true, console logs "Done!" and returns i.
Cool, but, if we do this...then it substitutes to only the last call (since we know that returning ONLY RETURNS TO THE LAST THING THAT CALLED IT)...That means, we need to find a way to have it return all the way back up!  So, how do we substitute it all the way back up through however many calls we make...Well, we just return the continuing call-chain like so!
1. Eight checks i < 10.
2. If true, RETURNS THE NEW call to eight again, with i = i + 1.
3. If not true, console logs "Done!" and returns i.
*/
function nine(i) {
    if (i < 10) {
        console.log(i);
        return nine(i+1); //IMPORTANT!!! (Step 2)
    }
    else {
        console.log("Done!");
        return i; //VERY important!!!! (Step 3)
    }

}
//console.log(nine(0));
//Below, is a set of functions demonstrating what I mean by "bubbling up" the return.
function ex1(i) {

    var result = ex2(i + 20);

    //console.log(result); You can use this instead of the console log outside of the function if you want.
    return result;
}
function ex2(i) {
    ex3(i + 20); //But there's no return here....So it can't go to ex1 and instead gets deleted when ex2 finishes.  Instead, if we return this...

    // Replace the above ^ with return ex3(i + 20);
}
function ex3(i) {

    return i + 20; //This (60)...Gets substituted to line 151...
}
console.log(ex1(0))

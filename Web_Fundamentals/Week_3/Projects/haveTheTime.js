var HOUR = 8;
var MINUTE = 50;
var PERIOD = "AM";

//our result should:
console.log("It's almost 9 in the morning");

And when changed to...

var HOUR = 7;
var MINUTE = 15;
var PERIOD = "PM";
console.log("It's just after 7 in the evening");


// Challenge:
// If minutes less than 30, "just after" the hour, more than 30, "almost" the next hour
// AM / PM, "in the morning", "in the evening",
// HINT
//
// You can add as many items into console.log as you need (They will be separated with spaces)
//
// Example:
//
// var person = "Jack";
// var me = "Jill";
// console.log("Hello", person, "I am", me, ".");
// // Hello Jack I am Jill.
// Bonus (Only If You Have Time):
// Add functionality for "quarter after", "half past", "5 after" ...
// Distinguish between "in the afternoon", "at night", "noon", "midnight" ...

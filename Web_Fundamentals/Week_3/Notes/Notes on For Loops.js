Notes on For Loops:

//   A            B        D
for (var num = 1; num < 6; num = num + 1)
{
  console.log("I'm counting! The number is ", num); // C
}
console.log("We are done. Goodbye world!");         // E

// The above will execute in this sequence: A - B-C-D - B-C-D - B-C-D - B-C-D - B-C-D - B - E.





var num = 1;                          // A
while (num < 6)                       // B
{
  console.log("I'm counting! The number is " + num); // C
  num = num + 1;                      // D
}
console.log("We are done. Goodbye world!");      // E

// The above will ALSO execute in this sequence: A - B-C-D - B-C-D - B-C-D - B-C-D - B-C-D - B - E.








for (INITIALIZATION; TEST; INCREMENT/DECREMENT) 
{
  // BODY of the loop – this runs repeatedly while TEST is true
}
// INIT. [TEST?-BODY-INCREMENT] (repeatedly while TEST is true). Exit.
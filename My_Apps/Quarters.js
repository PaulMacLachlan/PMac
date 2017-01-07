
function slots(quarters){
for (var turns = quarters; turns > 0 ; turns--) {
    spin = Math.floor((Math.random() * 100) + 1);
    console.log("You spun " + spin);
    winner = Math.floor((Math.random() * 100) + 1);

        if (spin === winner){
            console.log("YOU WIN!");
            quarters = quarters + spin;
        }
        else {
            console.log("Game Over");
            return 0;
        }
    }
}
slots(10)

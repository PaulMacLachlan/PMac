function whatTime(hour, min, period){
if(period == "AM"){
    period = "morning"
    }

else if (period === "PM" && hour > 1 && hour < 5) {
    period = "afternoon"
    }
else period = "evening"


if (min >= 1 && min < 20 && min != 15){
    console.log("It's just after " + hour + " O'clock" + " in the " + period);
    }

    else if (min === 5){
        console.log("It's five past " + hour + " in the " + period);
    }

    else if (min === 30){
        console.log("It's half past " + hour + " in the " + period);
    }

    else if (min === 15){
        console.log("It's a quarter past " + hour + " in the " + period);
    }

    else if (min > 30 && min < 45){
        console.log("It's " + hour + ":" + min + " in the " + period);
    }

    else if (min > 45 && min < 60){
        console.log("It's almost " + (hour + min) + period);
    }
}

whatTime(10,5,"AM")

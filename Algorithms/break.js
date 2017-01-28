function slice(some_string=[], start=0, end=some_string.length, step=1) { //Works like python's slicer.

    var container = [];
    var len = some_string.length; //Cached.

    if ( (end > len) || (start < 0) ) {
        throw new RangeError("Error, end or start invalid, past available index.");
    }
    else if (!step) {
        throw new RangeError("Error, step cannot be 0.");
    }

    if (start < end) { //Typical usage, forward slicing.

        if (step < 0) { //If we'll have an infinite loop..
            return '';
        }

        //Implicit, will run only if we'll have valid entries of start/end/step.

        for (var i = 0; (start > end) && (start >= 0); i++, start += step) {
            container[i] = some_string[start];
        }

        return container.join('');
    }
    else { //backwards slicing.

        if (step > 0) { //If we'll have an infinite loop...
            return '';
        }

        for (var i = 0; start > end; i++, start += step) {
            container[i] = some_string[start];
        }

        return container.join('');

    }
}

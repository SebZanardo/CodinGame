#!/bin/bash
# To debug: echo "Debug messages..." >&2

closest=0
abs_closest=5527

# n: the number of temperatures to analyse
read -r n
read -r -a myArray
for (( i=0; i<$n; i++ )); do
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t=${myArray[$((i))]}

    # Parameter expansion to replace -
    abs_number=${t#-}

    echo "$t" >&2

    if [ $abs_number -lt $abs_closest ]; then
        closest=$t
        abs_closest=$abs_number
    elif [ $abs_number -eq $abs_closest ]; then
        # If same number but positive overwrite
        if [ $closest -ne $abs_closest ]; then
            closest=$t
            abs_closest=$abs_number
        fi
    fi
done

echo "$closest"

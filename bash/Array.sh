MY_ARRAY=('Jan' 'Feb' 'Mar' 'Apr' 'May' 'Jun' 'Jul' 'Aug')

echo "================"
echo " Array property"
echo "================"
#Any element of an array may be referenced using ${name[subscript]}.
#The {braces} are required to avoid conflicts with the shell’s filename expansion operators.
echo "Array size: ${#MY_ARRAY[*]}"
echo "Length of item zero: ${#MY_ARRAY[0]}"

echo "=============================="
echo " Array expansion: Single word"
echo "=============================="
#If the subscript is '*' and the word is double-quoted
#${name[*]} expands to a single word 
# with the value of each array member 
# separated by the first character of the IFS variable
echo "Single word expansion: ${MY_ARRAY[*]}"
echo "Single word expansion in printf:"
printf "%s\n" "${MY_ARRAY[*]}"
echo "Single word expansion of the indexes in printf:"
printf "%s\n" "${!MY_ARRAY[*]}"
OLDIFS=$IFS
IFS=","
echo "Single word expansion with IFS: ${MY_ARRAY[*]}"
echo "Single word expansion with IFS in printf:"
printf "%s\n" "${MY_ARRAY[*]}"
IFS=$OLDIFS

echo "================================"
echo " Array expansion: Separate word"
echo "================================"
#${name[@]} expands each element of name to a separate word
echo "Separate word expansion: ${MY_ARRAY[@]}"
echo "Separate word expansion in printf:"
printf "%s\n" "${MY_ARRAY[@]}"
echo "Separate word expansion of the indexes in printf:"
printf "%s\n" "${!MY_ARRAY[@]}"

echo "============="
echo " Array Slice"
echo "============="
#${parameter:offset:length} This is referred to as Substring Expansion. 
#It expands to up to length characters of the value of parameter 
# starting at the character specified by offset.
echo "Slice from 1 to 1+2: ${MY_ARRAY[@]:1:2}"
echo "Slice from 1 to end: ${MY_ARRAY[@]:1}"

#Note that a negative offset must be separated from the colon 
# by at least one space to avoid being confused with the ‘:-’ expansion.
echo "Slice from -3 to end: ${MY_ARRAY[@]: -3}"
echo "Slice from -3 with length 2: ${MY_ARRAY[@]: -3: 2}"
echo "Slice from -1 with length 2(overflow case): ${MY_ARRAY[@]: -1: 2}"

echo "===================="
echo " Array Append/Remove"
echo "===================="
MY_ARRAY=("${MY_ARRAY[@]}" 'Sep')
echo "After Append tail: ${MY_ARRAY[*]}"
unset MY_ARRAY[1]
echo "After Remove MY_ARRAY[1]: ${MY_ARRAY[*]}"
unset MY_ARRAY[-1]
echo "After Remove MY_ARRAY[-1]: ${MY_ARRAY[*]}"

echo "================="
echo " Dashes in printf"
echo "================="
#'--' is bash 'positional parameters' builtin
# If no arguments follow this option, 
# then the positional parameters are unset. 
# Otherwise, the positional parameters are set to the arguments
printf -- "-not -name %s\n" "${MY_ARRAY[@]}"
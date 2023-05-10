# SNAS
Losslessly Swap Newline and Space (Linux/Ubuntu CLI Command)

Be sure to swap out "YOURFILE" for the file you want to swap, and "OUTPUTFILE" for the file you want the name to be.

```
sed 's/ /LCF48D/g' < YOURFILE > temp1
sed 's/\n/nLzF2r/g' < temp1 > temp2

sed 's/LCF48D /\n /g' < temp2 > temp3
sed 's/nLzF2r/ /g' < temp3 > swaped_version

sed 's/\n /LCF48D/g' < swaped_version > temp5
sed 's/ /nLzF2r/g' < temp5 > temp6

sed 's/LCF48D/ /g' < temp6 > temp7
sed 's/nLzF2r/\n/g' < temp7 > OUTPUTFILE
```

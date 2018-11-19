var=1
for name in $( ls *.wav );
do
   mv $name nuevo$var.wav;
   var=$(($var+1))
done

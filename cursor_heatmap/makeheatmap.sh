#!/bin/sh

#take the data from the logfile and make a heatmap from it using heatmap.py

#generate a filename with a u in it.
u=$(dirname $1)/$(basename $1 ".log")u.log

#make a u file with samples where the mouse is still removed
cat $1 | uniq > $u

#count the number of samples in each file
c1=$(wc -l $1 | cut -f1 -d' ')
c2=$(wc -l $u | cut -f1 -d' ')

#choose a good alpha value (make this constant if you wish to do comparisons 
#among different images!)
#The alpha should be between 0 and 100.
#A sensible rule would be,
#  if count = 1 alpha should be 100
#  if as count gets larger, alpha should decrease
alpha1=20
alphau=5 # $(( 100 / $c2))

#make the heatmap images
./heatmap.py $1 $alpha1
./heatmap.py $u $alphau

#echo $c1
#echo $c2

echo $(( ($c2*100)/$c1 ))% of time mouse was moving
echo $(( 100-(($c2*100)/$c1) ))% of time mouse was still


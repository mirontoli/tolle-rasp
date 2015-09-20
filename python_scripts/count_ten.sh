#!/bin/bash
#the same as count_ten.py but in bash
#flite is a simple speech synthesator
for i in {1..11}
do
 sudo flite -t $i
 sleep 1
done
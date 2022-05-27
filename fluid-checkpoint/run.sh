#!/bin/bash
set -ex


for name in whole first_half second_half; do
    echo "Running $name"
    rm -rf $name
    hemelb-confcheck $name.xml
    mpirun -np 3 hemelb -in $name.xml -out $name -i 1 -ss 1111
done


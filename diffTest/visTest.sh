#!/bin/bash
# Use for a visual check when difftest can't be used (i.e. incorrect version of Python in use). 
# Good for checking if NaNs aren't produced (e.g. during Reset)

CODEDIR=${HEMELB_SRC:=../../Code}
NPROCS=2

# Ensure code is built
make -j $(( $NPROCS+1 )) -C $CODEDIR

# Remove the results folder so that we have somewhere for the test output to go
rm -r results

# Run the test
./run.sh $CODEDIR

../../Tools/visim/visim results/Images/ ./VisimImages/

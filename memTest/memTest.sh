#!/bin/bash

CODEDIR=${HEMELB_SRC:=../../hemelb/Code}
NPROCS=2

# Ensure code is built
make -j $(( $NPROCS+1 )) -C $CODEDIR/build

# Remove the results folder so that we have somewhere for the test output to go
rm -r memResults

# Run the memory test using Valgrind
MPIWRAP_DEBUG=quiet \
LD_PRELOAD=~/sw/valgrind/mpi/libmpiwrap-amd64-linux.so \
mpirun -np 3 \
valgrind -q --leak-check=yes --track-origins=yes \
$CODEDIR/build/hemelb -in config.xml -out memResults -i 1 -s 1 -ss 1111

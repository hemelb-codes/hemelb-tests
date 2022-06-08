#!/bin/bash
set -ex

MPIRUN=${MPIRUN:-mpirun}
MPIRUN_FLAGS=${MPIRUN_FLAGS:-}
MPIRUN_NUMPROCS_FLAG=${MPIRUN_NUMPROCS_FLAG:--np}
NUMPROCS=${NUMPROCS:-3}

for name in whole first_half second_half; do
    echo "Running $name"
    rm -rf $name
    hemelb-confcheck $name.xml
    $MPIRUN $MPIRUN_FLAGS $MPIRUN_NUMPROCS_FLAG $NUMPROCS hemelb -in $name.xml -out $name -i 1 -ss 1111
done

python compare.py

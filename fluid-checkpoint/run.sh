#!/bin/bash
set -ex

MPIRUN=${MPIRUN:-mpirun}
MPIRUN_FLAGS=${MPIRUN_FLAGS:-}
MPIRUN_NUMPROCS_FLAG=${MPIRUN_NUMPROCS_FLAG:--np}
NUMPROCS=${NUMPROCS:-3}

function run_hemelb {
    in_xml=$1
    out_dir=$2
    rm -rf $out_dir
    hemelb-confcheck $in_xml
    $MPIRUN $MPIRUN_FLAGS $MPIRUN_NUMPROCS_FLAG $NUMPROCS hemelb -in $in_xml -out $out_dir
}

echo "Running whole 200 steps"
run_hemelb whole.xml whole

echo "Running second half"
run_hemelb whole/Checkpoints/100/restart.xml second_half

python compare.py

#!/bin/bash

set -ex

GOLD_NUMPROCS=3
GOLD_STEERING=basic

MPIRUN=${MPIRUN:-mpirun}
MPIRUN_FLAGS=${MPIRUN_FLAGS:-}
MPIRUN_NUMPROCS_FLAG=${MPIRUN_NUMPROCS_FLAG:--np}
NUMPROCS=${NUMPROCS:-${GOLD_NUMPROCS}}

# Which steering library was compiled into the test executable?
HEMELB_STEERING_LIB=${HEMELB_STEERING_LIB:-${GOLD_STEERING}}

# Remove any results folder so that we have somewhere for the test output to go
rm -rf results

# Run the test (hemelb needs to be in your PATH)
$MPIRUN $MPIRUN_FLAGS $MPIRUN_NUMPROCS_FLAG $NUMPROCS hemelb -in config.xml

OFFSET_CHECK=${OFFSET_CHECK:-full}
if [[ ${OFFSET_CHECK} == light ]]; then
    flag="--light-offset-checks"
else
    flag=""
fi

# Use the script to examine any differences between the snapshot files
./NumericalComparison $flag CleanExtracted results/Extracted

exit $?

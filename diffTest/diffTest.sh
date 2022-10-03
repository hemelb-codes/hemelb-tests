#!/bin/bash

set -ex

GOLD_NUMPROCS=2

MPIRUN=${MPIRUN:-mpirun}
MPIRUN_FLAGS=${MPIRUN_FLAGS:-}
MPIRUN_NUMPROCS_FLAG=${MPIRUN_NUMPROCS_FLAG:--np}
NUMPROCS=${NUMPROCS:-${GOLD_NUMPROCS}}

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

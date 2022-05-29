#!/bin/bash

set -e

MPIRUN=${MPIRUN:-mpirun}
MPIRUN_FLAGS=${MPIRUN_FLAGS:-}
MPIRUN_NUMPROCS_FLAG=${MPIRUN_NUMPROCS_FLAG:--np}
NUMPROCS=${NUMPROCS:-3}

# Remove any results folder so that we have somewhere for the test output to go
rm -rf results

# Run the test (hemelb needs to be in your PATH)
$MPIRUN $MPIRUN_FLAGS $MPIRUN_NUMPROCS_FLAG $NUMPROCS hemelb -in config.xml -i 1 -ss 1111

# Use the script to examine any differences between the snapshot files
./NumericalComparison CleanExtracted results/Extracted

# Check the difference between colloid outputs
# diff ColloidOutput.xdr results/ColloidOutput.xdr

exit $?

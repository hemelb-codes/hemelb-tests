#!/bin/bash

set -e

# Remove any results folder so that we have somewhere for the test output to go
rm -rf results

# Run the test (hemelb needs to be in your PATH)
mpirun -np 3 hemelb -in config.xml -i 1 -ss 1111

# Use the script to examine any differences between the snapshot files
./NumericalComparison CleanExtracted results/Extracted

# Check the difference between colloid outputs
# diff ColloidOutput.xdr results/ColloidOutput.xdr

exit $?

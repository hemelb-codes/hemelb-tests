#!/bin/bash

NPROCS=2

# Remove the results folder so that we have somewhere for the test output to go
rm -r results

# Run the test
./run.sh ${HEMELB_INSTALL_DIR:=/usr/local/bin/}

# Use the script to examine any differences between the snapshot files
./NumericalComparison CleanExtracted results/Extracted

# Check the difference between colloid outputs
# diff ColloidOutput.xdr results/ColloidOutput.xdr

exit $?

from pathlib import Path

import numpy as np

from hlb.parsers.extraction import ExtractedProperty

test_dir = Path("")

def get_cp(run_name):
    return ExtractedProperty(test_dir / run_name / "Extracted/checkpoint.xtr")

whole = get_cp("whole")
first = get_cp("first_half")
second = get_cp("second_half")

assert first.times[0] == whole.times[0]
assert second.times[0] == whole.times[0]
assert second.times[1] == whole.times[1]

w1 = whole.GetByTimeStep(100)
f1 = first.GetByTimeStep(100)
s1 = second.GetByTimeStep(100)

assert np.all(w1 == f1) and np.all(w1 == s1)

print("First checkpoint matches")

w2 = whole.GetByTimeStep(200)
s2 = second.GetByTimeStep(200)

assert np.all(w2 == s2)
print("Second checkpoint matches")
    

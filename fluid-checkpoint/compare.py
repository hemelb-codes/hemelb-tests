from pathlib import Path

import numpy as np

from hlb.parsers.extraction import ExtractedProperty

test_dir = Path("")

def get_cp(run_name, time):
    xp = ExtractedProperty(test_dir / run_name / f"Checkpoints/{time}/distributions.xtr")
    assert len(xp.times) == 1
    assert xp.times[0] == time
    return xp

whole1 = get_cp("whole", 100)
whole2 = get_cp("whole", 200)
first1 = get_cp("first_half", 100)
second1 = get_cp("second_half", 100)
second2 = get_cp("second_half", 200)

w1 = whole1.GetByTimeStep(100)
f1 = first1.GetByTimeStep(100)
s1 = second1.GetByTimeStep(100)

assert np.all(w1 == f1) and np.all(w1 == s1)

print("First checkpoint matches")

w2 = whole2.GetByTimeStep(200)
s2 = second2.GetByTimeStep(200)

assert np.all(w2 == s2)
print("Second checkpoint matches")
    

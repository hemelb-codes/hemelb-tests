import argparse
import xml.etree.ElementTree as ET

from hlb.utils.xml_compare import XmlChecker, ScalarQuantityCheck, VectorQuantityCheck


def strip_extra(top):
    assert top.tag == "hemelbsettings"
    top.remove(top.find("monitoring"))
    top.remove(top.find("properties"))
    return top


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("reference")
    p.add_argument("test")
    args = p.parse_args()

    ref = strip_extra(ET.parse(args.reference).getroot())
    checker = XmlChecker(ref)
    special = {
        "hemelbsettings/simulation/voxel_size": ScalarQuantityCheck(),
        "hemelbsettings/simulation/origin": VectorQuantityCheck(),
        "hemelbsettings/simulation/step_length": ScalarQuantityCheck(),
        "hemelbsettings/*/*/position": VectorQuantityCheck(),
        "hemelbsettings/*/*/normal": VectorQuantityCheck(),
        "hemelbsettings/*/*/condition/mean": ScalarQuantityCheck(),
        "hemelbsettings/*/*/condition/amplitude": ScalarQuantityCheck(),
        "hemelbsettings/*/*/condition/phase": ScalarQuantityCheck(),
        # period set to default of 1s by gmytool
        "hemelbsettings/*/*/condition/period": ScalarQuantityCheck(1.0),
    }
    checker.attr_checks = special
    checker.check_path(args.test)

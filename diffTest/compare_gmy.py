import argparse
import numpy as np
from hlb.parsers.geometry.simple import ConfigLoader


def compare_preamble(ref, oth):
    assert ref.Domain.VoxelSize == oth.Domain.VoxelSize
    assert np.all(ref.Domain.Origin == oth.Domain.Origin)

    assert ref.Domain.Version == oth.Domain.Version
    assert ref.Domain.BlockSize == oth.Domain.BlockSize
    assert np.all(ref.Domain.BlockCounts == oth.Domain.BlockCounts)
    print("Preamble OK")


def compare_header(ref, oth):
    assert np.all(ref.Domain.BlockFluidSiteCounts == oth.Domain.BlockFluidSiteCounts)
    print("Header OK")


def compare_body(ref, oth):
    for bIdx in ref.Domain.BlockIndexer.IterNd():
        refb = ref.Domain.GetBlock(bIdx)
        compare_block(refb, oth.Domain.GetBlock(bIdx))
        print(f"{refb} OK")


def compare_block(ref, oth):
    for ijk in ref.GetDomain().BlockSiteIndexer.IterNd():
        compare_site(ref.GetLocalSite(ijk), oth.GetLocalSite(ijk))


ISEC_TOL = 1e-8
NORM_TOL = (1 - 1e-6) ** 2


def compare_site(ref, oth):
    assert ref.Type == oth.Type

    if ref.IsSolid:
        return

    assert np.all(ref.IntersectionType == oth.IntersectionType)
    assert np.all(
        np.abs(ref.IntersectionDistance - oth.IntersectionDistance) < ISEC_TOL
    )
    assert np.all(ref.IOletIndex == oth.IOletIndex)
    assert ref.WallNormalAvailable == oth.WallNormalAvailable
    if ref.WallNormalAvailable:
        assert np.dot(ref.WallNormal, oth.WallNormal) > NORM_TOL


def compare(ref, oth):
    compare_preamble(ref, oth)
    compare_header(ref, oth)
    compare_body(ref, oth)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("reference")
    p.add_argument("other")
    args = p.parse_args()

    ref_ldr = ConfigLoader(args.reference)
    ref_ldr.Load()

    oth_ldr = ConfigLoader(args.other)
    oth_ldr.Load()

    compare(ref_ldr, oth_ldr)

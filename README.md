# rqmesh-backend-quadwild

The optional **QuadWild-BiMDF** remeshing back-end for the [rqmesh](https://github.com/sandner-art/rqmesh) Blender
extension ([rqmesh-blender](https://github.com/sandner-art/rqmesh-blender)), built as checksummed packages for all four
Blender platforms.

This repository is a fork of [cgg-bern/quadwild-bimdf](https://github.com/cgg-bern/quadwild-bimdf), the authors'
QuadWild with Bi-MDF quantization, itself a fork of [nicopietroni/quadwild](https://github.com/nicopietroni/quadwild).
The shared-library build (`lib_quadwild`, `lib_quadpatches`) comes from
[ksami/quadwild-bimdf](https://github.com/ksami/quadwild-bimdf), branch `feature/lib`; its commits are replayed here
with their original authorship. The upstream README is kept as [README.upstream.md](README.upstream.md).

Base used at setup: **cgg**.

- `cgg`: cgg-bern `main` at `e722c7e` (2026-08-03) plus ksami's commits.
- `ksami`: ksami's `feature/lib` at `b2f985b` (2024-10-08), unchanged.

**Licence:** GPL-3.0, like everything upstream. See [LICENSE](LICENSE) and [rqmesh/NOTICE.md](rqmesh/NOTICE.md).

## Branches

| Branch | Contents |
|---|---|
| `rqmesh` (default) | The base above, ksami's shared-library commits, our `qr_flow` change, packaging and CI, and the QRemeshify ctypes wrapper as a submodule pinned at `e5e5679` |
| `main`, … | Upstream as forked, untouched |

## Releases

Pushing a tag `rqmesh-vX.Y.Z` builds and publishes:

- `rqmesh_backend_quadwild_bimdf-{linux-x64,windows-x64,macos-arm64,macos-x64}.zip`: the libraries, the wrapper, `LICENSE`, a `SOURCE` note, and a manifest with SHA-256 checksums;
- `index.json`: the package list for the extension's back-end manager;
- `rqmesh-backend-quadwild-X.Y.Z-src.tar.gz`: the complete corresponding source, with every submodule and our changes. Blossom-V is excluded: it's not built and not free.

The tags are prefixed so they never collide with upstream tags.

**Using a release with the extension**

- **Self-hosted flavour:** set *Back-end index URL* to `https://github.com/sandner-art/rqmesh-backend-quadwild/releases/latest/download/index.json`. Downloads happen only with Blender's Online Access on, and after a confirmation.
- **Blender Extensions flavour:** the platform does not allow downloading functional code. Download the package for your platform and use *Install Back-end from File*.

## Updating upstream

```
git fetch upstream
git switch rqmesh
git rebase --onto <new upstream commit> <old base commit> rqmesh   # replay ksami's and our commits
rqmesh/tools/init_submodules.sh                                    # then run the workflow by hand
```

Then tag a new release.

**Upstream's `Build` workflow** (`.github/workflows/build.yaml`, manual trigger only) is left as forked. Don't use it for releases: it checks out every submodule, including Blossom-V.

**Excluded:** Blossom-V (non-free) and Gurobi (commercial). The build passes `-DSATSUMA_ENABLE_BLOSSOM5=0 -DQUADRETOPOLOGY_WITH_GUROBI=OFF`.

## Credits

- **QuadWild:** N. Pietroni, S. Nuvoli, T. Alderighi, P. Cignoni, M. Tarini. *Reliable Feature-Line Driven Quad-Remeshing*. ACM TOG 40(4), SIGGRAPH 2021.
- **Bi-MDF quantization:** M. Heistermann, J. Warnett, D. Bommes. *Min-Deviation-Flow in Bi-directed Graphs for T-Mesh Quantization*. ACM TOG 42(4), SIGGRAPH 2023.
- **Shared-library build and ctypes wrapper:** ksami (QRemeshify).

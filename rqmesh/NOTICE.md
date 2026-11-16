# Notice of modification (GPL-3.0, section 5a)

The `rqmesh` branch of this repository is a modified version of QuadWild-BiMDF. Base used at setup: **cgg**.

- `cgg`: cgg-bern/quadwild-bimdf `main` at `e722c7e` (2026-08-03), with ksami's shared-library commits from ksami/quadwild-bimdf `feature/lib` (2024-09/10) replayed.
- `ksami`: ksami/quadwild-bimdf `feature/lib` at `b2f985b`.

| Date | Who | What |
|---|---|---|
| 2024-09/10 | ksami | Shared-library build: `lib_quadwild`, `lib_quadpatches`, parameter passing, cross-platform exports. These are ksami's commits with their authorship, cherry-picked with `-x`. |
| 2026-11-16 | the rqmesh authors (github.com/sandner-art) | `libs/quadretopology/quadretopology/qr_flow.cpp`: reads optional per-subside bounds (`RQM_SUBSIDE_BOUNDS`) and dumps subsides (`RQM_DUMP_SUBSIDES`). It is inert unless one of these environment variables is set. |
| 2026-11-16 | the rqmesh authors | Packaging only: CI workflow, `rqmesh/` tools, the QRemeshify wrapper as a submodule, README; the upstream README was renamed to README.upstream.md |

The full list of changes is the git history of the `rqmesh` branch since the base commit.

**Copyright** remains with the original authors of QuadWild, QuadWild-BiMDF, the shared-library build and the
QRemeshify wrapper. Every file keeps its original licence header.

**Third-party submodules** (vcglib, xfield_tracer, satsuma, lemon, nlohmann/json, OpenMesh, CoMISo, Eigen, libigl,
libTimekeeper, cmake-library) carry their own licence files. Each release's source archive includes them.

**Not included and not built:** `libs/blossom5-cmake` (Blossom-V, non-free licence) and Gurobi (commercial).

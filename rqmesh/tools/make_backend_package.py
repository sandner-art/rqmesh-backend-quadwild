# SPDX-License-Identifier: GPL-3.0-or-later
"""Build one RQM back-end package (QuadWild-BiMDF libraries + QRemeshify's ctypes wrapper) for one platform.
The format must match rqm_lab/backends.py (PACKAGE_SCHEMA, rqm_backend.json, per-file SHA-256): the add-on refuses
anything else.
usage: make_backend_package.py --wrapper QRemeshify/QRemeshify/lib --libs DIR --platform linux-x64 --version 1.0.0+rqm1
                               --out rqm_backend_quadwild_bimdf-linux-x64.zip [--license FILE] [--source TEXT]"""
import argparse, hashlib, json, os, shutil, sys, tempfile, zipfile

PACKAGE_SCHEMA = 1
LIBS = {'windows': ('lib_quadwild.dll', 'lib_quadpatches.dll'),
        'macos': ('liblib_quadwild.dylib', 'liblib_quadpatches.dylib'),
        'linux': ('liblib_quadwild.so', 'liblib_quadpatches.so')}


def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''): h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--wrapper', required=True); ap.add_argument('--libs', required=True)
    ap.add_argument('--platform', required=True); ap.add_argument('--version', required=True)
    ap.add_argument('--out', required=True); ap.add_argument('--license'); ap.add_argument('--source', default='')
    a = ap.parse_args()
    os_ = a.platform.split('-')[0]
    if os_ not in LIBS: sys.exit(f'unknown platform {a.platform}')
    stage = tempfile.mkdtemp(prefix='rqm_pkg_'); q = os.path.join(stage, 'qwlib')
    shutil.copytree(a.wrapper, q, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    for name in LIBS[os_]:
        src = os.path.join(a.libs, name)
        if not os.path.isfile(src): sys.exit(f'missing {src}')
        shutil.copy2(src, os.path.join(q, name))
    files = {}
    for dp, dn, fn in os.walk(q):
        for f in sorted(fn):
            p = os.path.join(dp, f); files[os.path.relpath(p, stage).replace(os.sep, '/')] = sha256(p)
    man = dict(schema=PACKAGE_SCHEMA, name='QuadWild-BiMDF', version=a.version, platform=a.platform,
               license='GPL-3.0-or-later', source=a.source, files=dict(sorted(files.items())))
    with zipfile.ZipFile(a.out, 'w', zipfile.ZIP_DEFLATED) as z:
        for rel in man['files']: z.write(os.path.join(stage, rel), 'quadwild_bimdf/' + rel)
        z.writestr('quadwild_bimdf/rqm_backend.json', json.dumps(man, indent=1))
        if a.license: z.write(a.license, 'quadwild_bimdf/LICENSE.txt')
        z.writestr('quadwild_bimdf/SOURCE.txt', a.source + '\n')
    shutil.rmtree(stage)
    print(json.dumps(dict(out=a.out, platform=a.platform, files=len(files), sha256=sha256(a.out))))


if __name__ == '__main__':
    main()

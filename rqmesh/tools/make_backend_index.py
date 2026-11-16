# SPDX-License-Identifier: GPL-3.0-or-later
"""Write the back-end index the self-hosted RQM add-on reads (Preferences > Back-end index URL).
usage: make_backend_index.py --base-url https://github.com/ORG/rqm-backend-quadwild/releases/download/TAG/ --out index.json PKG.zip..."""
import argparse, hashlib, json, os, zipfile


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--base-url', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('packages', nargs='+'); a = ap.parse_args()
    assets, version = [], None
    for p in a.packages:
        with zipfile.ZipFile(p) as z:
            man = json.loads(z.read('quadwild_bimdf/rqm_backend.json'))
        version = version or man['version']
        if man['version'] != version: raise SystemExit(f'mixed versions: {man["version"]} vs {version}')
        h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
        assets.append(dict(platform=man['platform'], url=a.base_url.rstrip('/') + '/' + os.path.basename(p), sha256=h,
                           size=os.path.getsize(p)))
    idx = dict(schema=1, name='QuadWild-BiMDF', version=version, license='GPL-3.0-or-later',
               assets=sorted(assets, key=lambda x: x['platform']))
    json.dump(idx, open(a.out, 'w'), indent=1); print(json.dumps(idx, indent=1))


if __name__ == '__main__':
    main()

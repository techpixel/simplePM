from wheel.cli import unpack
import json, requests, shutil
from xmlrpc import client as xmlrpc
#from vendored.wheel.cli import unpack

import requests
import json
package_name = 'Django'
# Package info url
PYPI_API_URL = 'https://pypi.python.org/pypi/{package_name}/json'
package_details_url = PYPI_API_URL.format(package_name=package_name)
response = requests.get(package_details_url)
data = json.loads(response.content)
if response.status_code == 200:
    dependencies = data['info'].get('requires_dist')
    dependencies2 = data['info'].get('requires')
    dependencies3 = data['info'].get('setup_requires')
    dependencies4 = data['info'].get('test_requires')
    dependencies5 = data['info'].get('install_requires')
    if dependencies2:
        dependencies.extend(dependencies2)
    if dependencies3:
        dependencies.extend(dependencies3)
    if dependencies4:
        dependencies.extend(dependencies4)
    if dependencies5:
        dependencies.extend(dependencies5)
    dependencies = list(set(dependencies))
  
print(dependencies)

while True: pass

pkgName = 'flask'
pypi = xmlrpc.ServerProxy("https://pypi.org/pypi")

release = pypi.package_releases(pkgName)

pkg = pypi.release_urls(pkgName, release[0])[0]

print(pkg)

r = requests.get(pkg['url'], allow_redirects=True)

with open(pkg['filename'], 'wb+') as f:
  f.write(r.content)

if pkg['filename'].endswith('.whl'):
  unpack.unpack(pkg['filename'])
elif pkg['filename'].endswith('.tar.gz'):
  shutil.unpack_archive(pkg['filename'], 'gztar
  
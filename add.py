import os
from vendored.toml import toml
from xmlrpc import client as xmlrpc

pypi = xmlrpc.ServerProxy("https://pypi.org/pypi")

def package_add(pkgName, release=None):
  global pypi

  if not release:
    release = pypi.package_releases(pkgName)[0]

  pkg = pypi.release_urls(pkgName, release)[0]
  dirpath = os.path.join(os.environ['PYTHONPATH'], pkg['filename'])

  pkginfo = {
    pkgName:{
      'filename':pkg['filename'],
      'ver':pypi.package_releases(pkgName)[0],
      'url':pkg['url'],
      'dirpath':dirpath,
      'installed':False
    }
  }

  with open('odinproj.toml', 'a+') as odinproj:
    odinproj.write(toml.dumps(pkginfo))
  
  print(f'{pkgName} added to your Odin Project.')
  print('Install the package with odin install')
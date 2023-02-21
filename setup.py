from setuptools import setup, find_namespace_packages

includes = [
    'Dissertation.ProtoScan',
    'external.*'
]

excludes = [
    'Dissertation.samples',
    'Dissertation.eval',
    'Dissertation.data',
]

foundPackages = find_namespace_packages(include=includes, exclude=excludes)

print(f'Found Packages: \n{foundPackages}')

setup(
    name='F-Dudley Dissertation',
    version='0.1.0',
    description='My Dissertation Project files for My Final Year Project at Birmingham City University',

    packages=foundPackages,
)

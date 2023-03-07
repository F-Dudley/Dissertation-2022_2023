import os
from setuptools import setup, find_namespace_packages

includes = [

]

excludes = [
    'data*',
    'samples*',
]

foundPackages = find_namespace_packages(
    where='Dissertation',
    include=includes,
    exclude=excludes
)
print(f'Found Packages: \n{foundPackages}')

setup(
    name='F-Dudley Dissertation',
    version='0.1.0',
    description='My Dissertation Project files for My Final Year Project at Birmingham City University',

    package_dir={'': 'Dissertation'},
    packages=foundPackages,

    install_requires=[
        'pykinect2',
        'opencv-python',
        'open3d>=0.15.0',
        'tqdm',

        # Point E Packages
        f'point_e @ git+file://{os.getcwd()}//external//Point-E#egg=point_e',
        'pillow',
        'torch==1.13.1',
    ],
)

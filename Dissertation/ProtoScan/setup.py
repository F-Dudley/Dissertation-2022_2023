from setuptools import setup, find_packages

buildIncludes = [
    '*',
]

buildExcludes = [
    'tests',
    'tests.*',
]

setup(
    version='0.1.0',

    name='F-Dudley Dissertation',
    description='My Dissertation Project files for My Final Year Project at Birmingham City University',
    author='Finn Dudley',

    packages=find_packages(
        include=buildIncludes,
        exclude=buildExcludes
    ),

    install_requires=[
        'pykinect2',
        'opencv-python',
        'open3d>=0.15.0',
        'tqdm',

        # Point E Packages
        'torch',
        "Pillow",
        'point_e',
    ],
)

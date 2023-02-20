from setuptools import setup, find_namespace_packages

buildIncludes = [
    'Dissertation.*',
]

buildExcludes = [
    'Dissertation.tests',
    'Dissertation.tests.*',
]

setup(
    version='0.1.0',

    name='F-Dudley Dissertation',
    description='My Dissertation Project files for My Final Year Project at Birmingham City University',
    author='Finn Dudley',

    packages=find_namespace_packages(
        where='Dissertation', include=buildIncludes, exclude=buildExcludes),

    install_requires=[
        'pykinect2',
        'opencv-python',
        'open3d>=0.15.0',
        'tqdm',

        # Point E Packages
        'torch',
        "Pillow",
    ],
)

from setuptools import setup, find_packages

setup(
    name='comp0035-data-prep',
    version='1.0',
    author='Sarah Sanders',
    url='https://github.com/nicholsons/comp0035-data-prep',
    python_requires='>=3.7',
    packages=find_packages(
        include=[
        ]
    ),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
    ],
    package_data={
        'cgd': ['cgd_raw.csv'],
    },
)

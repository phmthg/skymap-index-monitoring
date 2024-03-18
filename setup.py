from setuptools import setup, find_packages

setup(
    name='skymap_index_monitoring',
    version='0.1',
    packages=find_packages(),
    description='A sample Python project',
    author='Sky',
    author_email='thongktqt10@email.com',
    url='https://github.com/phmthg/skymap-index-monitoring',
    packages=find_packages(),
    install_requires=[
        "flask",
        "rasterio",
        "geopandas",
        "rio-tiler>=4,<5"
    ],
)
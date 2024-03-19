from setuptools import setup, find_packages

setup(
    name='skymap_index_monitoring',
    version='0.2',
    description='A sample Python project',
    author='Sky',
    author_email='thongktqt10@email.com',
    url='https://github.com/phmthg/skymap-index-monitoring',
    install_requires=[
        "flask",
        "rasterio",
        "geopandas",
        "rio-tiler>=4,<5"
    ],
)
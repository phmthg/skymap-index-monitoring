from setuptools import setup, find_packages

setup(
    name='skymap_index_monitoring',
    version='0.1.0',
    url='http://git.skymapglobal.vn/monitor-services/docker-service/skymap-index-monitoring.git',
    packages=find_packages(),
    install_requires=[
        # "requests",
        "flask",
        "rasterio",
        "geopandas",
        "rio-tiler>=4,<5",
        ""
    ],
)
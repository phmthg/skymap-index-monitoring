python setup.py sdist
twine upload dist/*
rm -rf dist build skymap_index_monitoring.egg-info
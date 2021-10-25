python appveyor.py
cd ..
py setup.py sdist -d dist/0.8.3/
cd stubs
py setup.py bdist_wheel -d ../dist/stubs sdist -d ../dist/stubs
cd ../dist
twine upload --repository testpypi 0.8.3/pyunity* stubs/pyunity_stubs-0.8.3*
twine upload 0.8.3/pyunity* stubs/pyunity_stubs-0.8.3*

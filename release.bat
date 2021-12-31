python appveyor.py
cd ..
py setup.py sdist -d dist/0.8.4/
cd stubs
py setup.py bdist_wheel -d ../dist/stubs sdist -d ../dist/stubs
cd ../dist
twine upload --repository testpypi 0.8.4/pyunity* stubs/pyunity?stubs*0.8.4*
twine upload 0.8.4/pyunity* stubs/pyunity?stubs*0.8.4*

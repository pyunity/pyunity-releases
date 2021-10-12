python appveyor.py
cd ../stubs
py ../stubs/setup.py bdist_wheel -d ../dist/stubs sdist -d ../dist/stubs
cd ../dist
twine upload --repository testpypi 0.8.2/pyunity* stubs/pyunity_stubs-0.8.2*
twine upload 0.8.2/pyunity* stubs/pyunity_stubs-0.8.2*

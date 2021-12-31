@echo off

python appveyor.py
cd ..
py setup.py sdist -d dist\post-0.4\0.8.4\
cd stubs
py setup.py bdist_wheel -d ..\dist\stubs sdist -d ..\dist\stubs
cd ..\dist
if not "%~1" == "" (
twine upload --repository testpypi post-0.4\0.8.4\pyunity* stubs\pyunity?stubs*0.8.4*
twine upload post-0.4\0.8.4\pyunity* stubs\pyunity?stubs*0.8.4*
)
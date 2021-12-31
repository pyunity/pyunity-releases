New features:
- Rewrote documentation and docstrings
- Reformatted code
- F string integration
- `ImmutableStruct` and `ABCMeta` metaclasses
  - The `ABCMeta` class has more features than the default Python `abc` module.
- Rewrote examples
- Combined many functions common to both Vector2 and Vector3 into a single Vector class.
  - If you want to implement your own Vector classes, subclass from Vector and implement
    the required abstract methods.
- Fixed quaternion and rotation maths
- Input axes and mouse input
- Multiple lights
- Different light types
- Window provider caching and checking
- Gui components
  - This includes buttons, checkboxes, images and text boxes
  - Rect transforms can be very flexible
  - Platform-specific font loading
- Stub package
  - This will work with editors such as VSCode and PyCharm, just install `pyunity-stubs` from pip

Stub package: https://pypi.org/project/pyunity-stubs

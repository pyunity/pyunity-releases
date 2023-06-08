## API
New features:

### Module
- `RenderTarget` component which renders a Camera output to a texture
- `Mathf` module
- Coroutines and async functions
- Advanced component attribute settings
- Prefabs
- STL loading
- Mesh generation
- Customizable scene runner
- Shadow mapping
- Revamped project format
- Version info when running `python -m pyunity -v`
- Linux wheels audited with `auditwheel` on three different archs
- Environment variable documentation

## Internal
New features:

### Module
- Window provider organization

  - New window providers can be added with
    a respective Python package
  - Current window providers: GLFW, SDL2, GLUT (not fully supported), GLContext

- Rotation bugs fixed
- Separate EventLoops for rendering, physics and update
- PyUnity resource management
- Standardized code style and variable name case
- Import reorganization
- `pathlib.Path` usage
- Internal star imports removed
- Splash screen
- Better logging output

### Repository
- GitHub Actions integration
- Migration from unittest to PyTest
- Mypy integration
- Switch to using `pypa/build` instead of running `setup.py`
- Migration to a `pyproject.toml`-based project
- Automatic running of `prepare.py` when installing if needed
- GitHub issue forms
- New badges displayed on README

# Orgranizing larger programs

- Packages are modules that can contain other modules.
- Packages are generally implemented as directories containing a special \_\_init__.py file.
- The \_\_init__.py file is executed when the package is imported.
- Packages can contain sub packages wich themselves are implemented with  \_\_init__.py files in directories.
- The module object of packages have a \_\_path__ attribute.

#### Sys.path
List of directories Python searches for modules in.

#### PYTHONPATH
Environment variable listing paths added to sys.path.
Uses the same format as system PATH environment variable.

#### \_\_all__
list of attribute names imported via ``` from module import *```

#### Executable directories
Directories containing an entry point for Python execution.

Directories containg a ``__main__.py`` file.


#### Recommended Project structure

```
project_name/
    src/
        project_name/
            __init__.py
            more_source_files.py
    setup.py
    requirements.txt
    README.md
```

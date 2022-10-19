# pyOverrideImport

This is an example repo to demonstrate how to override imported functions/classes using another python module.

The file structure used in this example is the following:

```
📦project
 ┣ mymodules
 ┃ ┣ 📂modulea
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜funcs.py
 ┃ ┗ 📂moduleb
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜funcs.py
 ┣ 📜app.py
 ```
 
If we run `app.py`, both modules are imported, but the function `print_ok` is overriden.
 
```bash
$ python3 app.py

modulea imported
moduleb imported
Module B message
```

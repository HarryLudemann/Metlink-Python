## Publishing Package (Only Authorized Users)
### 1. Update Version Number
In both setup.py and metlink/metlink, update the version number to new version.
## 2. Build Package
```
python setup.py sdist bdist_wheel
```
### 3. Upload Package
```
twine upload dist/*
```
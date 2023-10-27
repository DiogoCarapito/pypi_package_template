# pypi_package_template
Python Package template for PyPi

## Cheatsheet

### Build package

```bash
python3 setup.py sdist bdist_wheel
```

### Use twine to upload to PyPI
```bash
twine check dist/*
````
```bash
twine upload dist/*
```

## Useful links

PyPi
- [https://pypi.org/](https://pypi.org/)
- [https://test.pypi.org/](https://test.pypi.org)
- [https://pypi.org/classifiers/](https://pypi.org/classifiers/)

PyPA
- [https://packaging.python.org/en/latest/overview/](https://packaging.python.org/en/latest/overview/)
- [https://packaging.python.org/guides/distributing-packages-using-setuptools/](https://packaging.python.org/guides/distributing-packages-using-setuptools/)

Sample Project
- [https://github.com/pypa/sampleproject](https://github.com/pypa/sampleproject)

Twine
- [https://twine.readthedocs.io/en/stable/](https://twine.readthedocs.io/en/stable/)

Legal
- [https://www.tldrlegal.com/](https://www.tldrlegal.com/)
- [https://choosealicense.com/](https://choosealicense.com/)



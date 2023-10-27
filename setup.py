from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


VERSION = "0.0.1"
DESCRIPTION = "pypi_package_template"
LONG_DESCRIPTION = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="pypi_package_template",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/DiogoCarapito/pypi_package_template",
    author="DiogoCarapito",
    author_email="diogo.carapito@gmail.com",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords="template",
    packages=find_packages(),
    python_requires=">=3.7, <4",
    install_requires=[],
    project_urls={
        "Bug Reports": "https://github.com/DiogoCarapito/pypi_package_template/issues",
        "Source": "https://github.com/DiogoCarapito/pypi_package_template",
    },
)

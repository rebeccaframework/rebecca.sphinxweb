from setuptools import setup, find_packages

requires = [
    "pyramid",
    "sphinx",
    "sqlalchemy",
    "zope.sqlalchemy",
    "pyramid_tm",
]

points = {
    "console_scripts": [
        "rsphinx=rebecca.sphinxweb.scripts:main",
    ],
    "paste.app_factory": [
        "main=rebecca.sphinxweb:main",
    ],
}

setup(
    name="rebecca.sphinxweb",
    namespace_packages=['rebecca'],
    install_requires=requires,
    packages=find_packages(),
    entry_points=points,
)

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='flaskr',
    version='1.0.0',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Click==7.0',
        'Flask==1.1.1',
        'itsdangerous==1.1.0',
        'Jinja2==2.10.1',
        'MarkupSafe==1.1.1',
        'Werkzeug==0.15.4',
    ],
)

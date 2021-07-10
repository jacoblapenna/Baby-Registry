from setuptools import find_packages
from setuptools import setup

setup(
    name="registry_app",
    version="1.0.0",
    url="mindyandjacob.com",
    license="BSD",
    maintainer="Jacob Lapenna",
    maintainer_email="me@jacoblapenna.com",
    description="Baby registry, withoug compromising the purchaser's privacy.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask"]
)

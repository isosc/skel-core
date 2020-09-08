import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skel", 
    version="0.5.0",
    author="Jeremy Logan",
    author_email="lot@ornl.gov",
    description="The core Skel generative mechanisms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isosc/skel-core",
    install_requires=['Cheetah3'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=["scripts/skel"]
    test_suite='nose.collector',
    tests_require=['nose']
)

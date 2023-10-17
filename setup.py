import setuptools

setuptools.setup(
    name="isakk",
    version="0.1.1",
    author="Luca D'Amico",
    author_email="menteora@bancolini.com",
    package_dir={
        "isakk": ".",
    },
    packages=[
        "isakk",
    ],
    description="It Swiss Army Knife Kit",
    url="https://github.com/menteora/isakk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


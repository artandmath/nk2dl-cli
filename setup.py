from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nk2dl-cli",
    version="0.1.0",
    author="Daniel Harkness",
    author_email="danielharkness@icloud.com",
    description="Nuke to Deadline Submitter - Command Line Interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/artandmath/nk2dl-cli",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "nk2dl>=0.1.0,<0.2.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
            "isort>=5.12.0",
            "mypy>=1.5.1",
        ]
    },
    entry_points={
        "console_scripts": [
            "nk2dl=nk2dl_cli.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Graphics :: 3D Rendering",
        "Environment :: Console",
    ],
    python_requires=">=3.10",
)
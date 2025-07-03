from pathlib import Path
from setuptools import setup, find_packages

readme = (Path(__file__).parent / "README.md").read_text()

setup(

    name = "trial-package",
    version = "1.0.0",
    author = "Fady A. Sulaiman",
    author_email = "Sulaiman.a.fady@gmail.com",
    description = "A refresher for using setup.py",
    long_description = readme,
    long_description_content_type= "text/markdown",
    url = "",
    packages = find_packages(), # Automatically finds packages
    # package_dir = {"": "src"}, # Packages are in src/ directory
    classifiers= [
        "programming language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires = ">=3.6",
    install_requires = [
        "requests>=2.25.0",
        "numpy>=1.19.0"
    ],

    entry_points = {
        "console_scripts": [
            "my-tool=mypackage.cli:main",
            "another-tool=mypackage.scripts:run",
        ],
        "gui_scripts": [
            "my-gui=mypackage.gui:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,

)

# Or you can move all the config to a setup.cfg file and just let this file hold ```setup()```
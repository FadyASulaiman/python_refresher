# Core
python setup.py build          # Build the package
python setup.py install        # Install locally
python setup.py develop        # Development install (like pip install -e .)


# Creating distributions
python setup.py sdist          # Create source distribution (.tar.gz)
python setup.py bdist_wheel    # Create wheel distribution (.whl)
python setup.py bdist_wheel --universal  # Universal wheel (py2+py3)


# others
python setup.py check          # Check metadata
python setup.py clean          # Clean build artifacts
python setup.py --help-commands # List all commands
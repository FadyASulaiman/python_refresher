# pip install . vs. pip install -e .
## pip install .
This performs a **standard installation** where pip builds the package and copies the built files to your site-packages directory. The package code is essentially "frozen" at installation time. **If you modify your source code after installation, those changes won't be reflected** in the installed package until you reinstall.

## pip install -e . (editable/development install)
The -e flag creates an **"editable" or "development" installation**. Instead of copying files, pip creates a link between your development directory and site-packages. This means **changes to your source code are immediately reflected in the installed package without reinstallation.** Under the hood, pip creates a .pth file in site-packages that points to your development directory.

When to use each: Use -e . during development when you're actively modifying code. Use regular pip install . for production deployments or when you want a stable, isolated copy of the package.


## pip commands

``` pip install -r requirements.txt ```
``` pip freeze ```

``` pip install -r requirements.txt --no-index ``` fails offline.
--no-index (optionally combined with --find-links to specify local directories)
This prevents pip from accessing PyPI and forces it to use only locally available packages.
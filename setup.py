# -*- coding: utf-8 -*-
"""pyScreenBrightness: python screen brightness controller
"""
from setuptools import setup
import platform

DOCLINES = (__doc__ or '').split("\n")


CLASSIFIERS = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: Implementation :: CPython
Topic :: Software Development
Operating System :: Microsoft :: Windows
Operating System :: Microsoft :: Windows :: 7
Operating System :: Linux
Operating System :: MacOS
"""


metadata = dict(
        name = 'pyScreenBrightness',
        maintainer = "x007007007",
        maintainer_email = "x007007007@126.com",
        description = DOCLINES[0],
        long_description = "\n".join(DOCLINES[2:]),
        url = "https://github.com/x007007007/pyScreenBrightness/",
        author = "Xingci Xu",
        download_url = "https://github.com/x007007007/pyScreenBrightness/",
        license = 'MIT',
        classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
        platforms = ["Windows", "Linux", "Mac OS-X", "Darwin"],
        packages=['pyScreenBrightness'],
        package_dir={'': 'src'},
        version="0.1.0"
    )



if platform.system() == "Windows":
    platform_metadata = dict(
        install_requires = ['win32api', 'wmi'],
    )
elif platform.system() == "Darwin":
    platform_metadata = dict(
        install_requires = ['pyobjc-core', 'PyObjC']
    )
elif platform.system() == "Linux":
    platform_metadata = dict(
        install_requires = []
    )
else:
    raise OSError("don't support {}".format(platform.system()))

current_meta = {}
current_meta.update(metadata)
current_meta.update(platform_metadata)
setup(**current_meta)
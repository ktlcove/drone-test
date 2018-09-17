import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='drone-test',

    version='0.0.1',

    description='get package from github release and deploy to docker server',  # Required

    # long_description=long_description,  # Optional

    # long_description_content_type='text/markdown',  # Optional (see note above)

    # url='http://git.jdb-dev.com/devops/slb.git',  # Optional

    author='ktlcove',  # Optional

    author_email='ktl_cove@126.com',  # Optional

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='drone docker',  # Optional

    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(
        include=('drone_test',)
    ),  # Required

    install_requires=[
        "flask",
        "redis"
    ],  # Optional

    extras_require={
        'test': ['coverage'],
    },

    # data_files=[('my_data', ['data/data_file'])],  # Optional

    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)

from setuptools import setup

__version_info__ = (4, 2, 1)
__version__ = '.'.join([str(v) for v in __version_info__])
setup(
      name = "Unum_test",
      version = __version__,
      description  = "Units in Python",
      long_description = open("README.rst").read(),
      author = "Chris MacLeod, Pierre Denis, Lukasz Laba",
      author_email = "lukaszlaba@gmail.com",
      url = "https://unum.readthedocs.io/",
      tests_require=['nose>=0.11'],
      test_suite="nose.collector",
      license = 'GNU General Public License (GPL)',
      keywords = 'si units, calculations, math, unit system',
      classifiers=  [
                    'Development Status :: 5 - Production/Stable',
                    'Intended Audience :: Science/Research',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: GNU General Public License (GPL)',
                    'Operating System :: POSIX :: Linux',
                    'Operating System :: Microsoft :: Windows',
                    'Programming Language :: Python',
                    'Topic :: Scientific/Engineering',
                    'Topic :: Scientific/Engineering :: Mathematics',
                    'Topic :: Scientific/Engineering :: Physics',
                    'Topic :: Education',
                    ],
      package_dir={'': 'src'},  # tell distutils packages are under src
      packages = ('unum',
                  'unum.units',
                  'unum.units.custom',
                  'unum.units.others',
                  'unum.units.si',
                  'tests',
                 ),
      python_requires='>=2.4, <4',
)

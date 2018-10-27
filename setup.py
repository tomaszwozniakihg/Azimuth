# from Cython.Build import cythonize
from setuptools import setup
import sys

if sys.version_info[0] >= 3:
    requires = ['scipy', 'numpy', 'matplotlib', 'nose', 'scikit-learn', 'pandas', 'biopython']
else:
    requires = ['scipy', 'numpy', 'matplotlib<3.0', 'nose', 'scikit-learn>=0.17.1,<0.18', 'pandas', 'biopython']

setup(name='Azimuth',
      version='2.0',
      author='Nicolo Fusi and Jennifer Listgarten',
      author_email="fusi@microsoft.com, jennl@microsoft.com",
      description=("Machine Learning-Based Predictive Modelling of CRISPR/Cas9 guide efficiency"),
      packages=["azimuth", "azimuth.features", "azimuth.models", "azimuth.tests"],
      package_data={'azimuth': ['saved_models/*.*']},
      install_requires=requires,
      license="BSD",
      # ext_modules=cythonize("ssk_cython.pyx"),
      )

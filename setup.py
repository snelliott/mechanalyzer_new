""" Install Mechanism Analyzer functions
"""

from distutils.core import setup


setup(
    name="mechanalyzer",
    version="0.2.0",
    packages=[
        'mechanalyzer',
        'mechanalyzer.builder',
        'mechanalyzer.calculator',
        'mechanalyzer.parser',
        'mechanalyzer.plotter',
        'mechanalyzer.inf',
        'ratefit',
        'ratefit.calc',
        'ratefit.fit',
        'ratefit.fit.arrhenius',
        'ratefit.fit.chebyshev',
        'ratefit.fit.troe'],
    package_dir={
        'mechanalyzer': 'mechanalyzer',
        'ratefit': 'ratefit'},
    package_data={
        'mechanalyzer': ['tests/data/*.txt',
                         'tests/data/*.dat',
                         'tests/data/*.csv'],
        'ratefit': ['tests/data/*',
                    'fit/arrhenius/dsarrfit.mako',
                    'fit/troe/troefit.mako']
    }
)
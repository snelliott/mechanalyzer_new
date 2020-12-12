"""
Test the rate plotting functionality for comparing two mechanisms
"""


import tempfile
import numpy
import chemkin_io


# Set up the thermo data
NAMES = ['N2', 'Ne']
THM_DCT = {
    'InChI=1S/N2/c1-2':
        {'mech1': [[1.4136091551074, 5.130163864501488, 10.23657268925187],
                   [0.007074035569284, 0.007811401860078307, -0.003554327],
                   [0.049413953363214, 0.054535303462551296, 0.0584043464],
                   [-23.29336752701, -49.40513959804981, -106.65846691742]],
         'mech2': [[1.4136091551074, 5.130163864501488, 10.23657268295187],
                   [0.007074035569284, 0.007811401860078307, -0.002888327],
                   [0.049413953363214, 0.054535303462551296, 0.0584993464],
                   [-23.29336752701, -49.40513959804981, -106.6584069174]]},
    'InChI=1S/Ne':
        {'mech1': [[1.0027929496287, 3.4867982723176656, 8.454808918941974],
                   [0.004968010602075, 0.004968010646602075, 0.00446602075],
                   [0.03754194552367, 0.04098550796320769, 0.0444253589171],
                   [-17.768179745206, -37.49870969089003, -80.403352863367]],
         'mech2': [[1.0027929496287, 3.4867982723176656, 8.454808918919474],
                   [0.004968010602075, 0.004968010646602075, 0.00496602075],
                   [0.03754194552367, 0.04098550796320769, 0.0444290789171],
                   [-17.768179745206, -37.49870969089003, -80.403332136457]]},
}
TEMPS = numpy.array([500.0, 1000.0, 1500.0])

# Set paths to make the plots
PLOT_PATH = tempfile.mkdtemp()
print(PLOT_PATH)


def test__plot_thermo():
    """ test chemkin_io.mechparser.plot.thermo
    """
    name_thm_dct = dict(zip(NAMES, THM_DCT.values()))
    chemkin_io.plotter.thermo.build(name_thm_dct, TEMPS, dir_prefix=PLOT_PATH)


if __name__ == '__main__':
    test__plot_thermo()

import numpy as np
from matplotlib import pyplot as plt
#some basic colors
clearer='#fd94aeff'
darker='#da76a2ff'
kblue='#569bd2ff'
color_current = 'darkorange'
color_current_2 = 'goldenrod'
color_current_3 = 'peru'
color_current_4 = 'sienna'
color_ongoing = 'rebeccapurple'
color_ongoing_2 = 'blueviolet'
color_ongoing_3 = 'mediumpurple'
color_ongoing_4 = 'darkmagenta'
color_ongoing_5 = 'orchid'
color_proposed = 'darkcyan'
color_proposed_2 = 'darkturquoise'
color_proposed_3 = 'cadetblue'
color_proposed_4 = 'cyan'


# data_files.py
#matplotlib default colors
#hc -> (8.54826*10^-19 Sqrt[Omega])/f
prop_cycle = plt.rcParams['axes.prop_cycle']
mplcolors = prop_cycle.by_key()['color']

#Each row gives filename, short name, type (Direct bound/projected bound/projected curve/ indirect bound), color, depth level in plot
detector_data = [
    # Direct bounds. They are plotted as shaded areas, so line width and dash style will be ignored
    #(file, label, category, color, linewidth,linestyle, opacity, depth level, comment, x-shift of label, y-shift of label, angle of label, label color, label size)
    #LC Resonators
    ('Curves/DetectorCurves/DMRadioGUT.txt', 'DMRadio-GUT-res', 'Ongoing', 'Curves', color_ongoing_2, 3, 'dotted', 1,'glyph', None, 1.E-200, 1.E-200, -1.1*np.pi/2.8, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/DMRadioGUTBB.txt', 'DMRadio-GUT', 'Ongoing', 'Curves', color_ongoing_2, 2, 'solid', 1,'glyph', None, 1.50e5, 1.8e-16,- np.pi/2.8, color_ongoing_2, '11pt' ),
     ('Curves/DetectorCurves/DMRadiom3.txt', 'DMRADIO-m3-res', 'Ongoing', 'Curves', color_ongoing_3, 3, 'dotted', 1,'glyph', None, 1.E-200,1.E-200, -1.1*np.pi/2.8, color_ongoing_3, '11pt' ),
    ('Curves/DetectorCurves/DMRadiom3BB.txt', 'DMRadio-m3', 'Ongoing', 'Curves', color_ongoing_3, 2, 'solid', 1,'glyph', None, 2.1E7 , 1.55E-18, - np.pi/2.805, color_ongoing_3, '11pt' ),
    #Magnetic Weber bars
    ('Curves/DetectorCurves/MWB-DMR-broad.csv', 'DMRadio-GUT ', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 1E5,  2e-22, 0., color_proposed, '11pt' ),
    ('Curves/DetectorCurves/MWB-DMR-res.csv', 'Mag. Weber bars ', 'Proposed', 'Curves', color_proposed, 3, 'dotted', 1,'glyph', None, 8E1,  1.7e-1*1.086552572360649e-19, -3.6*np.pi/8, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/auriga_sens.csv', 'Auriga', 'Existing', 'Curves', color_current_3, 2, 'solid', 1,'glyph', None, 6E2, 9E-20, 0., color_current_3, '11pt' ),
    ('Curves/DetectorCurves/minigrail.csv', 'MiniGrail', 'Existing', 'Curves', color_current_2, 2, 'solid', 1,'glyph', None, 2E3, 3E-18, 0., color_current_2, '11pt' ),
    ('Curves/DetectorCurves/MWB-EFR-broad.csv', 'ADMX-EFR', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 1E7, 1.2E-20, 0., color_proposed, '11pt' ),
    #Magnon Detectors
    ('Curves/DetectorCurves/magnon1.txt', 'magnon 2', 'Proposed', 'SingleFreq', color_proposed, 2, 'solid', 1,'glyph', None, 1E20, 1E20, np.pi/2, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/magnon2.txt', 'magnon', 'Proposed', 'SingleFreq', color_proposed, 2, 'solid', 1,'glyph', None, None, None, np.pi/2, color_proposed, '11pt' ),
    #RF cavities
    ('Curves/DetectorCurves/ADMX.txt', 'ADMX', 'Ongoing', 'Curves', color_ongoing, 3, 'dotted', 1,'glyph', None, 1.70*0.65e9, 4E-24, np.pi/2, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/SQMS.txt', 'SQMS', 'Ongoing', 'Curves', color_ongoing, 3, 'dotted', 1,'glyph', None, 2.0e9, 1E-24, np.pi/2, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/HAYSTAC.txt', 'HAYSTAC', 'Ongoing', 'SingleFreq', color_ongoing, 2, 'solid', 1,'glyph', None, None, None, np.pi/2, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/CAPP.txt', 'CAPP', 'Ongoing', 'SingleFreq', color_ongoing, 2, 'solid', 1,'glyph', None, None, None, np.pi/2, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/ORGAN.txt', 'ORGAN', 'Ongoing', 'SingleFreq', color_ongoing, 2, 'solid', 1,'glyph', None, None, None, np.pi/2, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/c1.txt', 'c1', 'Ongoing', 'SingleFreq', color_ongoing, 2, 'solid', 1,'glyph', None, None, None, np.pi/2, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/c2.txt', 'c2', 'Ongoing', 'SingleFreq', color_ongoing, 2, 'solid', 1,'glyph', None, None, None, np.pi/2, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/c3.txt', 'c3', 'Ongoing', 'SingleFreq', color_ongoing, 2, 'solid', 1,'glyph', None, None, None, np.pi/2, color_ongoing, '11pt' ),
    #MAGO
    ('Curves/DetectorCurves/MAGO_broad.csv', 'MAGO', 'Ongoing', 'Curves', color_ongoing, 2, 'solid', 1,'overlay', None, 1096.5983223359426/(2*np.pi), 1.1*9.62915213463117e-18/np.sqrt(2*np.pi), -np.pi/2.8, color_ongoing, '11pt' ),
    #('Curves/DetectorCurves/mago_res_simple.csv', 'MAGO (res)', 'Ongoing', 'Curves', color_ongoing, 3, 'dotted', 1,'glyph', None, 1E-100, 1E-100, -np.pi/2.8, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/MAGO_res.csv', 'MAGO (res)', 'Ongoing', 'Curves', color_ongoing, 3, 'dotted', 1,'glyph', None, 1E-100, 1E-100, -np.pi/2.8, color_ongoing, '11pt' ),
    #HELIOSCOPES
    ('Curves/DetectorCurves/IAXOHET.txt', 'LF IAXO-HET', 'Proposed', 'Curves', color_proposed, 2, 'dashed', 1,'glyph', None, 6E9, 9E-24, -np.pi/3.9, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/IAXOHET_LOW.txt', 'LF IAXO-HET', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 1E-200, 1E-200, 0, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/IAXOHET_HIGH.txt', 'LF IAXO-HET', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 1E-200, 1E-200, 0, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/IAXOSPD.txt', 'IAXO-SPD', 'Proposed', 'Curves', color_proposed, 2, 'dashed', 1,'glyph', None, None, None, -np.pi/4, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/IAXOSPD_LOW.txt', 'LF IAXO-SPD', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 1E-200, 1E-200, 0, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/IAXOSPD_HIGH.txt', 'LF IAXO-SPD', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 1E-200, 1E-200, 0, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/IAXO.txt', 'IAXO', 'Existing', 'Curves', color_current, 2, 'solid', 0.5, 'underlay', None, 2.51189E17,    12E-38, np.pi/2, color_current, '11pt' ),
    ('Curves/DetectorCurves/CAST.txt', 'CAST', 'Existing', 'Curves', color_current, 2, 'solid', 0.5,'underlay', None, 5.5E17,  5E-37, -np.pi/4, color_current, '11pt' ),
    #GW INTERFEROMETERS
    #('Curves/DetectorCurves/ligoO4a_simple.csv', 'LIGO', 'Existing', 'Areas', color_current, 2, 'solid', 0.5, 'underlay', None, 2E1, 1e-17, np.pi/2, 'white', '10pt' ),
    ('Curves/DetectorCurves/ligoO4a.csv', 'LIGO', 'Existing', 'Curves', color_current, 2, 'solid', 0.7, 'underlay', None, 1.8e3, 2.7e-24, 0.9*np.pi/4, color_current, '11pt' ),
    #('Curves/DetectorCurves/LIGOHF.txt', 'LIGO HF', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 7E8,   1E-18, 0.7*np.pi/2.8, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/LIGOHF2.txt', 'LIGO HF', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 2E5,  4E-22, 0.7*np.pi/2.8, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/geo.csv', 'GEO600', 'Existing', 'Curves', color_current_3, 3, 'solid', 1, 'underlay', None, 1E2, 4.5e-22, -1.25*np.pi/4, color_current_3, '11pt' ),
    ('Curves/DetectorCurves/GEOHF.txt', 'GEO HF', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1, 'underlay', None, 2E5,  4E-21, 0.7*np.pi/2.8, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/nemo.csv', 'NEMO', 'Ongoing', 'Curves', color_ongoing, 2, 'solid', 1, 'underlay', None, 6e3, 2E-24, 2.9*np.pi/8, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/QUEST.csv', 'QUEST', 'Current', 'Areas', color_current, 2, 'solid', 0.6, 'underlay', None, None, None, 0, color_current, '11pt' ),
    ('Curves/DetectorCurves/QUEST_design.csv', 'QUEST (design)', 'Proposed', 'Curves', color_ongoing, 2, 'solid', 0.6, 'underlay', None, None, None, 0, color_ongoing, '11pt' ),
    #LIGHT SHINING THROUGH WALL
    ('Curves/DetectorCurves/DALI.txt', 'DALI II', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 8E9, 2.4E-23, -np.pi/7.5, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/DALIPT2.txt', 'DALI PT', 'Ongoing', 'Curves', color_ongoing, 2, 'solid', 1, 'underlay', None, 5E9, 4E-20, -np.pi/3.9, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/DALIPT.txt', 'DALI PT2', 'Ongoing', 'Curves', color_ongoing, 2, 'solid', 1, 'underlay', None, 1.E-200, 1E-100, np.pi/2, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/ALPSII.txt', 'ALPS II', 'Ongoing', 'Curves', color_ongoing, 2, 'solid', 1, 'underlay', None, None, None, -np.pi/4, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/ALPSIIRes.txt', 'ALPS II res', 'Ongoing', 'Curves', color_ongoing, 2, 'dotted', 1, 'underlay', None, None, None, -np.pi/4, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/JURA.txt', 'JURA', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1, 'underlay', None, None, None, -np.pi/4, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/OSQAR.txt', 'OSQAR II', 'Existing', 'Curves', color_current, 2, 'solid', 1, 'underlay', None, None, None, -np.pi/4, color_current, '11pt' ),
    #Madmax
     ('Curves/DetectorCurves/madmax_hybrid_broad_ext.csv', 'Madmax', 'Ongoing', 'Curves', color_ongoing_4, 2, 'solid', 1,'glyph', None, 1e10, 2E-22, -np.pi/4.2, color_ongoing_4, '11pt' ),
     ('Curves/DetectorCurves/madmax_hybrid_res.csv', 'Madmax (res)', 'Ongoing', 'Curves', color_ongoing_4, 3, 'dotted', 1,'glyph', None,  1E-100,1E-100,-np.pi/4.2, color_ongoing_4, '11pt' ),
     #Holometer
     ('Curves/DetectorCurves/HOLOMETER.txt', 'Holometer', 'Existing', 'Curves', color_current, 2, 'solid', 1,'underlay', None, 2E6, 6.E-20, 0, color_current, '11pt' ),
     #Levitated sensors
     ('Curves/DetectorCurves/levitatedSensors_1mdisc.csv', 'Lev. sens. 1m', 'Ongoing', 'Curves', color_ongoing_5, 3, 'dotted', 1,'glyph', None, 1E4, 5E-19, -np.pi/2.81, color_ongoing_5, '11pt' ),
     ('Curves/DetectorCurves/levitatedSensors_100m.csv', 'Lev. sens. 100m', 'Proposed', 'Curves', color_proposed_2, 3, 'dotted', 1,'glyph', None, 6e4, 8e-24, -np.pi/25, color_proposed_2, '11pt' ),
     #Bulk accoustic wave devices
     ('Curves/DetectorCurves/BAW_current.txt', 'BAW 1', 'Existing', 'SingleFreq', color_current, 2, 'solid', 1,'glyph', None, 4.5e6, 2e-20, np.pi/2, color_current, '11pt' ),
     ('Curves/DetectorCurves/BAW_20mK.csv', 'BAW 2', 'Ongoing', 'Curves', color_ongoing_4, 3, [6, 2, 1, 2], 1,'glyph', None, 3e8, 1.e-21,  3.*np.pi/8, color_ongoing_4, '11pt' ),
     #Levitated superconductors
     ('Curves/DetectorCurves/SLedDoG1g.csv', 'Lev. SC 1g', 'Proposed', 'Curves', color_proposed_2, 2, 'solid', 1,'glyph', None, 1E3, 1.6E-16, -np.pi/2.8, color_proposed_2, '11pt' ),
     ('Curves/DetectorCurves/SLedDoG_30kg.csv', 'Lev. SC 30kg', 'Proposed', 'Curves', color_proposed_3, 2, 'solid', 1,'overlay', None,1E2, 1.1E-18, -np.pi/2.8, color_proposed_3, '11pt' )
]


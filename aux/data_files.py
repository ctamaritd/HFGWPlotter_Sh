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
color_current_5 = 'orange'
color_current_6 = 'navajowhite'
color_ongoing = 'rebeccapurple'
color_ongoing_2 = 'blueviolet'
color_ongoing_3 = 'magenta'
color_ongoing_4 = 'darkmagenta'
color_ongoing_5 = 'orchid'
color_proposed = 'darkcyan'
color_proposed_2 = 'darkturquoise'
color_proposed_3 = 'cadetblue'
color_proposed_4 = 'deepskyblue'


# data_files.py
#matplotlib default colors
#hc -> (8.54826*10^-19 Sqrt[Omega])/f
prop_cycle = plt.rcParams['axes.prop_cycle']
mplcolors = prop_cycle.by_key()['color']

#Each row gives filename, short name, type (Direct bound/projected bound/projected curve/ indirect bound), color, depth level in plot
detector_data = [# Direct bounds. They are plotted as shaded areas, so line width and dash style will be ignored
    #(file, label, category, color, linewidth,linestyle, opacity, depth level, comment, x-shift of label, y-shift of label, angle of label, label color, label size)
    #LC Resonators
    ('Curves/DetectorCurves/DMRadioGUT.txt', 'DMRadio-GUT-res', 'Ongoing', 'Curves', color_ongoing_2, 3, 'dotted', 1,'glyph', None, 1.75e5, 6e-19, -1.05*np.pi/2.8, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/DMRadioGUTBB.txt', 'DMRadio-GUT', 'Ongoing', 'Curves', color_ongoing_2, 2, 'solid', 1,'glyph', None, 1.75e5, 1.75e-16,- np.pi/2.8, color_ongoing_2, '11pt' ),
     ('Curves/DetectorCurves/DMRadiom3.txt', 'DMRADIO-m3-res', 'Ongoing', 'Curves', color_ongoing_3, 3, 'dotted', 1,'glyph', None, 2.1E7, 2E-21, -1.05*np.pi/2.8, color_ongoing_3, '11pt' ),
    ('Curves/DetectorCurves/DMRadiom3BB.txt', 'DMRadio-m3', 'Ongoing', 'Curves', color_ongoing_3, 2, 'solid', 1,'glyph', None, 2.1E7 , 1.6E-18, - np.pi/2.805, color_ongoing_3, '11pt' ),
    #Magnetic Weber bars
    ('Curves/DetectorCurves/MWB-DMR-broad.csv', 'Mag. Weber bars', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 8E1,  1.7e-1*1.086552572360649e-19, -3.6*np.pi/8, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/MWB-DMR-res.csv', 'Mag. Weber bars (res)', 'Proposed', 'Curves', color_proposed, 3, 'dotted', 1,'glyph', None, 1E-100, 1E-100, -3.6*np.pi/8, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/auriga_sens.csv', 'Auriga', 'Existing', 'Areas', color_current_6, 2, 'solid', 1,'glyph', None, 7E2, 9E-20, np.pi/2., 'white', '11pt' ),
    ('Curves/DetectorCurves/minigrail.csv', 'MiniGrail', 'Existing', 'Areas', color_current_6, 2, 'solid', 1,'glyph', None, 2.5E3, 9E-20, np.pi/2, 'white', '11pt' ),
    ('Curves/DetectorCurves/MWB-EFR-broad.csv', 'ADMX-EFR', 'Proposed', 'Curves', color_proposed_2, 2, 'solid', 1,'glyph', None, 1E7, 1.2E-20, 0., color_proposed_2, '11pt' ),
    #Magnon Detectors
    ('Curves/DetectorCurves/magnon1.txt', 'magnon 2', 'Proposed', 'SingleFreq', color_proposed, 2, 'solid', 1,'glyph', None, 1E20, 1E20, np.pi/2, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/magnon2.txt', 'magnon', 'Proposed', 'SingleFreq', color_proposed, 2, 'solid', 1,'glyph', None, None, None, np.pi/2, color_proposed, '11pt' ),
    #RF cavities
    ('Curves/DetectorCurves/ADMX.txt', 'ADMX', 'Ongoing', 'Curves', color_ongoing, 3, 'dotted', 1,'glyph', None, 1.70*0.65e9, 4E-24, np.pi/2, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/SQMS.txt', 'SQMS', 'Ongoing', 'Curves', color_ongoing_5, 3, 'dotted', 1,'glyph', None, 2.0e9, 1E-24, np.pi/2, color_ongoing_5, '11pt' ),
    ('Curves/DetectorCurves/HAYSTAC.txt', 'HAYSTAC', 'Ongoing', 'SingleFreq', color_ongoing_4, 2, 'solid', 1,'glyph', None, 9.5e9, 7e-23, np.pi/2, color_ongoing_4, '11pt' ),
    ('Curves/DetectorCurves/CAPP.txt', 'CAPP', 'Ongoing', 'SingleFreq', color_ongoing_4, 2, 'solid', 1,'glyph', None, 3e9, 7e-22, np.pi/2, color_ongoing_4, '11pt' ),
    ('Curves/DetectorCurves/ORGAN.txt', 'ORGAN', 'Ongoing', 'SingleFreq', color_ongoing_4, 2, 'solid', 1,'glyph', None, 2.55e10, 1.1e-20, np.pi/2, color_ongoing_4, '11pt' ),
    ('Curves/DetectorCurves/ORGAN2.txt', 'ORGAN 2', 'Ongoing', 'SingleFreq', color_ongoing_4, 2, 'solid', 1,'glyph', None, 1E-100, 1e-100, np.pi/2, color_ongoing_4, '11pt' ),
    ('Curves/DetectorCurves/c1.txt', 'c1', 'Ongoing', 'SingleFreq', color_ongoing, 2, 'solid', 1,'glyph', None, 1.8e8, 5e-21, np.pi/2, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/c2.txt', 'c2', 'Ongoing', 'SingleFreq', color_ongoing, 2, 'solid', 1,'glyph', None, 1.8e9, 2.e-22, np.pi/2, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/c3.txt', 'c3', 'Ongoing', 'SingleFreq', color_ongoing, 2, 'solid', 1,'glyph', None, 1.8e10, 4e-21, np.pi/2, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/Rades1.txt', 'Rades 1', 'Ongoing', 'Curves', color_ongoing_5, 2, 'dotted', 1,'glyph', None, 3.2E8, 7E-25, np.pi/2, color_ongoing_5, '11pt' ),
    ('Curves/DetectorCurves/Rades2.txt', 'Rades 2', 'Ongoing', 'Curves', color_ongoing_3, 2, 'dotted', 1,'glyph', None, 3.2E9, 7E-24, np.pi/2, color_ongoing_3, '11pt' ),
    #MAGO
    ('Curves/DetectorCurves/MAGO_broad.csv', 'MAGO', 'Ongoing', 'Curves', color_ongoing, 2, 'solid', 1,'glyph', None, 1096.5983223359426/(2*np.pi), 1.1*9.62915213463117e-18/np.sqrt(2*np.pi), -np.pi/2.8, color_ongoing, '11pt' ),
    #('Curves/DetectorCurves/mago_res_simple.csv', 'MAGO (res)', 'Ongoing', 'Curves', color_ongoing, 3, 'dotted', 1,'glyph', None, 1E-100, 1E-100, -np.pi/2.8, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/MAGO_res.csv', 'MAGO (res)', 'Ongoing', 'Curves', color_ongoing, 3, 'dotted', 1,'glyph', None, 1E-100, 1E-100, -np.pi/2.8, color_ongoing, '11pt' ),
    #HELIOSCOPES
    ('Curves/DetectorCurves/IAXOHET.txt', 'LF IAXO-HET', 'Proposed', 'Curves', color_proposed_2, 2, 'dashed', 1,'glyph', None, 9E10, 1.E-25, -np.pi/4.1, color_proposed_2, '11pt' ),
    ('Curves/DetectorCurves/IAXOHET_LOW.txt', 'LF IAXO-HET-LOW', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 1E-200, 1E-200, 0, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/IAXOHET_HIGH.txt', 'LF IAXO-HET-HIGH', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 1E-200, 1E-200, 0, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/IAXOSPD.txt', 'LF IAXO-SPD', 'Proposed', 'Curves', color_proposed_3, 2, 'dashed', 1,'glyph', None, 1.E11, 8E-32, -np.pi/4.1, color_proposed_3, '11pt' ),
    ('Curves/DetectorCurves/IAXOSPD_LOW.txt', 'LF IAXO-SPD-LOW', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 1E-200, 1E-200, 0, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/IAXOSPD_HIGH.txt', 'LF IAXO-SPD-HIGH', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 1E-200, 1E-200, 0, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/IAXO.txt', 'IAXO', 'Ongoing', 'Curves', color_ongoing, 3, 'solid', 1, 'glyph', None, 5.5E17,    1.5E-38, -np.pi/4, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/CAST.txt', 'CAST', 'Existing', 'Areas', color_current, 2, 'solid', 0.5,'underlay', None, 1E18,  4.E-37, np.pi/2, 'white', '11pt' ),
    #GW INTERFEROMETERS
    #('Curves/DetectorCurves/ligoO4a_simple.csv', 'LIGO', 'Existing', 'Areas', color_current, 2, 'solid', 0.5, 'underlay', None, 2E1, 1e-17, np.pi/2, 'white', '10pt' ),
    ('Curves/DetectorCurves/ligoO4a.csv', 'LIGO', 'Existing', 'Areas', color_current, 2, 'solid', 0.5, 'underlay', None, 1.8e3, 2.7e-24, 0.9*np.pi/4, color_current, '11pt' ),
    #('Curves/DetectorCurves/LIGOHF.txt', 'LIGO HF', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 7E8,   1E-18, 0.7*np.pi/2.8, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/LIGOHF2.txt', 'LIGO HF', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 2E5,  4E-22, 0.7*np.pi/2.8, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/geo.csv', 'GEO600', 'Existing', 'Areas', color_current, 3, 'solid', 0.6, 'underlay', None, 1.5E2, 1.5e-21, -1.25*np.pi/4, 'white', '11pt' ),
    ('Curves/DetectorCurves/GEOHF.txt', 'GEO HF', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1, 'underlay', None, 2E5,  4E-21, 0.7*np.pi/2.8, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/nemo.csv', 'NEMO', 'Ongoing', 'Curves', color_ongoing, 2, 'solid', 1, 'underlay', None, 6e3, 2E-24, 2.9*np.pi/8, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/QUEST.csv', 'QUEST', 'Existing', 'Areas', color_current, 2, 'solid', 0.6, 'underlay', None, 1.7E7, 4E-18, 0., 'white', '11pt' ),
    ('Curves/DetectorCurves/QUEST_design.csv', 'QUEST (des.)', 'Proposed', 'Curves', color_ongoing, 2, 'solid', 1, 'underlay', None, 3E7, 5.0E-20, 0., color_ongoing, '11pt' ),
    #LIGHT SHINING THROUGH WALL
    ('Curves/DetectorCurves/DALI.txt', 'DALI II', 'Proposed', 'Curves', color_proposed, 2, 'solid', 1,'glyph', None, 1E9, 8E-23, -np.pi/7.5, color_proposed, '11pt' ),
    ('Curves/DetectorCurves/DALIPT2.txt', 'DALI PT', 'Ongoing', 'Curves', color_ongoing, 2, 'solid', 1, 'underlay', None, 9E9, 1.5E-19, np.pi/2, color_ongoing, '11pt' ),#-np.pi/3.9
    ('Curves/DetectorCurves/DALIPT.txt', 'DALI PT2', 'Ongoing', 'Curves', color_ongoing, 2, 'solid', 1, 'underlay', None, 1.E-200, 1E-100, np.pi/2, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/ALPSII.txt', 'ALPS II', 'Ongoing', 'Curves', color_ongoing, 2, 'solid', 1, 'underlay', None, 3E14, 8E-37, -np.pi/4, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/ALPSIIRes.txt', 'ALPS II res', 'Ongoing', 'SingleFreq', color_ongoing, 2, 'solid', 1, 'underlay', None,  3E14, 8.E-39, -np.pi/4, color_ongoing, '11pt' ),
    ('Curves/DetectorCurves/JURA.txt', 'JURA', 'Proposed', 'Curves', color_proposed_2, 2, 'solid', 1, 'underlay', None, 3E14, 1.5E-37, -np.pi/4, color_proposed_2, '11pt' ),
    ('Curves/DetectorCurves/OSQAR.txt', 'OSQAR II', 'Existing', 'Areas', color_current, 2, 'solid', 0.5, 'underlay', None, 6E14,    3.5E-33, np.pi/2, 'white', '11pt' ),
    #Madmax
     ('Curves/DetectorCurves/madmax_hybrid_broad_ext.csv', 'Madmax', 'Ongoing', 'Curves', color_ongoing_4, 2, 'solid', 1,'glyph', None, 1.e10, 2E-22, -np.pi/4, color_ongoing_4, '11pt' ),
     ('Curves/DetectorCurves/madmax_hybrid_res.csv', 'Madmax (res)', 'Ongoing', 'Curves', color_ongoing_4, 3, 'dotted', 1,'glyph', None,  1E-100,1E-100,-np.pi/4.2, color_ongoing_4, '11pt' ),
     #Holometer
     ('Curves/DetectorCurves/HOLOMETER.txt', 'Holometer', 'Existing', 'Areas', color_current, 2, 'solid', 0.6,'underlay', None, 3E6, 3.E-19, np.pi/2, 'white', '11pt' ),
     #Levitated sensors
     ('Curves/DetectorCurves/levitatedSensors_1mdisc.csv', 'Lev. sens. 1m', 'Ongoing', 'Curves', color_ongoing_5, 3, 'dotted', 1,'glyph', None, 1E4, 5E-19, -np.pi/2.81, color_ongoing_5, '11pt' ),
     ('Curves/DetectorCurves/levitatedSensors_100m.csv', 'Lev. sens. 100m', 'Proposed', 'Curves', color_proposed_2, 3, 'dotted', 1,'glyph', None, 6e4, 8e-24, -np.pi/25, color_proposed_2, '11pt' ),
     #Bulk accoustic wave devices
     ('Curves/DetectorCurves/BAW_current.txt', 'BAW 1', 'Existing', 'SingleFreq', color_current, 2, 'solid', 1,'glyph', None, 1e7, 2e-21, np.pi/2, color_current, '11pt' ),
     ('Curves/DetectorCurves/BAW_20mK.csv', 'BAW 2', 'Ongoing', 'Curves', color_ongoing_4, 3, [6, 2, 1, 2], 1,'glyph', None, 3e8, 1.e-21,  3.*np.pi/8, color_ongoing_4, '11pt' ),
     #Levitated superconductors
     ('Curves/DetectorCurves/SLedDoG1g.csv', 'Lev. SC 1g', 'Proposed', 'Curves', color_proposed_2, 2, 'solid', 1,'glyph', None, 1E3, 1.6E-16, -np.pi/2.8, color_proposed_2, '11pt' ),
     ('Curves/DetectorCurves/SLedDoG_30kg.csv', 'Lev. SC 30kg', 'Proposed', 'Curves', color_proposed_3, 2, 'solid', 1,'overlay', None,1E2, 1.1E-18, -np.pi/2.8, color_proposed_3, '11pt' ),
     #User supplied##
     (' ', 'Your curve', 'Proposed', 'Curves','darkred', 3, 'solid', 1,'glyph', None, 0, 0, 0, 'darkred', '9pt' )
]


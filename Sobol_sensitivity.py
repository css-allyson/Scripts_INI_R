# %%
from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
import numpy as np
# %%
problem = {
    'num_vars':22,
    'names':["ANG_L_ange","ANG_L_anghd","ANG_L_anghe","ANG_L_angv","APP_CeilingHeight","APP_E_Window_SUP_AreaGross","APP_ExteriorWindowArea","BLDG_E_Window","BLDG_N_Window","BLDG_S_Window",
             "BLDG_W_Window","CONST_ThermalConductance_COB","CONST_ThermalConductance_PAR_EXT","CONST_ThermalConductance_PISO_TERREO","CONST_cob_CT","CONST_laje_CT","CONST_par_ext_CT",
             "SAMPLE_openFactor","SAMPLE_roof_abs","SAMPLE_shgc","SAMPLE_uVidro","SAMPLE_wall_abs"],
    'bounds':[[0,60], #ANG_L_ange
              [0,80], #ANG_L_anghd
              [0,80], #ANG_L_anghe
              [0,55], #ANG_L_angv
              [2.5,3.2], #APP_CeilingHeight
              [0,12], #APP_E_Window_SUP_AreaGross
              [0,12], #APP_ExteriorWindowArea
              [0,100], #BLDG_E_Window
              [0,100], #BLDG_N_Window
              [0,100], #BLDG_S_Window
              [0,100], #BLDG_W_Window
              [0.49,19.44], #CONST_ThermalConductance_COB
              [0.23,17.5], #CONST_ThermalConductance_PAR_EXT
              [0.82,35], #CONST_ThermalConductance_PISO_TERREO
              [25,550], #CONST_cob_CT
              [25,440], #CONST_laje_CT
              [20,440], #CONST_par_ext_CT
              [0.05,1], #"SAMPLE_openFactor
              [0.2,0.9], #SAMPLE_roof_abs
              [0.2,0.9], #SAMPLE_shgc
              [2.5,6], #SAMPLE_uVidro
              [0.2,0.9] #SAMPLE_wall_abs

    ]
}
# %%
param_values = saltelli.sample(problem, 3000)
# %%
np.savetxt("param_values.csv", param_values)

# %%

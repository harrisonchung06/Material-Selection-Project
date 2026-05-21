import utils
import math

# Steel
carbon_1023_sheet_ss = utils.Material(
    rho=7858.000032,
    E=204999998381.83875,
    nu=0.29,
    Sy=282685049.019888)

stainless_201_annealed_ss = utils.Material(
    rho=7859.999900,
    E=207000000000.0,
    nu=0.27,
    Sy=292000000.0)

aisi_1010_hot_rolled_bar = utils.Material(
    rho=7870.0,
    E=200000000000.0,
    nu=0.29,
    Sy=180000000.0)

aisi_1015_cold_drawn_ss = utils.Material(
    rho=7870.0,
    E=205000000000.0,
    nu=0.29,
    Sy=325000000.0)

aisi_1035_steel_ss = utils.Material(
    rho=7849.999987,
    E=204999998381.83875,
    nu=0.29,
    Sy=282685049.019888)

aisi_1045_cold_drawn = utils.Material(
    rho=7850.0,
    E=205000000000.0,
    nu=0.29,
    Sy=530000000.0)

aisi_304 = utils.Material(
    rho=8000.0,
    E=190000000000.0,
    nu=0.29,
    Sy=206807000.0)

aisi_316_stainless_sheet_ss = utils.Material(
    rho=8000.000133,
    E=192999997366.6726,
    nu=0.27,
    Sy=172368932.3292)

aisi_347_annealed_stainless_ss = utils.Material(
    rho=8000.000133,
    E=195000000983.2456,
    nu=0.27,
    Sy=275000000.856262)

aisi_4130_annealed_865c = utils.Material(
    rho=7850.0,
    E=205000000000.0,
    nu=0.285,
    Sy=460000000.0)

aisi_4340_normalized = utils.Material(
    rho=7850.0,
    E=205000000000.0,
    nu=0.32,
    Sy=710000000.0)

alloy_steel = utils.Material(
    rho=7700.0,
    E=210000000000.0,
    nu=0.28,
    Sy=620422000.0)

cast_alloy_steel = utils.Material(
    rho=7300.0,
    E=190000000000.0,
    nu=0.26,
    Sy=241275200.0)

cast_carbon_steel = utils.Material(
    rho=7800.0,
    E=190000000000.0,
    nu=0.26,
    Sy=248168000.0)

cast_stainless_steel = utils.Material(
    rho=7800.0,
    E=200000000000.0,
    nu=0.28,
    Sy=172339000.0)

stainless_steel_ferritic = utils.Material(
    rho=7800.0,
    E=200000000000.0,
    nu=0.28,
    Sy=172339000.0)

wrought_stainless_steel = utils.Material(
    rho=8000.0,
    E=200000000000.0,
    nu=0.26,
    Sy=206807000.0)

# Iron
ductile_iron = utils.Material(
    rho=7100.0,
    E=120000000000.0,
    nu=0.31,
    Sy=551485000.0)

malleable_cast_iron = utils.Material(
    rho=7300.0,
    E=190000000000.0,
    nu=0.27,
    Sy=275742000.0)

# Aluminium Alloys (visible portion only)
aluminum_1060_alloy = utils.Material(
    rho=2700.0,
    E=69000000000.0,
    nu=0.33,
    Sy=27574200.0)

aluminum_1060_h12 = utils.Material(
    rho=2700.0,
    E=69000000000.0,
    nu=0.33,
    Sy=61e6)

MATS = [
    carbon_1023_sheet_ss,
    stainless_201_annealed_ss,
    aisi_1010_hot_rolled_bar,
    aisi_1015_cold_drawn_ss,
    aisi_1035_steel_ss,
    aisi_1045_cold_drawn,
    aisi_304,
    aisi_316_stainless_sheet_ss,
    aisi_347_annealed_stainless_ss,
    aisi_4130_annealed_865c,
    aisi_4340_normalized,
    alloy_steel,
    cast_alloy_steel,
    cast_carbon_steel,
    cast_stainless_steel,
    stainless_steel_ferritic,
    wrought_stainless_steel,
    ductile_iron,
    malleable_cast_iron,
    aluminum_1060_alloy,
    aluminum_1060_h12,
]
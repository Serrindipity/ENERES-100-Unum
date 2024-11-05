"""
Note that this file will be overwritten when you upgrade to a new version
of Unum, so if you have custom units they should be in their own file.
"""

from unum import Unum
unit = Unum.unit

# << uncomment this import if you want to derive your units from SI >>
from unum.units.si import *
from unum.units.others import *

# << define your units hereafter, e.g.
#    M  = unit(  'm' , 0          , 'meter'     )
#    KM = unit( 'km' , 1000. * M  , 'kilometer' ) >>


si_prefixes = {
    "yotta": ("Y", 10**24),
    "zetta": ("Z", 10**21),
    "exa": ("E", 10**18),
    "peta": ("P", 10**15),
    "tera": ("T", 10**12),
    "giga": ("G", 10**9),
    "mega": ("M", 10**6),
    "kilo": ("k", 10**3),
    "hecto": ("h", 10**2),
    "deca": ("da", 10**1),
    "deci": ("d", 10**-1),
    "centi": ("c", 10**-2),
    "milli": ("m", 10**-3),
    "micro": ("μ", 10**-6),
    "nano": ("n", 10**-9),
    "pico": ("p", 10**-12),
    "femto": ("f", 10**-15),
    "atto": ("a", 10**-18),
    "zepto": ("z", 10**-21),
    "yocto": ("y", 10**-24),
}

def generate_units(base_unit_name: str, base_unit_symbol: str, prefixes: dict[str : tuple], value = 1) -> None:
    base_unit = unit(base_unit_symbol, 1, base_unit_name)  # Create the base unit
    
    units = {}
    
    for prefix, (symbol_prefix, multiplier) in prefixes.items():
        # Create unit symbol and description by combining prefix with the base unit
        unit_symbol = symbol_prefix + base_unit_symbol
        unit_description = prefix + base_unit_name
        
        # Generate unit using the unit() function
        u = unit(unit_symbol, multiplier * base_unit, unit_description)
        units[unit_symbol] = u
        unit[unit_description] = u
        
    
    # Include the base unit itself
    units[base_unit_symbol] = base_unit
    
    import sys
    module = sys.modules[__name__]
    for name, value in units.items():
        setattr(module, name, value)

generate_units('volt', 'V', si_prefixes, W / A)


year          = Y = y        = unit( 'y'        , 365 * D            , 'year'                       )
Wh         = WH      = unit( 'Wh'    , J * 3600       , 'watt hour'      )
bbl = unit('bbl', kg * 136, 'barrel')
LB = lb = unit('pound', kg * 0.454, 'US-pound')
TON = tn = ton = USTON = unit('ton', lb * 1000, 'US-short-ton')
Btu = btu  = BTU = unit('Btu', J * 1055, 'british-thermal-unit')
MBtu = mbtu = MBTU = unit('MBtu', Btu * 10**6, 'mega-btu')
foot = ft = unit('ft', m * 0.3048, 'foot')
acre = unit('acre', 4048 * ft**2, 'acre')
cent = CENT = unit('¢', 0, 'cent')
dollar = DOLLAR = unit('$', 100 * cent, 'dollar')


# SI prefixes for watts
YW = unit("YW", 10**24 * W, "yottawatt")    # Yottawatt
ZW = unit("ZW", 10**21 * W, "zettawatt")    # Zettawatt
EW = unit("EW", 10**18 * W, "exawatt")      # Exawatt
PW = unit("PW", 10**15 * W, "petawatt")     # Petawatt
TW = unit("TW", 10**12 * W, "terawatt")     # Terawatt
GW = unit("GW", 10**9 * W, "gigawatt")      # Gigawatt
MW = unit("MW", 10**6 * W, "megawatt")      # Megawatt
kW = unit("kW", 10**3 * W, "kilowatt")      # Kilowatt
hW = unit("hW", 10**2 * W, "hectowatt")     # Hectowatt
daW = unit("daW", 10**1 * W, "decawatt")    # Decawatt
dW = unit("dW", 10**-1 * W, "deciwatt")     # Deciwatt
cW = unit("cW", 10**-2 * W, "centiwatt")    # Centiwatt
mW = unit("mW", 10**-3 * W, "milliwatt")    # Milliwatt
μW = unit("μW", 10**-6 * W, "microwatt")    # Microwatt
nW = unit("nW", 10**-9 * W, "nanowatt")     # Nanowatt
pW = unit("pW", 10**-12 * W, "picowatt")    # Picowatt
fW = unit("fW", 10**-15 * W, "femtowatt")   # Femtowatt
aW = unit("aW", 10**-18 * W, "attowatt")    # Attowatt
zW = unit("zW", 10**-21 * W, "zeptowatt")   # Zeptowatt
yW = unit("yW", 10**-24 * W, "yoctowatt")   # Yoctowatt

# SI prefixes for joules
YJ = unit("YJ", 10**24 * J, "yottajoule")    # Yottajoule
ZJ = unit("ZJ", 10**21 * J, "zettajoule")    # Zettajoule
EJ = unit("EJ", 10**18 * J, "exajoule")      # Exajoule
PJ = unit("PJ", 10**15 * J, "petajoule")     # Petajoule
TJ = unit("TJ", 10**12 * J, "terajoule")     # Terajoule
GJ = unit("GJ", 10**9 * J, "gigajoule")      # Gigajoule
MJ = unit("MJ", 10**6 * J, "megajoule")      # Megajoule
kJ = unit("kJ", 10**3 * J, "kilojoule")      # Kilojoule
hJ = unit("hJ", 10**2 * J, "hectojoule")     # Hectojoule
daJ = unit("daJ", 10**1 * J, "decajoule")    # Decajoule
dJ = unit("dJ", 10**-1 * J, "decijoule")     # Decijoule
cJ = unit("cJ", 10**-2 * J, "centijoule")    # Centijoule
mJ = unit("mJ", 10**-3 * J, "millijoule")    # Millijoule
μJ = unit("μJ", 10**-6 * J, "microjoule")    # Microjoule
nJ = unit("nJ", 10**-9 * J, "nanojoule")     # Nanojoule
pJ = unit("pJ", 10**-12 * J, "picojoule")    # Picojoule
fJ = unit("fJ", 10**-15 * J, "femtojoule")   # Femtojoule
aJ = unit("aJ", 10**-18 * J, "attojoule")    # Attojoule
zJ = unit("zJ", 10**-21 * J, "zeptojoule")   # Zeptojoule
yJ = unit("yJ", 10**-24 * J, "yoctojoule")   # Yoctojoule

# SI prefixes for watt-hours (Wh)
YWh = unit("YWh", 10**24 * Wh, "yottawatt-hour")    # Yottawatt-hour
ZWh = unit("ZWh", 10**21 * Wh, "zettawatt-hour")    # Zettawatt-hour
EWh = unit("EWh", 10**18 * Wh, "exawatt-hour")      # Exawatt-hour
PWh = unit("PWh", 10**15 * Wh, "petawatt-hour")     # Petawatt-hour
TWh = unit("TWh", 10**12 * Wh, "terawatt-hour")     # Terawatt-hour
GWh = unit("GWh", 10**9 * Wh, "gigawatt-hour")      # Gigawatt-hour
MWh = unit("MWh", 10**6 * Wh, "megawatt-hour")      # Megawatt-hour
kWh = unit("kWh", 10**3 * Wh, "kilowatt-hour")      # Kilowatt-hour
hWh = unit("hWh", 10**2 * Wh, "hectowatt-hour")     # Hectowatt-hour
daWh = unit("daWh", 10**1 * Wh, "decawatt-hour")    # Decawatt-hour
dWh = unit("dWh", 10**-1 * Wh, "deciwatt-hour")     # Deciwatt-hour
cWh = unit("cWh", 10**-2 * Wh, "centiwatt-hour")    # Centiwatt-hour
mWh = unit("mWh", 10**-3 * Wh, "milliwatt-hour")    # Milliwatt-hour
μWh = unit("μWh", 10**-6 * Wh, "microwatt-hour")    # Microwatt-hour
nWh = unit("nWh", 10**-9 * Wh, "nanowatt-hour")     # Nanowatt-hour
pWh = unit("pWh", 10**-12 * Wh, "picowatt-hour")    # Picowatt-hour
fWh = unit("fWh", 10**-15 * Wh, "femtowatt-hour")   # Femtowatt-hour
aWh = unit("aWh", 10**-18 * Wh, "attowatt-hour")    # Attowatt-hour
zWh = unit("zWh", 10**-21 * Wh, "zeptowatt-hour")   # Zeptowatt-hour
yWh = unit("yWh", 10**-24 * Wh, "yoctowatt-hour")   # Yoctowatt-hour


# cleaning
del Unum
del unit

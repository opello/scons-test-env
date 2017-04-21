# VariantDir tree fix:
import fix

env = Environment()

SConscript('generator/SConscript-generate.py', exports='env', variant_dir='build/generator', duplicate=0)
SConscript('SConscript', exports='env', variant_dir='build/application', duplicate=0)

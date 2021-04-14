from cvars.public import PublicConVar
from plugins.info import PluginInfo


info = PluginInfo("circle_damage_indicator")
info.basename = 'circle_damage_indicator'
info.author = 'qPexLegendary'
info.version = '1.0.0'
info.variable = "cdi_version"
info.convar = PublicConVar(info.variable, info.version, "{0} version".format(info.name))

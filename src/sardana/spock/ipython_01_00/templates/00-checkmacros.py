import PyTango
import json
import sardana.spock.genutils
from IPython import get_ipython


WARNING = '\033[31m'
BOLD = '\033[1m'
ENDC = '\033[0m'

config = sardana.spock.genutils.get_config()


ds=PyTango.DeviceProxy(config.Spock.macro_server_name)
essentials = ds.get_property("EssentialMacros")
essentials=essentials['EssentialMacros']
if not essentials:
    print("No list of essential macros defined, skipping check.")
else:    
    allmacros=ds.read_attribute('MacroList').value

    macrolist = []
    for m in allmacros:
        macrojson = ds.GetMacroInfo([m])
        macroinfo=json.loads(macrojson[0])
        macrolist.append(macroinfo['module']+':'+m)

    allgood = True
    missingmacros=[]
    for em in essentials:
        if str(em) not in macrolist:
            missingmacros.append(str(em))
            allgood = False
    if allgood:
        print('All essential macros found!')
    else:
        print(WARNING+BOLD+'\n------------------------- WARNING! ------------------------\n')
        print('One or several essential macros missing!')
        print('It will not be possible to run scans and collect data in this state.')
        print('Verify that the MacroPath property of the MacroServer is set properly,')
        print('and that all macros exist and are readable by the MacroServer.\n') 
        print('The essential macros are defined in the EssentialMacros property')
        print('of MacroServer: '+str(config.Spock.macro_server_name)+'\n')
        print('Missing macros (module:macroname):')
        for m in missingmacros:
            print(m) 

        ipython = get_ipython()
        ipython.magic("config PromptManager.in_template = '{color.Red}(WARNING) {DOOR_ALIAS} [\\#]: '")



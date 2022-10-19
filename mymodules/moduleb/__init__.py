print("moduleb imported")

import sys
from mymodules.moduleb import funcs as new_funcs
my_funcs = sys.modules['mymodules.modulea.funcs']
my_funcs.print_ok = new_funcs.print_okb

sys.modules['mymodules.modulea.funcs'] = my_funcs

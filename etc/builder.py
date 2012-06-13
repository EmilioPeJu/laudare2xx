from iocbuilder import AutoSubstitution
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.modules.busy import Busy

class lRE2xx(AutoSubstitution, AutoProtocol):
    Dependencies = (Busy,)
    # Substitution attributes
    TemplateFile = 'lRE2xx.template'

    # AutoProtocol attributes
    ProtocolFiles = ['lRE2xx.proto']



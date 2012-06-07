from iocbuilder import AutoSubstitution
from iocbuilder.modules.streamDevice import AutoProtocol

class lRE2xx(AutoSubstitution, AutoProtocol):
    # Substitution attributes
    TemplateFile = 'lRE2xx.template'

    # AutoProtocol attributes
    ProtocolFiles = ['lRE2xx.proto']



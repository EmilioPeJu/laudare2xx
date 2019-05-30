from iocbuilder import AutoSubstitution
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.modules.busy import Busy

class lRE2xx(AutoSubstitution, AutoProtocol):
    Dependencies = (Busy,)
    # Substitution attributes
    TemplateFile = 'lRE2xx.template'

    # AutoProtocol attributes
    ProtocolFiles = ['lRE2xx.proto']

class lIntegralT(AutoSubstitution, AutoProtocol):
    Dependencies = (Busy,)
    # Substitution attributes
    TemplateFile = 'lIntegralT.template'

    # AutoProtocol attributes
    ProtocolFiles = ['lRE2xx.proto']

class lVariocool(AutoSubstitution, AutoProtocol):
    Dependecies = (Busy,)
    #Substitution attributes
    TemplateFile = 'lVariocool.template'
    
    #AutoProtocol attributes
    ProtocolFiles = ['lREVariocool.proto']

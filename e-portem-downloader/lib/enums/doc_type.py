"""Doc Type
"""
from enum import Enum


class DocType(Enum):
    """Doc type enum
    """
    RECIBOS = 'Nomina'
    CERTIFRETEN = 'Certificado_retencion'
    DECJURADA = 'Declaracion_jurada'

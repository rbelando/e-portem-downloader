"""Structure folders
"""

import os
import shutil
from lib.constants.path import OUTPUT_PATH, RECIBOS_PATH, DECJURADA_PATH, CERTIF_RETEN_PATH


def create_output_folder_structure():
    """Create output folder
    """
    if not os.path.isdir(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
    else:
        shutil.rmtree(OUTPUT_PATH, ignore_errors=True)
        os.makedirs(OUTPUT_PATH)


def create_nominas_folder():
    """Create output folder
    """
    if not os.path.isdir(RECIBOS_PATH):
        os.makedirs(RECIBOS_PATH)


def create_dec_jurada_folder():
    """Create Declaracion jurada folder
    """
    if not os.path.isdir(DECJURADA_PATH):
        os.makedirs(DECJURADA_PATH)


def create_certif_reten_folder():
    """Create certificacion retenciones folder
    """
    if not os.path.isdir(CERTIF_RETEN_PATH):
        os.makedirs(CERTIF_RETEN_PATH)

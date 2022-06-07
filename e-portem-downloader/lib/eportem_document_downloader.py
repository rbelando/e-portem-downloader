import os

import requests

from lib.constants.path import (CERTIF_RETEN_PATH, DECJURADA_PATH, OUTPUT_PATH,
                                RECIBOS_PATH)
from lib.enums.doc_type import DocType
from lib.enums.file_extions import FileExtension
from lib.folder_structure import (create_certif_reten_folder,
                                  create_dec_jurada_folder,
                                  create_nominas_folder)
from lib.models.eportem_document import EPortemDocument


class EportemDocumentDownloader():

    def execute(self, eportem_document: EPortemDocument) -> None:
        doc_date_month = eportem_document.get_created_at().month
        doc_date_year = eportem_document.get_created_at().year
        doc_folder_path = OUTPUT_PATH
        file_extension = FileExtension.PDF.value if eportem_document.get_doc_type(
        ).value == 'Nomina' else FileExtension.HTML.value
        file_name = f'{eportem_document.get_file_name()}.{file_extension}'

        if DocType.CERTIFRETEN == eportem_document.get_doc_type():
            doc_folder_path = CERTIF_RETEN_PATH
            create_certif_reten_folder()
        if DocType.RECIBOS == eportem_document.get_doc_type():
            doc_folder_path = RECIBOS_PATH
            create_nominas_folder()
        if DocType.DECJURADA == eportem_document.get_doc_type():
            doc_folder_path = DECJURADA_PATH
            create_dec_jurada_folder()

        # Year folder creation
        year_folder = os.path.join(doc_folder_path, str(doc_date_year))
        if not os.path.isdir(year_folder):
            os.makedirs(year_folder)

        # Month folder creation
        month_year = os.path.join(year_folder, str(doc_date_month))
        if not os.path.isdir(month_year):
            os.makedirs(month_year)

        data = requests.get(eportem_document.get_document_url(),
                            cookies={'.ASPXAUTH': os.getenv('ASPXAUTH')})
        download_file_path = os.path.join(month_year, file_name)
        with open(download_file_path, 'wb') as file:
            file.write(data.content)

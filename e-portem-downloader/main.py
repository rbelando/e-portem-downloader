"""Main script file for download documents from e-portem
"""
import os

import requests
from dotenv import load_dotenv

from lib.constants.locators import RECOVER_PASSWORD_LOCATOR
from lib.constants.ursl import BASE_PAGE, DOCUMENT_PAGE
from lib.eportem_document_downloader import EportemDocumentDownloader
from lib.eportem_response import EportemResponse
from lib.folder_structure import create_output_folder_structure

load_dotenv()

if "ASPXAUTH" in os.environ:
    create_output_folder_structure()
    for index in (number + 1 for number in range(20)):
        response = requests.get(f'{BASE_PAGE}{DOCUMENT_PAGE}{index}',
                                cookies={'.ASPXAUTH': os.getenv('ASPXAUTH')})
        if response.status_code == 200 and RECOVER_PASSWORD_LOCATOR not in response.text:
            eportem_response = EportemResponse()
            doc_downloader = EportemDocumentDownloader()
            for doc in eportem_response.process(response_text=response.text):
                doc_downloader.execute(doc)
        else:
            print(
                'There is a problem with your credentials. Please review .ASPXAUTH value is correct'
            )
            break
else:
    raise Exception("ASPXAUTH is not set in .env file")

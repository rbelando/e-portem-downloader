"""Eportem response
"""

import re
from datetime import datetime

from lib.constants.locators import DATE_PATTERN, DOC_TYPE_PATTERN
from lib.constants.ursl import DOCUMNET_DETAIL_URL, BASE_PAGE
from lib.enums.doc_type import DocType
from lib.models.eportem_document import EPortemDocument


class EportemResponse():
    """eportem response handler
    """

    def process(self, response_text: str) -> EPortemDocument:
        """Process the response text from eportem

        Args:
            response_text (str): The response text from request object

        Returns:
            List[EPortemDocument]: list of EportemDocuments
        """
        for match in re.finditer(DOCUMNET_DETAIL_URL, response_text):
            # Getting Document ID
            match_index = match.end()
            quotes_index = response_text[match_index:].find('"')
            end_index_doc_id = match_index + quotes_index
            doc_id = response_text[match_index:end_index_doc_id]
            # Getting Date
            end_index_date_pattern = response_text[end_index_doc_id:].find(
                DATE_PATTERN) + len(DATE_PATTERN)
            start_date_index = end_index_doc_id + end_index_date_pattern
            closing_div_index = response_text[start_date_index:].find('</div>')
            end_index_date = start_date_index + closing_div_index
            doc_date = response_text[start_date_index:end_index_date]
            # Getting document type
            end_index_doc_type_pattern = response_text[end_index_date:].find(
                DOC_TYPE_PATTERN) + len(DOC_TYPE_PATTERN)
            start_doc_type_index = end_index_doc_type_pattern + end_index_date
            closing_div_index = response_text[start_doc_type_index:].find(
                '</div>')
            end_index_doc_type = start_doc_type_index + closing_div_index
            doc_type = response_text[start_doc_type_index:end_index_doc_type]
            eportem_document = EPortemDocument(
                created_at=datetime.strptime(doc_date, '%d/%m/%Y').date(),
                document_url=f'{BASE_PAGE}{DOCUMNET_DETAIL_URL}{doc_id}',
                doc_type=DocType[doc_type.replace(" ", "")])
            yield eportem_document

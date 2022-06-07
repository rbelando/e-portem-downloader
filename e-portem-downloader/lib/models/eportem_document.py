"""E-portem Document Model
"""
from datetime import date
from lib.enums.doc_type import DocType


class EPortemDocument:
    """Representation of document from e-portem documents
    """
    _created_at: date
    _document_url: str
    _doc_type: DocType

    def __init__(self, created_at: date, document_url: str,
                 doc_type: DocType) -> None:
        self._created_at = created_at
        self._document_url = document_url
        self._doc_type = doc_type

    def get_created_at(self) -> date:
        """returns the created date of the document

        Returns:
            created_at (date): created date of the document
        """
        return self._created_at

    def set_created_at(self, created_at: date) -> None:
        """update the created date of the document

        Args:
            created_at (date): _description_
        """
        self._created_at = created_at

    def get_document_url(self) -> str:
        """return the document url

        Returns:
            document_url (str): partial url of the document
        """
        return self._document_url

    def set_document_url(self, document_url: str) -> None:
        """update the document url

        Args:
            document_url (str): partial url of the document
        """
        self._document_url = document_url

    def get_doc_type(self) -> DocType:
        """return the document type

        Returns:
            doc_type: document type
        """
        return self._doc_type

    def set_doc_type(self, doct_type: DocType) -> None:
        """update doc_type

        Args:
            doct_type (str): document type
        """
        self._doc_type = doct_type

    def get_file_name(self):
        """return the file name

        Returns:
            file_name: the file name
        """
        return f'{self._doc_type.value}_{self._created_at.year}-{self._created_at.month}-{self._created_at.day}'

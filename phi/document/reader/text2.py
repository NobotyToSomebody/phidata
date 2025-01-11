from typing import List
from phi.document.base import Document
from phi.document.reader.base import Reader
from phi.utils.log import logger
import hashlib

class TextReader2(Reader):
    """Reader for Info"""
    def read(self, info:str) -> List[Document]:
        if info.__len__ == 0:
            raise ValueError("Empty info")

        try:
            data = info.encode('utf-8')
            md5 = hashlib.md5(data)

            documents = [
                Document(
                    name=md5.hexdigest,
                    id=md5.hexdigest,
                    content=info,
                )
            ]
            if self.chunk:
                chunked_documents = []
                for document in documents:
                    chunked_documents.extend(self.chunk_document(document))
                return chunked_documents
            return documents
        except Exception as e:
            logger.error(f"Error reading: {info}: {e}")
            return []

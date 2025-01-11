from pathlib import Path
from typing import Union, List, Iterator

from phi.document import Document
from phi.document.reader.text2 import TextReader2
from phi.knowledge.agent import AgentKnowledge


class TextKnowledgeBase2(AgentKnowledge):
    info: str = ""
    reader: TextReader2 = TextReader2()

    @property
    def document_lists(self) -> Iterator[List[Document]]:
        """Iterate over text files and yield lists of documents.
        Each object yielded by the iterator is a list of documents.

        Returns:
            Iterator[List[Document]]: Iterator yielding list of documents
        """
        yield self.reader.read(info=self.info)
    
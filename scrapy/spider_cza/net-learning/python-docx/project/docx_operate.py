from docx import Document

def get_document(file):
    return Document(str)


class DocxReader:
    def __init__(self, document):
        self.document = document
        self.tables = self.document.tables
        self.tables_res = []

    @classmethod
    def from_str(cls, string=None, path=None):
        file = string if string else path
        if file:
            return cls(get_document(file))
        else:
            raise Exception("None thing to reading")

    def table_manage(self, ):
        pass

    def table2dict(self, ):
        for table in self.tables:
            res = {}

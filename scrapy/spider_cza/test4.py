class LLDownloadItem(object):
    pass

class PlasticFile(object):
    def __init__(self, *args, **kwargs):
        pass
    def process(self, pre=False):
        pass
    def to_dict(self):
        pass

class LLDownloadPipe(object):
    def process_item(self, item, spider):
        if isinstance(item, LLDownloadItem):
            item["source"] = [PlasticFile(**obj).process(pre=True).to_dict() for obj in item["source"]]
            item = dict(item)
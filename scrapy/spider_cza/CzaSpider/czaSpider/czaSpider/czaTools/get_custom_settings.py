from czaSpider import pipelines


def get_custom_settings(name):
    return getattr(pipelines, name[name.rfind('-') + 1:] + "Pipeline_setting")
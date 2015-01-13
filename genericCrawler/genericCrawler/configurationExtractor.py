__author__ = 'aviad elitzur'

import xml.etree.ElementTree as ET

class ConfigExtractor():
    FileName = ''

    @staticmethod
    def getTemplates():
        """
        go over all the templates and create list of PageTemplate
        """
        parser = ET.parse(ConfigExtractor.FileName)
        res=[]
        templates = parser.find('templates').getchildren()
        for template in templates:
            fields = []
            for field in template.find('extract_fields').getchildren():
                fields.append(DBField(**field.attrib))
            tmp=PageTemplate(fields,**template.attrib)
            res.append(tmp)
            return res

    @staticmethod
    def getStartURLs():
        """return list of start URLs"""
        parser = ET.parse(ConfigExtractor.FileName)
        res = []
        urls = parser.find('start_urls')
        urls = urls.findall('url')
        for url in urls:
            res.append(url.attrib['url'])
        return res
    @staticmethod
    def getDomain():
        """return domain for crawling"""
        parser = ET.parse(ConfigExtractor.FileName)
        domain = parser.find('domain')
        return domain.attrib['domain']
    @staticmethod
    def getLoginValuesDict():
        """return dictionary of login values"""
        parser = ET.parse(ConfigExtractor.FileName)
        return parser.find('login').attrib
    @staticmethod
    def getDepth():
        parser = ET.parse(ConfigExtractor.FileName)
        return int(parser.find('depth').text)
    @staticmethod
    def getDBpath():
        parser = ET.parse(ConfigExtractor.FileName)
        path = parser.find('DB_path').text
        return path


class PageTemplate():
    """
    define a page template for crawling
    template contains its characteristic in attributes
     and fields to extract in list of DBFields
    """
    def __init__(self, fields, **entries):
        self.__dict__.update(entries)
        self.fields = fields

class DBField():
    """
    defines one field to extract
    """
    def __init__(self, **entries):
        self.__dict__.update(entries)


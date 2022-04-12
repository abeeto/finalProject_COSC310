from msilib.schema import Media
from mediawiki import MediaWiki
import mediawiki

class wiki:
    
    @staticmethod
    def returnTopics(search):
        try:
            wikipedia = MediaWiki()
            p = wikipedia.page(search)
            topics = [topic for topic in p.sections if topic not in ['Bibliography', 'Further reading', 'Notes', 'References', 'External links', 'See also']]
            return [search,topics]
        except:
            return "Couldn't find anything on wikipedia"
    @staticmethod
    def returnContents(search, topic):
        try:
            wikipedia = MediaWiki()
            p = wikipedia.page(search)
            return p.section(topic)
        except Exception as e:
            return e




print(wiki.returnTopics("Kanye West"))
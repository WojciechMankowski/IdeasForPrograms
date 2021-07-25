from notion.client import NotionClient
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
from os import environ
class NotionAPISupport:
    def __init__(self):
        load_dotenv()
        token_v2 = environ.get('token_v2')
        url = "https://www.notion.so/b3d441ef28844fdc92ca3109b7d57577?v=fe38a190be464f31a2ccbf117645699d"
        self.client = NotionClient(token_v2=token_v2)
        self.collection_view = self.client.get_collection_view(url)
    def GetInformation(self):
        ideas = {}
        url = "https://www.notion.so/b3d441ef28844fdc92ca3109b7d57577?v=fe38a190be464f31a2ccbf117645699d"
        self.collection_view = self.client.get_collection_view(url)
        rows = self.collection_view.collection.get_rows()
        for item in rows:
            ideas[item.title] = {
                'Status': item.Status, 'Link GitHub': item.Link_GitHub

            }
        return ideas
    def AddingANewLine(self, title: str,status: str,link: str,opis: str):
        row = self.collection_view.collection.add_row()
        row.title = title
        row.Status = status
        row.Link_GitHub = link
        row.Opis = opis







# row = collection_view.collection.add_row()
# row.title = "Stworzenie api z pomysłami z Noit"
# row.Status = 'zarys pomysłu'
# row.Created = datetime.today()

if __name__ == '__main__':
    support = NotionAPISupport()
    idea = support.GetInformation()
    print(idea)


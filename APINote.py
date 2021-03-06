from notion.client import NotionClient
from dotenv import load_dotenv
from os import environ

class NotionAPISupport:
    def __init__(self):
        load_dotenv()


        token_v2 = environ.get('token_v2')
        self.url =\
            "https://www.notion.so/b3d441ef28844fdc92ca3109b7d57577?v=fe38a190be464f31a2ccbf117645699d"
        self.client = NotionClient(token_v2=token_v2)
        self.collection_view = self.client.get_collection_view(self.url)

    def GetInformation(self):
        ideas = {}
        url = "https://www.notion.so/b3d441ef28844fdc92ca3109b7d57577?v=fe38a190be464f31a2ccbf117645699d"
        self.collection_view = self.client.get_collection_view(url)
        rows = self.collection_view.collection.get_rows()
        for item in rows:
            if item.Comment == '?':
                Comment = None
            else:
                Comment = item.Comment
            if item.Opis == '?': Opis = None
            else:
                Opis = item.Opis
            # print(item.Status)
            ideas[item.title] = {
                'Status': item.Status, "Opis": Opis, 'Link GitHub': item.Link_GitHub,
                'Rating': item.Rating, "Komentarze": Comment

            }
        return ideas

    def AddingANewLine(self, title: str,status: str,link: str, opis: str, rating: int):
        row = self.collection_view.collection.add_row()
        row.title = title
        row.Status = status
        row.Link_GitHub = link
        row.Opis = opis
        row.Rating = rating
        row.NumberOfRatings = 1

    def AssessmentOfChanges(self, rating: float, title):
        cv = self.client.get_collection_view(self.url)
        CV = cv.collection.get_rows(search =title)
        for item in CV:
            item.Rating = item.Rating + rating
            item.NumberOfRatings = item.NumberOfRatings + 1
            print(item.Rating)
    def AddComment(self, comment, title):
        cv = self.client.get_collection_view(self.url)
        CV = cv.collection.get_rows(search=title)
        for item in CV:
            item.Comment = item.Comment + "," + comment
    def DowlandTitle(self):
        self.collection_view = self.client.get_collection_view(self.url)
        rows = self.collection_view.collection.get_rows()
        listTitle = []
        for item in rows:
            listTitle.append(item.title)
        return listTitle





# row = collection_view.collection.add_row()
# row.title = "Stworzenie api z pomys??ami z Noit"
# row.Status = 'zarys pomys??u'
# row.Created = datetime.today()

if __name__ == '__main__':
    support = NotionAPISupport()
    # idea = support.GetInformation()
    # print(idea)
    support.AssessmentOfChanges(3,"Testowy")
    support.AddComment("test", 'Testowy')


from pydantic import BaseModel
import pickle
import codecs


class Book(BaseModel):
    isbn: int
    title: str


def serialize(book: Book) -> str:
    return codecs.encode(pickle.dumps(book), "base64").decode()

def deserialize(obj:str):
    return pickle.loads(codecs.decode(obj.encode(),"base64"))

Book_Default = Book(isbn=884, title='Clean Code: A Handbook of Agile Software Craftsmanship')



if __name__ == "__main__":
    a = serialize(Book_Default)
    print(a)
    print(deserialize(a).isbn,deserialize(a).title)

   



    


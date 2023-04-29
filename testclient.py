import requests #needs to be run in 3.7.6 base interpreter
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import pickle
import codecs

class Book(BaseModel):
    isbn: int
    title: str

Book_Default = Book(isbn=9780132350884, title='Clean Code: A Handbook of Agile Software Craftsmanship')

def serialize(book: Book) -> str:
    return codecs.encode(pickle.dumps(book), "base64").decode()
def deserialize(obj:str):
    return pickle.loads(codecs.decode(obj.encode(),"base64"))


def req_post_book(port=5000, book=Book_Default):
    req_data = serialize(book)
    print(type(req_data)) # should be string

    url2 = 'http://127.0.0.1:{}/books_str/'.format(port)
    response = requests.post(url2, data=req_data)
    result = response.json()
    print(result['status'])

    # url = 'http://127.0.0.1:{}/books/'.format(port)
    # response = requests.post(url, data=req_data)
    # result = response.json()
    # print(result['status'])




# def req_post(port=5000):
#     headers = {'Content-Type': 'application/json'}
#     data = {'id': 100, 'name': "Jay", 'city': "Kochi"}
#     url = 'http://127.0.0.1:{}/getInformation'.format(port)
#     response = requests.post(url, data=json.dumps(data), headers=headers)
#     result = response.json()
#     if result:
#         print(result['status'])
#     else:
#         print(result)

# def req_get(port=5000):
#     # look for password in cracked password database first
#     response = requests.get("%s/items" %('http://127.0.0.1:{}/'.format(port)))
#     result = response.json()
#     if result is not None:
#         print('Success')
#         return
#     else:
#         print("None")
    



if __name__ == "__main__":
    # req_post(5000)
    req_post_book(5000)


   



    


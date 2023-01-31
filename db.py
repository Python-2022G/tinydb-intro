from tinydb import TinyDB
from tinydb.table import Document

db = TinyDB('db.json', indent=4)

u1 = {'chat_id': 5, 'username': 'User1'}
u2 = {'user_id': 9, 'username': 'User3'}

doc1 = Document(u1, doc_id=100)
doc2 = Document(u2, doc_id=101)

db.insert_multiple([doc1, doc2])

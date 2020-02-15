
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, deferred
from sqlalchemy import Column, Integer, Float, Date, String, DateTime
from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

#connect
connection_string = "postgres://postgres:4fcc9b2c-955f-45fc-93ce-64e3bf36beb8@fincrimedb1.cyiakjau7pt6.us-west-2.rds.amazonaws.com:5432/fincrimedb"
#db = create_engine(connection_string)

#fetch from test table
#some_stuff = db.execute("select * from test").fetchall()
#print(some_stuff)

#load transactions
def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

Base = declarative_base()
class transactions_load(Base):
    __tablename__ = 'transactions'
    __table_args__ = {'sqlite_autoincrement': True}

    #id2 = deferred(Column(Integer))
    curr =  Column(String)
    amt = Column(Integer)
    st =  Column(String)
    crdate = Column(DateTime)
    mer_category = Column(String)
    mer_country = Column(String)
    entry_md = Column(String)
    u_id = Column(String)
    tp = Column(String)
    src = Column(String)
    id1 = Column(UUID(as_uuid=True), primary_key=True)

engine = create_engine(connection_string)
Base.metadata.create_all(engine)
session = sessionmaker()
session.configure(bind=engine)
s = session()

file_name="transactions.csv"
data=Load_Data(file_name)
for i in data:
    record = transactions_load(**{
        #'id2':i[0],
        'curr' : i[0],
        'amt':i[1],
        'st':i[2],
        'crdate':i[3],
        'mer_category':i[4],
        'mer_country':i[5],
        'entry_md':i[6],
        'u_id':i[7],
        'tp':i[8],
        'src':i[9],
        'id1':i[10]
    })
    #print(record.id2)
    s.add(record)
#s.commit()
#s.close()




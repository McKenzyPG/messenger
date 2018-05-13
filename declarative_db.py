from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, MetaData, Column, Integer, String
import socket
Base = declarative_base()
engine = create_engine('sqlite:///memory', echo = True)

class User(Base):
    tablename = 'users'
    id = Column(Integer, primary_key = True)
    username = Column(String)
    fullname = Column(String)
    bio - Column(String)
    password = Column(String)
    ip = socket.gethostbyname(socket.getfqdn())

    def __init__(self, username, fullname, bio, password):
        self.username = username
        self.fullname = fullname
        self.bio = bio
        self.password = password
        self.ip = ip

    def __repr__(self):
        return "<User('%s', '%s','%s','%s','%s')>" % \
            self.username, self.fullname, self.bio, self.password, self.ip

users_table = User.__table__

metadata = Base.MetaData()

##########Session##########

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)

session = Session()

admin = User('admin', 'admin admin', 'born to root', 'admin123')
session.add(admin)

user1 = User('Deseptikon', 'Ivan Ivanov', 'Born in a galaxy far far away', '123qwe')
user2 = User('spiderman', 'Petr Petrov', 'maggleborn', '456asd')
user3 = User('wondergirl', 'Anna Pulemtechitsa', 'civil war hero', '1917revo')

#######Simple query#####

query1 = session.query(User).filter_by('spiderman').first()

session.add_all(User('manchkin', 'Sidr Sidrovich', 'make me proud', 'kosovojesrbija'), User('bourbon', 'Allain Barbier', 'a devenir', 'lemotdepasse'))

session.commit()

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import String,Boolean,Integer,Column,Text,ForeignKey

engine=create_engine("postgresql://postgres:naaga2244@localhost/Relationship",
    echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    orders = relationship("Order", back_populates="customer")

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship("Customer", back_populates="orders")    

print("Creating database.........")

Base.metadata.create_all(engine)
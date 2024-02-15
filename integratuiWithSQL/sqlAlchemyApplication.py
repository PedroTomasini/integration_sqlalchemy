import sqlalchemy as sqlA
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    # Atribulos da tabela
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname}"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"

print(User. __tablename__)
print(Address. __tablename__)

# Conexão com o banco de dados
engine = create_engine("sqlite://")

# Criando as clases como tabelas do banco de dados
Base.metadata.create_all(engine)

# Investiga o esquema do banco de dados
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    pedro = User(
        name='pedro',
        fullname='Pedro Tomasini',
        address=[Address(email_address='pedro@email.com')]
    )
    marcus = User(
        name='marcus',
        fullname='Marcus Tomasini',
        address=[Address(email_address='marcus@email.com'),
                 Address(email_address='marcust@email.com')]
    )
    patrick = User(
        name='patrick',
        fullname='Patrick Tomasini',
        address=[Address(email_address='patrick@email.com')]
    )

    # Enviando para o BD (persistência de dados)
    session.add_all([pedro, marcus, patrick])
    session.commit()


"""Base de datos ligera para referencias de canciones y emociones."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

ENGINE = create_engine("sqlite:///data/references.db")
SessionLocal = sessionmaker(bind=ENGINE)
Base = declarative_base()


class Reference(Base):
    __tablename__ = "references"
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, unique=True, index=True)


def init_db() -> None:
    Base.metadata.create_all(bind=ENGINE)


def save_reference(path: str) -> None:
    session = SessionLocal()
    ref = Reference(path=path)
    session.add(ref)
    session.commit()
    session.close()

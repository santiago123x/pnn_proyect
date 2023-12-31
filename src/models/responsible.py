from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Responsible(Base):
    __tablename__= 'Responsibles'

    id = Column(Integer, primary_key=True)
    institution_id = Column(Integer, ForeignKey("Institutions.id"))
    input_id = Column(Integer, ForeignKey("Inputs.id"))

    # Relación con la tabla Actor
    institution = relationship("Institution", back_populates="responsibles")
    # Relación con la tabla Responsible
    input = relationship("Input", back_populates="responsibles")
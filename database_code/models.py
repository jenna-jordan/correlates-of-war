from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    ForeignKeyConstraint,
    String,
    Text,
    Integer,
    Boolean,
    Date,
)

Base = declarative_base()


class Polity(Base):
    __tablename__ = "polity"

    id = Column(String(5), primary_key=True)
    name = Column(Text)
    type = Column(Text)
    abbr = Column(String(3))


class Polity_Dates(Base):
    __tablename__ = "polity_dates"

    polity = Column(String(5), primary_key=True)
    start_date = Column(Date, primary_key=True)
    end_date = Column(Date)

    __table_args__ = (ForeignKeyConstraint(["polity"], ["polity.id"]),)


class War_Type(Base):
    __tablename__ = "war_type"

    type_code = Column(Integer(1), primary_key=True)
    war_category = Column(String(11))
    war_subtype = Column(Text)
    type_description = Column(Text)
    last_updated = Column(Date)


class War(Base):
    __tablename__ = "war"

    id = Column(String(5), primary_key=True)
    name = Column(Text)
    type_code = Column(Integer(1))
    type_name = Column(Text)
    subtype_name = Column(Text)
    is_intervention = Column(Boolean)
    is_international = Column(Boolean)

    __table_args__ = (ForeignKeyConstraint(["type_code"], ["war_type.type_code"]),)


class War_Locations(Base):
    __tablename__ = "war_locations"

    war = Column(String(5), primary_key=True)
    region = Column(Text, primary_key=True)

    __table_args__ = (ForeignKeyConstraint(["war"], ["war.id"]),)


class War_Sides(Base):
    __tablename__ = "war_sides"

    war = Column(String(5), primary_key=True)
    side = Column(String(1), primary_key=True)
    deaths = Column(Integer)
    peak_total_forces = Column(Integer)
    peak_theater_forces = Column(Integer)


class War_Participants(Base):
    __tablename__ = "war_participants"

    war = Column(String(5), primary_key=True)
    polity = Column(String(5), primary_key=True)
    start_date = Column(Date, primary_key=True)
    start_date_prec = Column(Text)
    end_date = Column(Date)
    end_date_prec = Column(Text)
    side = Column(String(1))
    is_initiator = Column(Boolean)
    outcome = Column(Text)

    __table_args__ = (
        ForeignKeyConstraint(["war"], ["war.id"]),
        ForeignKeyConstraint(["polity"], ["polity.id"]),
        ForeignKeyConstraint(["war", "side"], ["war_sides.war", "war_sides.side"]),
    )


class War_Transitions(Base):
    __tablename__ = "war_transitions"

    from_war = Column(String(5), primary_key=True)
    to_war = Column(String(5), primary_key=True)

    __table_args__ = (
        ForeignKeyConstraint(["from_war"], ["war.id"]),
        ForeignKeyConstraint(["to_war"], ["war.id"]),
    )


class Resources(Base):
    __tablename__ = "resources"

    polity = Column(String(5), primary_key=True)
    year = Column(Integer(4), primary_key=True)
    resource = Column(String(10), primary_key=True)
    amount = Column(Integer)
    source = Column(Text)
    note = Column(Text)
    quality_code = Column(String(1))
    anomoly_code = Column(String(1))

    __table_args__ = (ForeignKeyConstraint(["polity"], ["polity.id"]),)

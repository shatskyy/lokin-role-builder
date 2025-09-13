from __future__ import annotations

from sqlalchemy import JSON, DateTime, ForeignKey, Index, Integer, Real, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class OnetOccupation(Base):
    __tablename__ = "onet_occupations"

    onet_code: Mapped[str] = mapped_column(String(20), primary_key=True)
    title: Mapped[str] = mapped_column(String(255), index=True)
    description: Mapped[str | None] = mapped_column(Text())
    job_zone: Mapped[int | None] = mapped_column(Integer())

    alt_titles: Mapped[list["OnetAltTitle"]] = relationship(back_populates="occupation", cascade="all, delete-orphan")
    tasks: Mapped[list["OnetTask"]] = relationship(back_populates="occupation", cascade="all, delete-orphan")
    skills: Mapped[list["OnetSkill"]] = relationship(back_populates="occupation", cascade="all, delete-orphan")
    knowledge: Mapped[list["OnetKnowledge"]] = relationship(back_populates="occupation", cascade="all, delete-orphan")
    abilities: Mapped[list["OnetAbility"]] = relationship(back_populates="occupation", cascade="all, delete-orphan")
    work_styles: Mapped[list["OnetWorkStyle"]] = relationship(back_populates="occupation", cascade="all, delete-orphan")


class OnetAltTitle(Base):
    __tablename__ = "onet_alt_titles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    onet_code: Mapped[str] = mapped_column(ForeignKey("onet_occupations.onet_code", ondelete="CASCADE"), index=True)
    alt_title: Mapped[str] = mapped_column(String(255))

    occupation: Mapped[OnetOccupation] = relationship(back_populates="alt_titles")

    __table_args__ = (
        Index("uq_onet_alt_title", "onet_code", "alt_title", unique=True),
        Index("ix_onet_alt_title_title", "alt_title"),
    )


class OnetTask(Base):
    __tablename__ = "onet_tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    onet_code: Mapped[str] = mapped_column(ForeignKey("onet_occupations.onet_code", ondelete="CASCADE"), index=True)
    task: Mapped[str] = mapped_column(Text())
    importance: Mapped[float | None] = mapped_column(Real)
    frequency: Mapped[float | None] = mapped_column(Real)

    occupation: Mapped[OnetOccupation] = relationship(back_populates="tasks")


class OnetSkill(Base):
    __tablename__ = "onet_skills"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    onet_code: Mapped[str] = mapped_column(ForeignKey("onet_occupations.onet_code", ondelete="CASCADE"), index=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    importance: Mapped[float | None] = mapped_column(Real)
    level: Mapped[float | None] = mapped_column(Real)

    occupation: Mapped[OnetOccupation] = relationship(back_populates="skills")


class OnetKnowledge(Base):
    __tablename__ = "onet_knowledge"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    onet_code: Mapped[str] = mapped_column(ForeignKey("onet_occupations.onet_code", ondelete="CASCADE"), index=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    importance: Mapped[float | None] = mapped_column(Real)
    level: Mapped[float | None] = mapped_column(Real)

    occupation: Mapped[OnetOccupation] = relationship(back_populates="knowledge")


class OnetAbility(Base):
    __tablename__ = "onet_abilities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    onet_code: Mapped[str] = mapped_column(ForeignKey("onet_occupations.onet_code", ondelete="CASCADE"), index=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    importance: Mapped[float | None] = mapped_column(Real)
    level: Mapped[float | None] = mapped_column(Real)

    occupation: Mapped[OnetOccupation] = relationship(back_populates="abilities")


class OnetWorkStyle(Base):
    __tablename__ = "onet_work_styles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    onet_code: Mapped[str] = mapped_column(ForeignKey("onet_occupations.onet_code", ondelete="CASCADE"), index=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    importance: Mapped[float | None] = mapped_column(Real)

    occupation: Mapped[OnetOccupation] = relationship(back_populates="work_styles")


class RoleRequest(Base):
    __tablename__ = "role_requests"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    founder_id: Mapped[str | None] = mapped_column(String(255))
    inputs_json: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[str | None] = mapped_column(DateTime(timezone=True))

    generated_roles: Mapped[list["GeneratedRole"]] = relationship(back_populates="request", cascade="all, delete-orphan")


class GeneratedRole(Base):
    __tablename__ = "generated_roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    role_request_id: Mapped[int] = mapped_column(ForeignKey("role_requests.id", ondelete="CASCADE"), index=True)
    onet_code: Mapped[str | None] = mapped_column(String(20))
    output_json: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[str | None] = mapped_column(DateTime(timezone=True))

    request: Mapped[RoleRequest] = relationship(back_populates="generated_roles")


class SystemMeta(Base):
    __tablename__ = "system_meta"

    key: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[str | None] = mapped_column(Text())



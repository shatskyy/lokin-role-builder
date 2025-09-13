"""init schema

Revision ID: 20250913_000001
Revises: 
Create Date: 2025-09-13 00:00:01
"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20250913_000001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # onet_occupations
    op.create_table(
        "onet_occupations",
        sa.Column("onet_code", sa.String(length=20), primary_key=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("job_zone", sa.Integer(), nullable=True),
    )
    op.create_index("ix_onet_occupations_title", "onet_occupations", ["title"], unique=False)

    # onet_alt_titles
    op.create_table(
        "onet_alt_titles",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("onet_code", sa.String(length=20), nullable=False),
        sa.Column("alt_title", sa.String(length=255), nullable=False),
        sa.ForeignKeyConstraint(["onet_code"], ["onet_occupations.onet_code"], ondelete="CASCADE"),
    )
    op.create_index("ix_onet_alt_titles_onet_code", "onet_alt_titles", ["onet_code"], unique=False)
    op.create_index("ix_onet_alt_title_title", "onet_alt_titles", ["alt_title"], unique=False)
    op.create_unique_constraint("uq_onet_alt_title", "onet_alt_titles", ["onet_code", "alt_title"])

    # onet_tasks
    op.create_table(
        "onet_tasks",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("onet_code", sa.String(length=20), nullable=False),
        sa.Column("task", sa.Text(), nullable=False),
        sa.Column("importance", sa.REAL(), nullable=True),
        sa.Column("frequency", sa.REAL(), nullable=True),
        sa.ForeignKeyConstraint(["onet_code"], ["onet_occupations.onet_code"], ondelete="CASCADE"),
    )
    op.create_index("ix_onet_tasks_onet_code", "onet_tasks", ["onet_code"], unique=False)

    # onet_skills
    op.create_table(
        "onet_skills",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("onet_code", sa.String(length=20), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("importance", sa.REAL(), nullable=True),
        sa.Column("level", sa.REAL(), nullable=True),
        sa.ForeignKeyConstraint(["onet_code"], ["onet_occupations.onet_code"], ondelete="CASCADE"),
    )
    op.create_index("ix_onet_skills_onet_code", "onet_skills", ["onet_code"], unique=False)
    op.create_index("ix_onet_skills_name", "onet_skills", ["name"], unique=False)

    # onet_knowledge
    op.create_table(
        "onet_knowledge",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("onet_code", sa.String(length=20), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("importance", sa.REAL(), nullable=True),
        sa.Column("level", sa.REAL(), nullable=True),
        sa.ForeignKeyConstraint(["onet_code"], ["onet_occupations.onet_code"], ondelete="CASCADE"),
    )
    op.create_index("ix_onet_knowledge_onet_code", "onet_knowledge", ["onet_code"], unique=False)
    op.create_index("ix_onet_knowledge_name", "onet_knowledge", ["name"], unique=False)

    # onet_abilities
    op.create_table(
        "onet_abilities",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("onet_code", sa.String(length=20), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("importance", sa.REAL(), nullable=True),
        sa.Column("level", sa.REAL(), nullable=True),
        sa.ForeignKeyConstraint(["onet_code"], ["onet_occupations.onet_code"], ondelete="CASCADE"),
    )
    op.create_index("ix_onet_abilities_onet_code", "onet_abilities", ["onet_code"], unique=False)
    op.create_index("ix_onet_abilities_name", "onet_abilities", ["name"], unique=False)

    # onet_work_styles
    op.create_table(
        "onet_work_styles",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("onet_code", sa.String(length=20), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("importance", sa.REAL(), nullable=True),
        sa.ForeignKeyConstraint(["onet_code"], ["onet_occupations.onet_code"], ondelete="CASCADE"),
    )
    op.create_index("ix_onet_work_styles_onet_code", "onet_work_styles", ["onet_code"], unique=False)
    op.create_index("ix_onet_work_styles_name", "onet_work_styles", ["name"], unique=False)

    # role_requests
    op.create_table(
        "role_requests",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("founder_id", sa.String(length=255), nullable=True),
        sa.Column("inputs_json", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
    )

    # generated_roles
    op.create_table(
        "generated_roles",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("role_request_id", sa.Integer(), nullable=False),
        sa.Column("onet_code", sa.String(length=20), nullable=True),
        sa.Column("output_json", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["role_request_id"], ["role_requests.id"], ondelete="CASCADE"),
    )
    op.create_index("ix_generated_roles_request_id", "generated_roles", ["role_request_id"], unique=False)

    # system_meta
    op.create_table(
        "system_meta",
        sa.Column("key", sa.String(length=255), primary_key=True),
        sa.Column("value", sa.Text(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("system_meta")
    op.drop_index("ix_generated_roles_request_id", table_name="generated_roles")
    op.drop_table("generated_roles")
    op.drop_table("role_requests")
    op.drop_index("ix_onet_work_styles_name", table_name="onet_work_styles")
    op.drop_index("ix_onet_work_styles_onet_code", table_name="onet_work_styles")
    op.drop_table("onet_work_styles")
    op.drop_index("ix_onet_abilities_name", table_name="onet_abilities")
    op.drop_index("ix_onet_abilities_onet_code", table_name="onet_abilities")
    op.drop_table("onet_abilities")
    op.drop_index("ix_onet_knowledge_name", table_name="onet_knowledge")
    op.drop_index("ix_onet_knowledge_onet_code", table_name="onet_knowledge")
    op.drop_table("onet_knowledge")
    op.drop_index("ix_onet_skills_name", table_name="onet_skills")
    op.drop_index("ix_onet_skills_onet_code", table_name="onet_skills")
    op.drop_table("onet_skills")
    op.drop_index("ix_onet_tasks_onet_code", table_name="onet_tasks")
    op.drop_table("onet_tasks")
    op.drop_constraint("uq_onet_alt_title", "onet_alt_titles", type_="unique")
    op.drop_index("ix_onet_alt_title_title", table_name="onet_alt_titles")
    op.drop_index("ix_onet_alt_titles_onet_code", table_name="onet_alt_titles")
    op.drop_table("onet_alt_titles")
    op.drop_index("ix_onet_occupations_title", table_name="onet_occupations")
    op.drop_table("onet_occupations")



"""Add education end_date.

Revision ID: c42ef019a6b7
Revises: e63419b2c20a
"""

from alembic import op
import sqlalchemy as sa

revision = "c42ef019a6b7"
down_revision = "e63419b2c20a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("education", sa.Column("end_date", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("education", "end_date")

"""plan row join to users table

Revision ID: e1a295f4b3f7
Revises: 1a68925c0955
Create Date: 2026-10-28 15:52:14.076696

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1a295f4b3f7'
down_revision: Union[str, Sequence[str], None] = '1a68925c0955'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    plan_enum = sa.Enum("free", "pro", name="user_plan")

    # Avval enum turini bazada yaratish kerak
    plan_enum.create(op.get_bind(), checkfirst=True)

    # Shundan keyin ustunni qo‘shamiz
    op.add_column(
        "users",
        sa.Column(
            "plan",
            plan_enum,
            server_default="free",
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("users", "plan")

    plan_enum = sa.Enum("free", "pro", name="user_plan")
    plan_enum.drop(op.get_bind(), checkfirst=True)
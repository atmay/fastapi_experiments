"""create_user_and_poll_tables

Revision ID: 6dd314e405bc
Revises: 
Create Date: 2022-03-08 22:43:09.992020

"""
from alembic import op
import sqlalchemy as sa
import enum


class PollType(enum.Enum):
    text = 1
    image = 2


# revision identifiers, used by Alembic.
revision = '6dd314e405bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(30), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
    )

    op.create_table(
        'polls',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(30), primary_key=True),
        sa.Column('type', sa.Enum(PollType), nullable=False),
        sa.Column('is_voting_allowed', sa.Boolean(), nullable=False),
        sa.Column(
            'is_adding_choices_allowed',
            sa.Boolean(),
            nullable=False,
        ),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
    )


def downgrade():
    op.drop_table('users')
    op.drop_table('polls')

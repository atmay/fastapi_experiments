"""create_user_and_poll_tables

Revision ID: 6dd314e405bc
Revises: 
Create Date: 2022-03-08 22:43:09.992020

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6dd314e405bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(30), nullable=False, name='username'),
        sa.Column('email', sa.String(100), nullable=False, name='e-mail'),
    )

    op.create_table(
        'polls',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.Integer, primary_key=True, autoincrement=True, name='title'),
        sa.Column('type', sa.String(30), nullable=False, name='type'),
        sa.Column(
            'is_voting_allowed', sa.String(100), nullable=False, name='voting allowed'
        ),
        sa.Column(
            'is_adding_choices_allowed',
            sa.String(100),
            nullable=False,
            name='adding choices allowed',
        ),
    )


def downgrade():
    op.drop_table('users')

"""add content column to table

Revision ID: 2195f51bcac1
Revises: 96e9a231f881
Create Date: 2023-01-12 23:21:27.859616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2195f51bcac1'
down_revision = '96e9a231f881'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass
    


def downgrade() -> None:
    op.drop_column('posts', 'content' )
    pass

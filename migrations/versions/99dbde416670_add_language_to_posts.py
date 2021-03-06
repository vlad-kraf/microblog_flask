"""add language to posts

Revision ID: 99dbde416670
Revises: 606694f9cb51
Create Date: 2020-01-04 11:22:17.306484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99dbde416670'
down_revision = '606694f9cb51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###

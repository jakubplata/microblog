"""add language to posts

Revision ID: fd6ee6f51201
Revises: 02932e896341
Create Date: 2018-09-23 07:56:41.543201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd6ee6f51201'
down_revision = '02932e896341'
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

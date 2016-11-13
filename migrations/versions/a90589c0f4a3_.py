"""empty message

Revision ID: a90589c0f4a3
Revises: None
Create Date: 2016-11-12 18:28:01.828350

"""

# revision identifiers, used by Alembic.
revision = 'a90589c0f4a3'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('title', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'title')
    ### end Alembic commands ###

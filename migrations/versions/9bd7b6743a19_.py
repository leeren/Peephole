"""empty message

Revision ID: 9bd7b6743a19
Revises: c61096e5e8da
Create Date: 2016-11-12 21:28:47.801995

"""

# revision identifiers, used by Alembic.
revision = '9bd7b6743a19'
down_revision = 'c61096e5e8da'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('connections')
    op.drop_table('roles')
    op.drop_table('role_users')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('login_count')
        batch_op.drop_column('last_login_ip')
        batch_op.drop_column('last_login_at')
        batch_op.drop_column('current_login_at')
        batch_op.drop_column('active')
        batch_op.drop_column('password')
        batch_op.drop_column('current_login_ip')

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('current_login_ip', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=255), nullable=True))
        batch_op.add_column(sa.Column('active', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('current_login_at', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('last_login_at', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('last_login_ip', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('login_count', sa.INTEGER(), nullable=True))

    op.create_table('role_users',
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('role_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], [u'roles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], [u'users.id'], )
    )
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), nullable=True),
    sa.Column('description', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('connections',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('provider_id', sa.VARCHAR(length=255), nullable=True),
    sa.Column('provider_user_id', sa.VARCHAR(length=255), nullable=True),
    sa.Column('access_token', sa.VARCHAR(length=255), nullable=True),
    sa.Column('secret', sa.VARCHAR(length=255), nullable=True),
    sa.Column('display_name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('full_name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('profile_url', sa.VARCHAR(length=512), nullable=True),
    sa.Column('image_url', sa.VARCHAR(length=512), nullable=True),
    sa.Column('rank', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###

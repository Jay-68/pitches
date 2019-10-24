"""third Migration

Revision ID: 8e6392b52ad1
Revises: 520ab6c672a7
Create Date: 2019-10-24 10:18:51.346676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e6392b52ad1'
down_revision = '520ab6c672a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('downvotes', sa.Column('id_user', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'downvotes', 'users', ['id_user'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'downvotes', type_='foreignkey')
    op.drop_column('downvotes', 'id_user')
    # ### end Alembic commands ###
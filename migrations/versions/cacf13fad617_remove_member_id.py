"""remove member id

Revision ID: cacf13fad617
Revises: 0c90c3692ab1
Create Date: 2023-04-11 18:14:52.929341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cacf13fad617'
down_revision = '0c90c3692ab1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('member', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=128), nullable=True))
        batch_op.alter_column('id',
               existing_type=sa.NUMERIC(),
               type_=sa.Integer(),
               nullable=False,
               autoincrement=True)

    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_constraint('member_of_project', type_='foreignkey')
        batch_op.drop_column('member_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('member_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('member_of_project', 'member', ['member_id'], ['id'])

    with op.batch_alter_table('member', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.Integer(),
               type_=sa.NUMERIC(),
               nullable=True,
               autoincrement=True)
        batch_op.drop_column('name')

    # ### end Alembic commands ###

"""Initial migration.

Revision ID: 7b509e012abe
Revises: 
Create Date: 2021-11-10 12:56:16.630672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b509e012abe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('email_db', sa.Column('time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('email_db', 'time')
    # ### end Alembic commands ###

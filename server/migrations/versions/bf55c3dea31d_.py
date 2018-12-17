"""empty message

Revision ID: bf55c3dea31d
Revises: ca9375d25ad6
Create Date: 2018-12-17 23:47:54.735338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf55c3dea31d'
down_revision = 'ca9375d25ad6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('email', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'email')
    # ### end Alembic commands ###

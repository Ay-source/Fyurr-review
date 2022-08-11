"""empty message

Revision ID: f7c3c501b018
Revises: 06a73d229da4
Create Date: 2022-08-11 02:11:10.113821

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f7c3c501b018'
down_revision = '06a73d229da4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', postgresql.ARRAY(sa.VARCHAR(length=120)), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
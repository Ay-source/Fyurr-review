"""empty message

Revision ID: a1008ab39021
Revises: 5227b578d948
Create Date: 2022-08-10 21:29:10.938660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1008ab39021'
down_revision = '5227b578d948'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website_link', sa.String(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('Venue', sa.Column('website_link', sa.String(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'website_link')
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'website_link')
    # ### end Alembic commands ###

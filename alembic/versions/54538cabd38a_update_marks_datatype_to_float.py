"""update marks datatype to Float

Revision ID: 54538cabd38a
Revises: fcf95c979fb7
Create Date: 2021-06-14 00:23:47.214849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54538cabd38a'
down_revision = 'fcf95c979fb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('certifications',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('provider', sa.String(), nullable=True),
    sa.Column('marks', sa.Float(), nullable=True),
    sa.Column('max_marks', sa.Float(), nullable=True),
    sa.Column('basicdetails_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['basicdetails_id'], ['basic_details.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('education',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('period_from', sa.Date(), nullable=True),
    sa.Column('period_to', sa.Date(), nullable=True),
    sa.Column('degree', sa.String(), nullable=True),
    sa.Column('institute', sa.String(), nullable=True),
    sa.Column('university', sa.String(), nullable=True),
    sa.Column('marks', sa.Float(), nullable=True),
    sa.Column('max_marks', sa.Float(), nullable=True),
    sa.Column('basicdetails_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['basicdetails_id'], ['basic_details.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('education')
    op.drop_table('certifications')
    # ### end Alembic commands ###

"""added "URLMap" model

Revision ID: dc0d77f2ca15
Revises: 
Create Date: 2023-10-16 23:13:05.929565

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'dc0d77f2ca15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('url_map',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original', sa.String(length=256), nullable=False),
    sa.Column('short', sa.String(length=16), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('url_map')
    # ### end Alembic commands ###
"""add columns

Revision ID: b2a2004fd427
Revises: bc8d86570b46
Create Date: 2024-07-22 15:23:24.997732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2a2004fd427'
down_revision = 'bc8d86570b46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'plants', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'plants', type_='unique')
    # ### end Alembic commands ###

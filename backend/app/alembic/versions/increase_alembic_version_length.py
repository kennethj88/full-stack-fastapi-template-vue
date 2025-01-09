"""Increase alembic_version column length

Revision ID: increase_alembic_version_length
Revises: 1a31ce608336
Create Date: 2024-01-09 01:20:15.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'increase_alembic_version_length'
down_revision = '1a31ce608336'
branch_labels = None
depends_on = None


def upgrade():
    # Increase the length of version_num column in alembic_version table
    op.alter_column('alembic_version', 'version_num',
               existing_type=sa.String(32),
               type_=sa.String(255),
               existing_nullable=False)


def downgrade():
    op.alter_column('alembic_version', 'version_num',
               existing_type=sa.String(255),
               type_=sa.String(32),
               existing_nullable=False) 
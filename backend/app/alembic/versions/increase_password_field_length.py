"""Increase password field length

Revision ID: increase_password_field_length
Revises: 1a31ce608336
Create Date: 2024-01-09 01:16:14.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'increase_password_field_length'
down_revision = 'increase_alembic_version_length'  # Point to the new migration
branch_labels = None
depends_on = None


def upgrade():
    # Increase the length of the hashed_password field
    op.alter_column('user', 'hashed_password',
               existing_type=sa.String(32),
               type_=sa.String(255),
               existing_nullable=False)


def downgrade():
    # Revert the length of the hashed_password field
    # Note: This might fail if there are passwords longer than 32 characters
    op.alter_column('user', 'hashed_password',
               existing_type=sa.String(255),
               type_=sa.String(32),
               existing_nullable=False) 
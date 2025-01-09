"""Add base model columns to existing tables

Revision ID: add_base_model_columns_to_existing
Revises: create_social_account_table
Create Date: 2024-01-09 01:13:08.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_base_model_columns_to_existing'
down_revision = 'create_social_account_table'
branch_labels = None
depends_on = None


def upgrade():
    # Add created_at and updated_at columns to user table
    op.add_column('user', sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')))
    op.add_column('user', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')))

    # Add created_at and updated_at columns to item table
    op.add_column('item', sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')))
    op.add_column('item', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')))

    # Create trigger function if it doesn't exist
    op.execute("""
    CREATE OR REPLACE FUNCTION update_updated_at_column()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.updated_at = now();
        RETURN NEW;
    END;
    $$ language 'plpgsql';
    """)

    # Create triggers for each table
    op.execute("""
    CREATE TRIGGER update_user_updated_at
        BEFORE UPDATE ON "user"
        FOR EACH ROW
        EXECUTE FUNCTION update_updated_at_column();
    """)

    op.execute("""
    CREATE TRIGGER update_item_updated_at
        BEFORE UPDATE ON item
        FOR EACH ROW
        EXECUTE FUNCTION update_updated_at_column();
    """)


def downgrade():
    # Drop triggers
    op.execute('DROP TRIGGER IF EXISTS update_user_updated_at ON "user"')
    op.execute('DROP TRIGGER IF EXISTS update_item_updated_at ON item')

    # Drop columns
    op.drop_column('user', 'updated_at')
    op.drop_column('user', 'created_at')
    op.drop_column('item', 'updated_at')
    op.drop_column('item', 'created_at') 
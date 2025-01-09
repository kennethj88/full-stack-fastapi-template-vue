"""Create social account table

Revision ID: create_social_account_table
Revises: increase_password_field_length
Create Date: 2024-01-09 01:11:29.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'create_social_account_table'
down_revision = 'increase_password_field_length'
branch_labels = None
depends_on = None


def upgrade():
    # Create social_account table
    op.create_table(
        'social_account',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('provider', sa.String(50), nullable=False),
        sa.Column('provider_user_id', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
        sa.UniqueConstraint('provider', 'provider_user_id', name='uq_provider_provider_user_id')
    )

    # Create trigger for updating updated_at
    op.execute("""
    CREATE OR REPLACE FUNCTION update_updated_at_column()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.updated_at = now();
        RETURN NEW;
    END;
    $$ language 'plpgsql';
    """)

    op.execute("""
    CREATE TRIGGER update_social_account_updated_at
        BEFORE UPDATE ON social_account
        FOR EACH ROW
        EXECUTE FUNCTION update_updated_at_column();
    """)


def downgrade():
    op.drop_table('social_account') 
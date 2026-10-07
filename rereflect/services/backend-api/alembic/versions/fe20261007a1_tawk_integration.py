"""Owner-scoped tawk.to connections with database-unique property ownership."""
from alembic import op
import sqlalchemy as sa

revision = "fe20261007a1"
down_revision = "fe20261006a1"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("tawk_integrations",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("organization_id", sa.Integer(), sa.ForeignKey("organizations.id"), nullable=False, unique=True),
        sa.Column("property_id", sa.String(24), nullable=False, unique=True),
        sa.Column("source_id", sa.Integer(), sa.ForeignKey("feedback_sources.id", ondelete="CASCADE"), nullable=False, unique=True),
        sa.Column("webhook_secret", sa.Text(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
    )


def downgrade():
    op.drop_table("tawk_integrations")

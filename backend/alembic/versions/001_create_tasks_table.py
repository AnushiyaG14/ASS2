from alembic import op
import sqlalchemy as sa

revision = "001"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("type", sa.String, nullable=False),
        sa.Column("execution_time", sa.Integer, nullable=False),
        sa.Column("status", sa.String, nullable=False),
        sa.Column("attempts", sa.Integer, nullable=False),
        sa.Column("logs", sa.Text, nullable=False),
    )

def downgrade():
    op.drop_table("tasks")

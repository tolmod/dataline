"""rename_openai_columns_to_gemini

Revision ID: 6d16b920a3f0
Revises: ca20728c080d
Create Date: 2026-04-05 15:00:00.000000

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "6d16b920a3f0"
down_revision: Union[str, None] = "ca20728c080d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("PRAGMA foreign_keys=OFF;")
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.alter_column("openai_api_key", new_column_name="gemini_api_key")
        batch_op.alter_column("preferred_openai_model", new_column_name="preferred_model")
        batch_op.alter_column("openai_base_url", new_column_name="api_base_url")
    op.execute("PRAGMA foreign_keys=ON;")


def downgrade() -> None:
    op.execute("PRAGMA foreign_keys=OFF;")
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.alter_column("gemini_api_key", new_column_name="openai_api_key")
        batch_op.alter_column("preferred_model", new_column_name="preferred_openai_model")
        batch_op.alter_column("api_base_url", new_column_name="openai_base_url")
    op.execute("PRAGMA foreign_keys=ON;")

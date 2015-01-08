"""Add api limit rate

Revision ID: 1f04eab41381
Revises: 26889be04d70
Create Date: 2014-10-02 13:28:48.362000

"""

# revision identifiers, used by Alembic.
revision = '1f04eab41381'
down_revision = '26889be04d70'


def upgrade():
    op.create_table('oauth2client_limits',

def downgrade():
    op.drop_table('oauth2client_limits')
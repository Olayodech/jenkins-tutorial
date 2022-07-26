"""adding product and customers

Revision ID: ce7031adeb20
Revises: 
Create Date: 2022-08-04 18:58:58.605298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce7031adeb20'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('first_name', sa.String(length=55), nullable=True),
    sa.Column('last_name', sa.String(length=55), nullable=True),
    sa.Column('address', sa.String(length=55), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customer_email'), 'customer', ['email'], unique=True)
    op.create_index(op.f('ix_customer_username'), 'customer', ['username'], unique=True)
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=125), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('price', sa.String(length=6), nullable=True),
    sa.Column('discount', sa.String(length=6), nullable=True),
    sa.Column('brand', sa.String(length=10), nullable=True),
    sa.Column('category', sa.String(length=10), nullable=True),
    sa.Column('image', sa.String(length=128), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_created_at'), 'product', ['created_at'], unique=False)
    op.create_index(op.f('ix_product_name'), 'product', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_name'), table_name='product')
    op.drop_index(op.f('ix_product_created_at'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_customer_username'), table_name='customer')
    op.drop_index(op.f('ix_customer_email'), table_name='customer')
    op.drop_table('customer')
    # ### end Alembic commands ###

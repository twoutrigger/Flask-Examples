"""new dataset

Revision ID: 859b02290720
Revises: 
Create Date: 2019-04-05 19:58:37.716478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '859b02290720'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_restaurants_address'), 'restaurants', ['address'], unique=False)
    op.create_index(op.f('ix_restaurants_cuisine'), 'restaurants', ['cuisine'], unique=False)
    op.create_index(op.f('ix_restaurants_name'), 'restaurants', ['name'], unique=False)
    op.create_index(op.f('ix_restaurants_new_cat'), 'restaurants', ['new_cat'], unique=False)
    op.create_index(op.f('ix_restaurants_new_postal'), 'restaurants', ['new_postal'], unique=False)
    op.create_index(op.f('ix_restaurants_new_time'), 'restaurants', ['new_time'], unique=False)
    op.create_index(op.f('ix_restaurants_review_count'), 'restaurants', ['review_count'], unique=False)
    op.create_index(op.f('ix_restaurants_stars'), 'restaurants', ['stars'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_restaurants_stars'), table_name='restaurants')
    op.drop_index(op.f('ix_restaurants_review_count'), table_name='restaurants')
    op.drop_index(op.f('ix_restaurants_new_time'), table_name='restaurants')
    op.drop_index(op.f('ix_restaurants_new_postal'), table_name='restaurants')
    op.drop_index(op.f('ix_restaurants_new_cat'), table_name='restaurants')
    op.drop_index(op.f('ix_restaurants_name'), table_name='restaurants')
    op.drop_index(op.f('ix_restaurants_cuisine'), table_name='restaurants')
    op.drop_index(op.f('ix_restaurants_address'), table_name='restaurants')
    # ### end Alembic commands ###

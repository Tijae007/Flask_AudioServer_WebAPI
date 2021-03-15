"""2021_03_15

Revision ID: 000001
Revises: 
Create Date: 2021-03-15 20:08:32.439309

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '000001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audiobooks',
                    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
                    sa.Column('title', sa.String(length=100), nullable=False),
                    sa.Column('author', sa.String(length=100), nullable=False),
                    sa.Column('narrator', sa.String(length=100), nullable=False),
                    sa.Column('duration', sa.INTEGER(), nullable=False),
                    sa.Column('upload_time', sa.DateTime(), nullable=False),
                    sa.CheckConstraint('duration >= 0', name=op.f('ck_audiobooks_duration_non_negative')),
                    sa.CheckConstraint('length(author) <= 100', name=op.f('ck_audiobooks_author_not_more_than_100')),
                    sa.CheckConstraint('length(narrator) <= 100',
                                       name=op.f('ck_audiobooks_narrator_not_more_than_100')),
                    sa.CheckConstraint('length(title) <= 100', name=op.f('ck_audiobooks_title_not_more_than_100')),
                    sa.CheckConstraint('upload_time >= CURRENT_DATE', name=op.f('ck_audiobooks_in_the_present')),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_audiobooks'))
                    )
    op.create_index(op.f('ix_audiobooks_author'), 'audiobooks', ['author'], unique=False)
    op.create_index(op.f('ix_audiobooks_narrator'), 'audiobooks', ['narrator'], unique=False)
    op.create_index(op.f('ix_audiobooks_title'), 'audiobooks', ['title'], unique=False)
    op.create_table('podcasts',
                    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('duration', sa.INTEGER(), nullable=False),
                    sa.Column('host', sa.String(length=100), nullable=False),
                    sa.Column('participants', sa.JSON(), nullable=True),
                    sa.Column('upload_time', sa.DateTime(), nullable=False),
                    sa.CheckConstraint('duration >= 0', name=op.f('ck_podcasts_duration_non_negative')),
                    sa.CheckConstraint('length(host) <= 100', name=op.f('ck_podcasts_host_not_more_than_100')),
                    sa.CheckConstraint('length(name) <= 100', name=op.f('ck_podcasts_name_not_more_than_100')),
                    sa.CheckConstraint('upload_time >= CURRENT_DATE', name=op.f('ck_podcasts_in_the_present')),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_podcasts'))
                    )
    op.create_index(op.f('ix_podcasts_host'), 'podcasts', ['host'], unique=False)
    op.create_index(op.f('ix_podcasts_name'), 'podcasts', ['name'], unique=True)
    op.create_table('songs',
                    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('duration', sa.INTEGER(), nullable=False),
                    sa.Column('upload_time', sa.DateTime(), nullable=False),
                    sa.CheckConstraint('duration >= 0', name=op.f('ck_songs_duration_non_negative')),
                    sa.CheckConstraint('length(name) <= 100', name=op.f('ck_songs_not_more_than_100')),
                    sa.CheckConstraint('upload_time >= CURRENT_DATE', name=op.f('ck_songs_in_the_present')),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_songs'))
                    )
    op.create_index(op.f('ix_songs_name'), 'songs', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_songs_name'), table_name='songs')
    op.drop_table('songs')
    op.drop_index(op.f('ix_podcasts_name'), table_name='podcasts')
    op.drop_index(op.f('ix_podcasts_host'), table_name='podcasts')
    op.drop_table('podcasts')
    op.drop_index(op.f('ix_audiobooks_title'), table_name='audiobooks')
    op.drop_index(op.f('ix_audiobooks_narrator'), table_name='audiobooks')
    op.drop_index(op.f('ix_audiobooks_author'), table_name='audiobooks')
    op.drop_table('audiobooks')
    # ### end Alembic commands ###
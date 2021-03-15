BEGIN;

CREATE TABLE alembic_version
(
    version_num VARCHAR(32) NOT NULL,
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 000001

CREATE TABLE audiobooks
(
    id          BIGSERIAL    NOT NULL,
    title       VARCHAR(100) NOT NULL,
    author      VARCHAR(100) NOT NULL,
    narrator    VARCHAR(100) NOT NULL,
    duration    INTEGER      NOT NULL,
    upload_time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    CONSTRAINT pk_audiobooks PRIMARY KEY (id),
    CONSTRAINT ck_audiobooks_duration_non_negative CHECK (duration >= 0),
    CONSTRAINT ck_audiobooks_author_not_more_than_100 CHECK (length(author) <= 100),
    CONSTRAINT ck_audiobooks_narrator_not_more_than_100 CHECK (length(narrator) <= 100),
    CONSTRAINT ck_audiobooks_title_not_more_than_100 CHECK (length(title) <= 100),
    CONSTRAINT ck_audiobooks_in_the_present CHECK (upload_time >= CURRENT_DATE)
);

CREATE
INDEX ix_audiobooks_author ON audiobooks (author);

CREATE
INDEX ix_audiobooks_narrator ON audiobooks (narrator);

CREATE
INDEX ix_audiobooks_title ON audiobooks (title);

CREATE TABLE podcasts
(
    id           BIGSERIAL    NOT NULL,
    name         VARCHAR(100) NOT NULL,
    duration     INTEGER      NOT NULL,
    host         VARCHAR(100) NOT NULL,
    participants JSON,
    upload_time  TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    CONSTRAINT pk_podcasts PRIMARY KEY (id),
    CONSTRAINT ck_podcasts_duration_non_negative CHECK (duration >= 0),
    CONSTRAINT ck_podcasts_host_not_more_than_100 CHECK (length(host) <= 100),
    CONSTRAINT ck_podcasts_name_not_more_than_100 CHECK (length(name) <= 100),
    CONSTRAINT ck_podcasts_in_the_present CHECK (upload_time >= CURRENT_DATE)
);

CREATE
INDEX ix_podcasts_host ON podcasts (host);

CREATE
UNIQUE INDEX ix_podcasts_name ON podcasts (name);

CREATE TABLE songs
(
    id          BIGSERIAL    NOT NULL,
    name        VARCHAR(100) NOT NULL,
    duration    INTEGER      NOT NULL,
    upload_time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    CONSTRAINT pk_songs PRIMARY KEY (id),
    CONSTRAINT ck_songs_duration_non_negative CHECK (duration >= 0),
    CONSTRAINT ck_songs_not_more_than_100 CHECK (length(name) <= 100),
    CONSTRAINT ck_songs_in_the_present CHECK (upload_time >= CURRENT_DATE)
);

CREATE
UNIQUE INDEX ix_songs_name ON songs (name);

INSERT INTO alembic_version (version_num)
VALUES ('000001');

COMMIT;


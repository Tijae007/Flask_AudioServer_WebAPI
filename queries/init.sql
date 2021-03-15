-- creates the user, database and pg_stat_statements
CREATE USER audiodb WITH PASSWORD 'cxMlZ4yjw62YZ1JP0DJLqPLec';
CREATE DATABASE audiodb OWNER audiodb;
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

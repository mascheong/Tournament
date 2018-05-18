-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Drop tables if they exist (for unit testing)

drop database if exists tournament;
create database tournament;

\c tournament;

drop table if exists players;
drop table if exists matches;

-- Create tables
create table players (
  id serial primary key,
  name text
);

create table matches (
  m_id serial primary key,
  winner int references players(id),
  loser int references players(id)
);

-- Create views for total wins and total losses
create view wins as (
  select p.id, p.name, count(m.winner) as wins
  from players p left join matches m
  on p.id = m.winner
  group by p.id, p.name
  order by wins desc
);

create view losses as (
  select p.id, p.name, count(m.loser) as losses
  from players p left join matches m
  on p.id = m.loser
  group by p.id, p.name
  order by losses desc
);

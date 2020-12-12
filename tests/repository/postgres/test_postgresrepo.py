import pytest
from rentomatic.repository.postgres_objects import Room
from rentomatic.repository import postgresrepo

pytestmark = pytest.mark.slowtest


def test_dummy(pg_session):
    assert len(pg_session.query(Room).all()) == 4


def test_repository_list_without_parameters(docker_setup, pg_data, pg_session):
    repo = postgresrepo.PostgresRepo(docker_setup["postgres"])

    repo_rooms = repo.list()

    assert set([r.code for r in repo_rooms]) == set(r["code"] for r in pg_data)

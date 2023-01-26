from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for dict in result:
        assert all(
            key in dict.keys()
            for key in ("title", "salary", "type")
        )

import pytest
from datetime import datetime
from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "min_salary": 0,
            "max_salary": 1000,
            "date_posted": datetime(2022, 1, 23)
        },
        {
            "min_salary": 1000,
            "max_salary": 3000,
            "date_posted": datetime(2022, 1, 23)
        },
        {
            "min_salary": None,
            "max_salary": None,
            "date_posted": datetime(2022, 1, 23)
        },
        {
            "min_salary": 400,
            "max_salary": 8000,
            "date_posted": datetime(2022, 1, 23)
        },
    ]
    jobs_min_salary = [jobs[0], jobs[3], jobs[1], jobs[2]]
    jobs_max_salary = [jobs[3], jobs[1], jobs[0], jobs[2]]

    sort_by(jobs, "min_salary")
    assert jobs == jobs_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == jobs_max_salary

    with pytest.raises(TypeError):
        sort_by()
        sort_by(jobs)

    with pytest.raises(ValueError):
        sort_by(jobs, "")
        sort_by(jobs, "salario")

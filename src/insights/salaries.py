from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    max_salaries = [int(job["max_salary"])
                    for job in jobs_list
                    if job["max_salary"].isnumeric()]
    return max(max_salaries)


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    min_salaries = [int(job["min_salary"])
                    for job in jobs_list
                    if job["min_salary"].isnumeric()]
    return min(min_salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        salary = int(salary)
        for key in ["min_salary", "max_salary"]:
            job[key] = int(job[key])
        if job["min_salary"] > job["max_salary"]:
            raise ValueError
    except (ValueError, TypeError, KeyError):
        raise ValueError
    return salary >= job["min_salary"] and salary <= job["max_salary"]


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError

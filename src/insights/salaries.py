from copy import deepcopy
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
    job_copy = deepcopy(job)
    try:
        salary = int(salary)
        for key in ["min_salary", "max_salary"]:
            job_copy[key] = int(job_copy[key])
        if job_copy["min_salary"] > job_copy["max_salary"]:
            raise ValueError
    except (ValueError, TypeError, KeyError):
        raise ValueError
    return (salary >= job_copy["min_salary"]
            and salary <= job_copy["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass
    return filtered_jobs

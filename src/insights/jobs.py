import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        return [row for row in csv_reader]


def get_unique_job_types(path: str) -> List[str]:
    jobs_list = read(path)
    job_types = []
    for job in jobs_list:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]

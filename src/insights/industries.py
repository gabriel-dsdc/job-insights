from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_list = read(path)
    industries = []
    for job in jobs_list:
        if job["industry"] not in industries and job["industry"]:
            industries.append(job["industry"])
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job["industry"] == industry]

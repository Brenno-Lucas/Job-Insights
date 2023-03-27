from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=',')
        arr = []
        for line in reader:
            arr.append(line)
        return arr


def get_unique_job_types(path: str) -> List[str]:
    read_jobs = read(path)
    arr = set([job["job_type"] for job in read_jobs])
    return arr


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_by_type = []
    for arr_jobs in jobs:
        if arr_jobs['job_type'] == job_type:
            jobs_by_type.append(arr_jobs)
    return(jobs_by_type)

from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    read_jobs = read(path)
    arr_industry = set([
        industry['industry']
        for industry in read_jobs if
        industry['industry'] != ''])
    return arr_industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_industry = []
    for arr_industry in jobs:
        if arr_industry['industry'] == industry:
            filtered_industry.append(arr_industry)
    return(filtered_industry)

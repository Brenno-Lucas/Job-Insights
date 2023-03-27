from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    read_jobs = read(path)
    arr_max_salary = set([
        int(max_salary['max_salary'])
        for max_salary in read_jobs
        if max_salary['max_salary'].isnumeric()])
    return(max(arr_max_salary))


def get_min_salary(path: str) -> int:
    read_jobs = read(path)
    arr_min_salary = set([
        int(min_salary['min_salary'])
        for min_salary in read_jobs
        if min_salary['min_salary'].isnumeric()])
    return(min(arr_min_salary))


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError('Não possui a key')
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
    except TypeError:
        raise ValueError("Valor inválido")
    else:
        if min_salary > max_salary:
            raise ValueError("Valor mínimo é maior que o máximo")
        return min_salary <= salary <= max_salary


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

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Generator

employee_working_hours_pattern = re.compile(r"(.+) (\d+)")


@dataclass
class EmployeeWorkingHours:
    employee_name: str
    total_hours: int
    hours_list: list

    def __eq__(self, other):
        if other is None:
            return False

        if isinstance(other, EmployeeWorkingHours):
            return self.employee_name == other.employee_name

        return False

    def __hash__(self):
        return hash(self.employee_name)

    def __str__(self):
        return f"{self.employee_name}: {', '.join(map(str, self.hours_list))}; sum: {self.total_hours}"

    def __add__(self, other):
        if other is None:
            return

        if isinstance(other, EmployeeWorkingHours):
            self.total_hours += self.total_hours
            self.hours_list.extend(other.hours_list)
        return self

    @staticmethod
    def build(value: str) -> "EmployeeWorkingHours":
        match = re.match(employee_working_hours_pattern, value)
        if match:
            name = match.group(1)
            hours = match.group(2)
            return EmployeeWorkingHours(
                employee_name=name,
                total_hours=int(hours),
                hours_list=[hours]
            )
        else:
            raise ValueError("Invalid format")

    @staticmethod
    def open(path: Path) -> Generator["EmployeeWorkingHours", None, None]:
        with path.open('r', encoding='utf-8') as file:
            for line in file:
                yield EmployeeWorkingHours.build(line.strip())


class EmployeeWorkingHoursReport:
    def __init__(self, path: Path):
        self.path = path
        self.data: dict[str, EmployeeWorkingHours] = {}

    def build(self):
        for employee_working_hours in EmployeeWorkingHours.open(self.path):
            name = employee_working_hours.employee_name
            existing_hours = self.data.get(name)
            if existing_hours is None:
                self.data[name] = employee_working_hours
            else:
                self.data[name] = existing_hours + employee_working_hours

    def save_in_file(self, path: Path):
        with path.open('w', encoding='utf-8') as file:
            file.write(str(self))

    def __str__(self):
        return "\n".join(map(str, self.data.values()))

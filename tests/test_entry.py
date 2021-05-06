import pytest
from datetime import datetime, timezone

from todayi.core import Entry

@pytest.fixture
def entry():
    yield Entry()

@pytest.mark.unit
def test_creation(entry):
    assert entry.created == entry.edited
    assert entry.unique_tasks == 0

    with pytest.raises(AttributeError):
        entry.created = datetime.now(timezone.utc)
        entry.edited = datetime.now(timezone.utc)
        entry.unique_property = 1

@pytest.mark.bad
def test_add_task(entry):
    entry.add("taskA")

    print(entry.unique_tasks)

    assert entry.unique_tasks == 1
    assert entry.summary() == "taskA: x1"



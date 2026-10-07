"""Retired work cannot enter the worker registry or generic event dispatch."""
from unittest.mock import MagicMock
import pytest
from src.celery_app import celery_app
RETIRED=("salesforce","intercom","zendesk")

def test_retired_task_modules_and_schedules_absent():
    tasks=[*celery_app.conf.include,*[v["task"] for v in celery_app.conf.beat_schedule.values()]]
    assert not [t for t in tasks if any(p in t for p in RETIRED)]

@pytest.mark.parametrize("provider",RETIRED)
def test_generic_dispatch_skips_retired(provider):
    from src.tasks.source_events import _find_matching_sources
    db=MagicMock()
    assert _find_matching_sources(db,provider,{})==[]
    db.query.assert_not_called()

@pytest.mark.parametrize("provider",RETIRED)
def test_old_queued_source_cannot_import(provider):
    from src.tasks.source_events import _process_event_for_source
    db=MagicMock();source=MagicMock(id=123,organization_id=456,source_type=provider)
    assert _process_event_for_source(db,source,MagicMock(),"old-event","event",{})["status"]=="provider_retired"
    db.add.assert_not_called()

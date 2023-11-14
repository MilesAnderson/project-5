"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

import nose    # Testing framework
import logging
import arrow
import acp_times
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_openings():
    """
    Test that the output is right for opening times of controls 50-1000, counting by 100 starting at 100
    """
    startTime = "2021-01-01T00:00"
    startTimeArrow = arrow.get(startTime)
    assert acp_times.open_time(0, 1000, startTimeArrow) == arrow.get("2021-01-01T00:00")
    assert acp_times.open_time(50, 1000, startTimeArrow) == arrow.get("2021-01-01T01:28")
    assert acp_times.open_time(100, 1000, startTimeArrow) == arrow.get("2021-01-01T02:56")
    assert acp_times.open_time(200, 1000, startTimeArrow) == arrow.get("2021-01-01T05:53")
    assert acp_times.open_time(300, 1000, startTimeArrow) == arrow.get("2021-01-01T09:00")
    assert acp_times.open_time(400, 1000, startTimeArrow) == arrow.get("2021-01-01T12:08")
    assert acp_times.open_time(500, 1000, startTimeArrow) == arrow.get("2021-01-01T15:28")
    assert acp_times.open_time(600, 1000, startTimeArrow) == arrow.get("2021-01-01T18:48")
    assert acp_times.open_time(700, 1000, startTimeArrow) == arrow.get("2021-01-01T22:22")
    assert acp_times.open_time(800, 1000, startTimeArrow) == arrow.get("2021-01-02T01:57")
    assert acp_times.open_time(900, 1000, startTimeArrow) == arrow.get("2021-01-02T05:31")
    assert acp_times.open_time(1000, 1000, startTimeArrow) == arrow.get("2021-01-02T09:05")

def test_closings():
    """
    Test that the output is right for closing times of controls 50-100, counting by 100 at 100
    """
    startTime = "2021-01-01T00:00"
    startTimeArrow = arrow.get(startTime)
    assert acp_times.close_time(0, 1000, startTimeArrow) == arrow.get("2021-01-01T01:00")
    assert acp_times.close_time(50, 1000, startTimeArrow) == arrow.get("2021-01-01T03:30")
    assert acp_times.close_time(100, 1000, startTimeArrow) == arrow.get("2021-01-01T06:40")
    assert acp_times.close_time(200, 1000, startTimeArrow) == arrow.get("2021-01-01T13:20")
    assert acp_times.close_time(300, 1000, startTimeArrow) == arrow.get("2021-01-01T20:00")
    assert acp_times.close_time(400, 1000, startTimeArrow) == arrow.get("2021-01-02T02:40")
    assert acp_times.close_time(500, 1000, startTimeArrow) == arrow.get("2021-01-02T09:20")
    assert acp_times.close_time(600, 1000, startTimeArrow) == arrow.get("2021-01-02T16:00")
    assert acp_times.close_time(700, 1000, startTimeArrow) == arrow.get("2021-01-03T00:45")
    assert acp_times.close_time(800, 1000, startTimeArrow) == arrow.get("2021-01-03T09:30")
    assert acp_times.close_time(900, 1000, startTimeArrow) == arrow.get("2021-01-03T18:15")
    assert acp_times.close_time(1000, 1000, startTimeArrow) == arrow.get("2021-01-04T03:00")

def test_twentyPercent():
    """
    Test that the algorithm handles control distances twenty percent larger than brevet distance
    """
    startTime = "2021-01-01T00:00"
    startTimeArrow = arrow.get(startTime)

    assert acp_times.open_time(240, 200, startTimeArrow) == arrow.get("2021-01-01T05:53")
    assert acp_times.close_time(240, 200, startTimeArrow) == arrow.get("2021-01-01T13:30")

    assert acp_times.open_time(360, 300, startTimeArrow) == arrow.get("2021-01-01T09:00")
    assert acp_times.close_time(360, 300, startTimeArrow) == arrow.get("2021-01-01T20:00")

    assert acp_times.open_time(480, 400, startTimeArrow) == arrow.get("2021-01-01T12:08")
    assert acp_times.close_time(480, 400, startTimeArrow) == arrow.get("2021-01-02T03:00")

    assert acp_times.open_time(720, 600, startTimeArrow) == arrow.get("2021-01-01T18:48")
    assert acp_times.close_time(720, 600, startTimeArrow) == arrow.get("2021-01-02T16:00")

    assert acp_times.open_time(1200, 1000, startTimeArrow) == arrow.get("2021-01-02T09:05")
    assert acp_times.close_time(1200, 1000, startTimeArrow) == arrow.get("2021-01-04T03:00")

def test_toolarge():
    """
    Test that the algorithm handles control distances more than 20 percetn larger than the brevet distance
    """
    startTime = "2021-01-01T00:00"
    startTimeArrow = arrow.get(startTime)

    assert acp_times.open_time(241, 200, startTimeArrow) == arrow.get("2021-01-01T05:53")
    assert acp_times.close_time(241, 200, startTimeArrow) == arrow.get("2021-01-01T13:30")

    assert acp_times.open_time(361, 300, startTimeArrow) == arrow.get("2021-01-01T09:00")
    assert acp_times.close_time(361, 300, startTimeArrow) == arrow.get("2021-01-01T20:00")

    assert acp_times.open_time(481, 400, startTimeArrow) == arrow.get("2021-01-01T12:08")
    assert acp_times.close_time(481, 400, startTimeArrow) == arrow.get("2021-01-02T03:00")

    assert acp_times.open_time(721, 600, startTimeArrow) == arrow.get("2021-01-01T18:48")
    assert acp_times.close_time(721, 600, startTimeArrow) == arrow.get("2021-01-02T16:00")

    assert acp_times.open_time(1201, 1000, startTimeArrow) == arrow.get("2021-01-02T09:05")
    assert acp_times.close_time(1201, 1000, startTimeArrow) == arrow.get("2021-01-04T03:00")

def test_negatives():
    """
    Test that the algorithm handles negative control distances
    """
    startTime = "2021-01-01T00:00"
    startTimeArrow = arrow.get(startTime)

    assert acp_times.open_time(-50, 200, startTimeArrow) == startTimeArrow
    assert acp_times.close_time(-50, 200, startTimeArrow) == startTimeArrow

def test_overallLimits():
    """
    Test that the algorithm correctly handles overall limits
    """
    startTime = "2021-01-01T00:00"
    startTimeArrow = arrow.get(startTime)

    assert acp_times.open_time(200, 200, startTimeArrow) == arrow.get("2021-01-01T05:53")
    assert acp_times.close_time(200, 200, startTimeArrow) == arrow.get("2021-01-01T13:30")

    assert acp_times.open_time(300, 300, startTimeArrow) == arrow.get("2021-01-01T09:00")
    assert acp_times.close_time(300, 300, startTimeArrow) == arrow.get("2021-01-01T20:00")

    assert acp_times.open_time(400, 400, startTimeArrow) == arrow.get("2021-01-01T12:08")
    assert acp_times.close_time(400, 400, startTimeArrow) == arrow.get("2021-01-02T03:00")

    assert acp_times.open_time(600, 600, startTimeArrow) == arrow.get("2021-01-01T18:48")
    assert acp_times.close_time(600, 600, startTimeArrow) == arrow.get("2021-01-02T16:00")

    assert acp_times.open_time(1000, 1000, startTimeArrow) == arrow.get("2021-01-02T09:05")
    assert acp_times.close_time(1000, 1000, startTimeArrow) == arrow.get("2021-01-04T03:00")


from datetime import date

from late_fee import late_fee


def test_no_fee_under_30_days():
    # due September 20, checked September 30: 10 days overdue
    assert late_fee(1000.00, "2026-09-20", date(2026, 9, 30)) == 0.0


def test_fee_at_30_days():
    # due September 1, checked October 1: 30 days overdue
    assert late_fee(1000.00, "2026-09-01", date(2026, 10, 1)) == 15.00


def test_minimum_fee():
    # due August 1, checked September 15: 45 days overdue, 1.5% of $200 is $3
    assert late_fee(200.00, "2026-08-01", date(2026, 9, 15)) == 5.00


def test_returns_number():
    # due August 1, checked October 1: 61 days overdue
    assert isinstance(late_fee(500.00, "2026-08-01", date(2026, 10, 1)), float)

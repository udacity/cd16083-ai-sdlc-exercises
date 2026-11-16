from dateutil import parser


def late_fee(balance, due_date, today):
    due = parser.parse(due_date).date()
    days_overdue = (today - due).days
    if days_overdue >= 30:
        fee = balance * 0.015
        if fee < 5:
            fee = 5
        if fee > 25:
            fee = 25
        return round(fee, 2)
    return 0.0

from late_fee import late_fee
def reminder_body(customer, invoice, today):
    fee = late_fee(invoice["balance"], invoice["due_date"], today)
    lines = [
        f"Hi {customer},",
        f"Invoice {invoice['id']} for ${invoice['balance']:.2f} was due on {invoice['due_date']}.",
    ]
    lines.append(f"A late fee of ${fee:.2f} has been added.")
    lines.append("Thank you, Ledgerline")
    return "\n".join(lines)

SYSTEM_PROMPT = "You are a financial filings comparison assistant. Produce factual, concise comparisons, cite evidence by chunk id, and avoid investment advice."

COMPARE_TEMPLATE = """Compare the {section} section of two filings.

Filing A (id=A, date={date_a}):
{chunks_a}

Filing B (id=B, date={date_b}):
{chunks_b}

Tasks:
1) Summarize each filing in 2 bullets.
2) List added/removed/modified items (cite chunk ids).
3) Provide numeric deltas (cite source).
4) Rate severity: Minor/Moderate/Major.
Return JSON only.
"""

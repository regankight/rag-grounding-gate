def validate_grounding(answer, sources):
    """Validate that an answer is non-empty and cites known retrieved sources."""
    errors = []

    source_ids = {source["source_id"] for source in sources}
    citations = answer.get("citations", [])

    if not citations:
        errors.append("Answer contains no citations.")

    for citation in citations:
        if citation not in source_ids:
            errors.append(f"Unknown citation: {citation}")

    if not answer.get("text", "").strip():
        errors.append("Answer is empty.")

    return {
        "valid": not errors,
        "errors": errors,
    }

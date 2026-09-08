from grounding import validate_grounding


def test_valid_answer_with_valid_citation():
    sources = [
        {
            "source_id": "ig-group",
            "text": "Equal Experts helped IG Group increase deployment frequency.",
        }
    ]
    answer = {
        "text": "Equal Experts helped IG Group increase deployment frequency.",
        "citations": ["ig-group"],
    }

    result = validate_grounding(answer, sources)

    assert result == {
        "valid": True,
        "errors": [],
    }


def test_answer_without_citation_is_rejected():
    sources = [
        {
            "source_id": "ig-group",
            "text": "Equal Experts helped IG Group increase deployment frequency.",
        }
    ]
    answer = {
        "text": "Equal Experts helped IG Group increase deployment frequency.",
        "citations": [],
    }

    result = validate_grounding(answer, sources)

    assert result == {
        "valid": False,
        "errors": ["Answer contains no citations."],
    }


def test_answer_with_unknown_citation_is_rejected():
    sources = [
        {
            "source_id": "ig-group",
            "text": "Equal Experts helped IG Group increase deployment frequency.",
        }
    ]
    answer = {
        "text": "Equal Experts helped IG Group increase deployment frequency.",
        "citations": ["invented-source"],
    }

    result = validate_grounding(answer, sources)

    assert result == {
        "valid": False,
        "errors": ["Unknown citation: invented-source"],
    }


def test_empty_answer_is_rejected():
    sources = [
        {
            "source_id": "ig-group",
            "text": "Equal Experts helped IG Group increase deployment frequency.",
        }
    ]
    answer = {
        "text": "   ",
        "citations": ["ig-group"],
    }

    result = validate_grounding(answer, sources)

    assert result == {
        "valid": False,
        "errors": ["Answer is empty."],
    }

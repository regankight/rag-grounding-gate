# RAG Grounding Gate — Lightweight validation layer for grounded LLM responses

A small Python reliability component that validates generated answers against
retrieved source IDs before allowing them downstream.

It demonstrates citation enforcement, provenance checking, explicit failure
handling, and unit-tested GenAI output validation.

## Requirements

- Python 3.10+
- pytest

## Installation

Clone the repository:

```bash
git clone https://github.com/regankight/rag-grounding-gate.git
cd rag-grounding-gate
```

Install the test dependency:

```bash
python -m pip install pytest
```

Run the tests:

```bash
pytest
```

## Why this exists

A generated answer should not automatically become trusted application output.

```text
retrieved evidence
        ↓
      LLM
        ↓
 candidate answer
        ↓
GROUNDING GATE
        ↓
 accept / reject + reasons
```

The key design idea is:

```text
generation != trusted output

generation
    ↓
validation
    ↓
application
```

This project intentionally does **not** attempt semantic hallucination
detection. It only enforces a few simple, explicit output constraints.

## Checks

`validate_grounding(answer, sources)` rejects an answer when:

- it has no citations;
- it cites a source ID that was not retrieved;
- its answer text is empty.

## Example

```python
from grounding import validate_grounding

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

print(result)
# {"valid": True, "errors": []}
```

An answer with an invented citation is rejected:

```python
answer = {
    "text": "Equal Experts helped IG Group increase deployment frequency.",
    "citations": ["made-up-source"],
}

print(validate_grounding(answer, sources))
# {
#     "valid": False,
#     "errors": ["Unknown citation: made-up-source"]
# }
```

## Run the tests

Install pytest if needed:

```bash
python -m pip install pytest
```

Then run:

```bash
pytest
```

The test suite covers exactly four cases:

1. valid answer with a valid citation;
2. answer with no citation;
3. answer with an invented citation;
4. empty answer.

## Project structure

```text
rag-grounding-gate/
├── grounding.py
├── test_grounding.py
└── README.md
```

## Definition of done

```text
validator exists
+
4 tests pass
+
README explains why the gate exists
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

import json


def json_format(data: str) -> str:
    """
    Format JSON string with proper indentation.
    """
    return json.dumps(json.loads(data), indent=2, ensure_ascii=False)


def json_compress(data: str) -> str:
    """
    Compress JSON string by removing whitespace.
    """
    return json.dumps(json.loads(data), separators=(',', ':'), ensure_ascii=False)

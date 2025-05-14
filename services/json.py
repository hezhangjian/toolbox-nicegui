import json

def format_json(data: str) -> str:
    """Format JSON string with proper indentation."""
    return json.dumps(json.loads(data), indent=2, ensure_ascii=False)

def compress_json(data: str) -> str:
    """Compress JSON string by removing whitespace."""
    return json.dumps(json.loads(data), separators=(',', ':'), ensure_ascii=False)

def validate_json(data: str) -> tuple[bool, str]:
    """Validate JSON string and return (is_valid, error_message)."""
    try:
        json.loads(data)
        return True, "JSON格式正确"
    except json.JSONDecodeError as e:
        return False, f"JSON格式错误: {str(e)}" 

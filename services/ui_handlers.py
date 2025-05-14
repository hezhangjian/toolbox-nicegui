from nicegui import ui
from services.json import format_json, compress_json, validate_json

def handle_json_format(input_text, output_text):
    try:
        output_text.value = format_json(input_text.value)
        ui.notify('格式化成功', type='positive')
    except json.JSONDecodeError as e:
        ui.notify(f'JSON格式错误: {str(e)}', type='negative')

def handle_json_compress(input_text, output_text):
    try:
        output_text.value = compress_json(input_text.value)
        ui.notify('压缩成功', type='positive')
    except json.JSONDecodeError as e:
        ui.notify(f'JSON格式错误: {str(e)}', type='negative')

def handle_json_validate(input_text):
    is_valid, message = validate_json(input_text.value)
    ui.notify(message, type='positive' if is_valid else 'negative')

def clear_textareas(input_text, output_text):
    input_text.value = ''
    output_text.value = '' 

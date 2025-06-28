from nicegui import ui

import hashlib


def calculate_md5(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()


def render_md5():
    ui.label('MD5').classes('text-2xl font-bold mb-4')

    input_text = ui.input('Input Text', placeholder='Enter Text Here')
    output_text = ui.label('')

    def on_click():
        md5_hash = calculate_md5(input_text.value)
        output_text.set_text(f'MD5 Hash: {md5_hash}')

    ui.button('Calculate', on_click=on_click)

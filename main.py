from nicegui import ui
from services.ui_handlers import handle_json_format, handle_json_compress, handle_json_validate, clear_textareas


@ui.page('/tools/json-formatter')
def json_formatter():
    with ui.card().classes('w-full max-w-4xl mx-auto p-8'):
        ui.label('JSON格式化').classes('text-2xl font-bold mb-4')
        ui.label('JSON美化与验证工具').classes('text-gray-500 mb-8')

        with ui.row().classes('w-full gap-4'):
            with ui.column().classes('w-1/2'):
                ui.label('输入 JSON').classes('text-lg mb-2')
                input_text = ui.textarea().classes('w-full h-64')

            with ui.column().classes('w-1/2'):
                ui.label('格式化结果').classes('text-lg mb-2')
                output_text = ui.textarea().classes('w-full h-64')

        with ui.row().classes('w-full gap-4 mt-4'):
            ui.button('格式化', on_click=lambda: handle_json_format(input_text, output_text)).classes('bg-blue-500')
            ui.button('压缩', on_click=lambda: handle_json_compress(input_text, output_text)).classes('bg-green-500')
            ui.button('验证', on_click=lambda: handle_json_validate(input_text)).classes('bg-purple-500')
            ui.button('清空', on_click=lambda: clear_textareas(input_text, output_text)).classes('bg-gray-500')


@ui.page('/')
def home():
    tools = [
        {'icon': 'edit_note', 'title': 'JSON格式化', 'desc': 'JSON美化与验证工具', 'route': '/tools/json-formatter'},
        {'icon': 'lock', 'title': 'MD5', 'desc': 'MD5哈希计算工具'},
        {'icon': 'link', 'title': 'URL编码解码', 'desc': 'URL编码/解码转换'},
        {'icon': 'palette', 'title': 'HEX转换', 'desc': '进制转换工具'},
        {'icon': 'alarm', 'title': '时间戳转换', 'desc': '时间戳与日期转换'},
        {'icon': 'vpn_key', 'title': '华为云Token', 'desc': '获取华为云访问令牌'},
    ]
    with ui.element('div').classes('grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 p-8'):
        for tool in tools:
            with ui.card().classes(
                    'flex flex-col items-center p-8 rounded-xl shadow hover:shadow-lg transition cursor-pointer').on(
                'click', lambda t=tool: ui.navigate.to(t.get('route', '#'))):
                ui.icon(tool['icon'], size='48px').classes('mb-4')
                ui.label(tool['title']).classes('text-xl font-bold mb-2')
                ui.label(tool['desc']).classes('text-gray-500')


if __name__ == '__main__':
    ui.run(
        title='ChuQin ToolBox',
        favicon='🤖',
        dark=True,
        reload=False,
        show=True,
        port=8080
    )

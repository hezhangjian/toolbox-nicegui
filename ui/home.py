from nicegui import ui
from dataclasses import dataclass


@dataclass
class Tool:
    icon: str
    title: str
    desc: str
    route: str


def render_home():
    tools = [
        Tool(icon='palette', title='HEX转换', desc='进制转换工具', route='/hex'),
        Tool(icon='edit_note', title='JSON格式化', desc='JSON美化与验证工具', route='/json'),
        Tool(icon='lock', title='MD5', desc='MD5哈希计算工具', route='/md5'),
        Tool(icon='alarm', title='时间戳转换', desc='时间戳与日期转换', route='/time'),
        Tool(icon='link', title='URL编码解码', desc='URL编码/解码转换', route='/url-codec'),
    ]

    with ui.element('div').classes(
            'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-10 p-10 w-full max-w-7xl'):
        for tool in tools:
            with ui.card().classes(
                    'flex flex-col items-center p-10 rounded-2xl border border-gray-200 bg-white shadow-md hover:shadow-xl hover:scale-105 transition-all duration-200 cursor-pointer') \
                    .on('click', lambda t=tool: ui.navigate.to(t.route)):
                ui.icon(tool.icon, size='56px', color='primary').classes('mb-5')
                ui.label(tool.title).classes('text-2xl font-bold mb-2 text-gray-900')
                ui.label(tool.desc).classes('text-gray-600')

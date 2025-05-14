from nicegui import ui

from ui.hex import render_hex
from ui.home import render_home
from ui.json import render_json
from ui.md5 import render_md5
from ui.time import render_time
from ui.url_codec import render_url_codec


@ui.page('/')
def ui_home():
    render_home()


@ui.page('/json')
def ui_json():
    render_json()


@ui.page('/hex')
def ui_hex():
    render_hex()


@ui.page('/md5')
def ui_md5():
    render_md5()


@ui.page('/time')
def ui_time():
    render_time()


@ui.page('/url-codec')
def ui_url_codec():
    render_url_codec()


if __name__ == '__main__':
    ui.run(
        title='ChuQin ToolBox',
        favicon='🤖',
        dark=False,
        reload=False,
        show=True,
        port=8080
    )

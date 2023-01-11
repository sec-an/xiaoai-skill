import music_handler
from .sdk import xiaoai_request
from .response_handler import build_text_message, build_music_message
from music_handler import migu


def parse_input(event):
    req = xiaoai_request(event)
    if req.request.type == 0:
        return build_text_message('想听什么歌？', is_session_end=False, open_mic=True)
    elif req.request.type == 1:
        print(req.query)
        print(req.request.slot_info.intent_name)
        print(str(req.request.slot_info.slots))
        mp3_urls = migu.search(req.query)
        return build_music_message('马上播放歌曲', mp3_urls)
    elif req.request.type == 2:
        return build_text_message('拜拜', is_session_end=True, open_mic=False)
    else:
        return build_text_message('我没听懂欸', is_session_end=True, open_mic=False)
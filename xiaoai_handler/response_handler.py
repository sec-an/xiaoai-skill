from .sdk import (XiaoAIResponse,
                  XiaoAIToSpeak,
                  xiaoai_response,
                  XiaoAIOpenResponse,
                  XiaoAIDirective,
                  XiaoAITTSItem,
                  XiaoAIAudioItem,
                  XiaoAIStream)


# 文本回复
def build_text_message(to_speak, is_session_end, open_mic, not_understand=False):
    xiao_ai_response = XiaoAIResponse(
        not_understand=not_understand,
        to_speak=XiaoAIToSpeak(type_=0, text=to_speak),
        open_mic=open_mic)
    response = xiaoai_response(XiaoAIOpenResponse(version='1.0',
                                                  is_session_end=is_session_end,
                                                  response=xiao_ai_response))
    return response


# 音乐回复
def build_music_message(to_speak, mp3_urls, not_understand=False):
    all_list = []
    if to_speak is not None:
        info_tts = XiaoAIDirective(
            type_='tts',
            tts_item=XiaoAITTSItem(
                type_='0', text=to_speak
            ))

        all_list.append(info_tts)
    for url in mp3_urls:
        info_audio = XiaoAIDirective(
            type_='audio',
            audio_item=XiaoAIAudioItem(stream=XiaoAIStream(url=url))
        )
        all_list.append(info_audio)
    xiao_ai_response = XiaoAIResponse(directives=all_list, open_mic=False, not_understand=not_understand, )
    response = xiaoai_response(XiaoAIOpenResponse(
        version='1.0', is_session_end=True, response=xiao_ai_response))
    return response

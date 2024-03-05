import requests
from nakuru.entities.components import *
from nakuru import (
    GroupMessage,
    FriendMessage
)
from botpy.message import Message, DirectMessage
from cores.qqbot.global_object import (
    AstrMessageEvent,
    CommandResult
)


class Main:
    """
    初始化函数, 可以选择直接pass
    """
    def __init__(self) -> None:
        print("ATRI")

    async def run(self, ame: AstrMessageEvent):
        msg = ame.message_str
        url = f"http://api.soulter.top/atriproj/conversation?prompt={msg}&sid={ame.session_id}&json=true"
        resp = requests.get(url)
        #{
        #     "session_id": "107.172.132.177",
        #     "result": "初次见面夏生先生！我是亚托莉，超高兴认识你！我会一直陪伴你的，因为我是高性能的嘛！",
        #     "translated_result": "はじめまして夏生さん！私はアトリーです。お会いできて嬉しいです！私はずっとあなたと一緒にいます。私は高性能だからです！",
        #     "audio_url": "http://api.soulter.top/atriproj/audio_file?filename=tmp/2024-03-05-13-31-20.wav",
        #     "context_len": 4,
        #     "usage_tokens": 11832
        # }
        # await ame.gocq_platform.send_msg(ame.message_obj, [
            
        # ])
        return CommandResult(
            hit=True,
            success=True,
            message_chain=[Record(file=resp.json()['audio_url']),],
            command_name='atri'
        )

    
    def info(self):
        return {
            "name": "astrbot-plugin-atri",
            "desc": "笨蛋萝卜子",
            "help": "",
            "version": "v1.0",
            "author": "Soulter"
        }

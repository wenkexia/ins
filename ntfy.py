import requests
import json


def push_json(
    message,
    url,
    topic,
    title="通知",
    tags=None,
    priority=4,
    actions=None,
    click=None,
    attach=None,
    filename=None,
    delay=None,
    email=None,
):
    """
    @description: 推送消息到ntfy(https://ntfy.wenke.live/docs/subscribe/api/#json-message-format)
    @param topic: 消息标题
    @param message: 消息内容
    @param url：必须是ntfy 根 URL，而不是主题 URL
    @param title:
    @param tags: 标签，表情
    @param priority: 优先级
    @param actions:
    @param click: 点击通知
    @param attach: 附件
    @param filename:
    @param delay: 延时
    @param email: 邮件
    @return: Boolean
    """

    resp = requests.post(
        url,
        data=json.dumps(
            {
                "topic": topic,
                "title": title,  # 消息标题
                "message": message,  # 消息内容
                "tags": tags,
                "priority": priority,
                "actions": actions,
                "click": click,
                "attach": attach,  # 附件
                "filename": filename,
                "delay": delay,
                "email": email,
            }
        ),
    )
    if resp.status_code == 200:
        print(f"向主题{topic}推送成功")
        return True
    else:
        print(f"向主题{topic}推送失败")
        return False

import pytchat

import os


class ConnectComments:
    def __init__(self, video_id) -> None:
        self.chat = pytchat.create(video_id=video_id, interruptable=False)

    def get_comment(self):
        comments = self.__get_comments()
        if comments is None:
            return None
        message = comments[-1]
        print(message.message)
        return message.message

    def __get_comments(self):
        if self.chat.is_alive() is False:
            print('Streaming is not started')
            return None
        while self.chat.is_alive():
            print("Loading comments...")
            comments = list(self.chat.get().sync_items())
            if comments == []:
                print('Failed to load comments')
            else:
                return comments


if __name__ == '__main__':
    import time

    video_id = os.getenv('VIDEO_ID')
    chat = ConnectComments(video_id)
    time.sleep(1)
    print(chat.get_comment())

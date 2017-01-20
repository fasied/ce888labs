from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()
global average#=[0,0,0,0,0]
@module.rule('')
def hi(bot, trigger,):
    global average
    print(trigger, trigger.nick)
    #bot.say('Hi, ' + trigger.nick)
    str(trigger)
    list = emo.detect_emotion_in_raw_np(trigger)
    print(list)

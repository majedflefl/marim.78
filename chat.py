from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# إنشاء الروبوت
chatbot = ChatBot('TestBot')

# تدريب الروبوت
trainer = ChatterBotCorpusTrainer(chatbot)

# تدريب الروبوت باستخدام قاعدة بيانات ChatterBot المدمجة
trainer.train("chatterbot.corpus.english")

# اختبار الروبوت
response = chatbot.get_response("Hello, how are you?")
print(response)

while True:
    try:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print("Bot:", response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

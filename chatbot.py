# =====================================
# SUPER SMART AI STUDENT CHATBOT
# Mini Project - Python
# =====================================

import datetime

def greeting():
    print("==========================================")
    print("      🤖 SUPER SMART AI STUDENT CHATBOT")
    print("==========================================")
    print("Hello Student! I am here to chat and help you 😊")
    print("Type 'exit' anytime to end the chat.\n")


def chatbot_reply(user):

    # greetings
    if "hi" in user or "hello" in user:
        return "Hello! How are you today?"

    # exam stress + motivation (TAGDA WALA 😎)
    elif "exam" in user and "motivation" in user:
        return (
            "Achha batao 😏, tum shayad Ambani ke ladke ho kya?\n"
            "Isliye padhne ka motivation nahi aa raha?\n"
            "Socho zara — tier-3 college me mehnat karke aaye ho,\n"
            "aur ab exam ke time give up?\n"
            "Isse bada motivation kya chahiye bhai 💪🔥\n"
            "Utho, padhai karo aur khud par bharosa rakho!"
        )

    elif "exam najdik" in user or "exam paas" in user:
        return (
            "Exam paas aa gaya hai aur tension hona normal hai.\n"
            "Lekin yaad rakho — pressure me hi diamond banta hai 💎\n"
            "Thoda-thoda padho, consistency rakho, ho jayega 💪"
        )

    # feelings / health
    elif "sick" in user or "not well" in user or "ill" in user:
        return "Oh! Take care 😟. Please rest well and stay healthy."

    elif "sad" in user or "stress" in user:
        return "Stress lena easy hai, handle karna strong logon ka kaam 💪"

    # chatbot info
    elif "name" in user:
        return "I am a Super Smart AI Student Chatbot."

    elif "ai" in user:
        return "AI stands for Artificial Intelligence."

    # study related
    elif "college" in user:
        return "I am designed to help college students."

    elif "subject" in user:
        return "Subjects include Python, Data Structures, COA, etc."

    # motivation normal
    elif "motivate" in user or "motivation" in user:
        return "Discipline > Motivation. Start now, mood baad me ban jayega 🚀"

    # time & date
    elif "time" in user:
        return "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")

    elif "date" in user:
        return "Today's date is " + datetime.datetime.now().strftime("%d-%m-%Y")

    # thanks & bye
    elif "thank" in user:
        return "You're welcome 😊 Happy to help!"

    elif "bye" in user:
        return "Goodbye! Have a great day 👋"

    # help
    elif "help" in user:
        return "I can help with exams, stress, motivation, AI, time and more."

    else:
        return "Hmm 🤔 I didn't understand that. Try saying it differently."


# -------- MAIN PROGRAM --------
greeting()

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Bot: Thank you for chatting. Goodbye 👋")
        break

    response = chatbot_reply(user_input)
    print("Bot:", response)
    
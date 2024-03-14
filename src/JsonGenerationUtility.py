import json
Messages = []
ChatLogString = ""
while True:
    nickname = input("Nickname: ")
    text = input("Text: ")
    if nickname == "" or text == "":
        break
    ChatLogString += f"\n{nickname}: {text}"
Messages.append({"role": "user", "content": ChatLogString})

answer = input("Answer: ")
Messages.append({"role": "assistant", "content": answer})
with open("../GenerationTemplates/template.json", mode="a") as file:
    file.write(json.dumps(Messages))


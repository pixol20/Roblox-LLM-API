from transformers import AutoTokenizer, AutoModelForCausalLM
import json
MODEL_PATH = "../models/Llama-2-7b-chat-hf"
JSON_PATH = "../GenerationTemplates/template.json"
Model = None
Tokenizer = None

Template = []

def LoadModel():
    global Model
    global Tokenizer
    global Template
    Model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map="auto", load_in_4bit=True)
    Tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    Tokenizer.pad_token = Tokenizer.eos_token
    with open(JSON_PATH, 'rb') as file:
        Template = json.load(file)

def GenerateText(History):
    TemplatePlusHistory = Template
    TemplatePlusHistory.append(History)
    TokenizedChat = Tokenizer.apply_chat_template(TemplatePlusHistory, tokenize=True, add_generation_prompt=True, return_tensors="pt").to("cuda")
    GeneratedIds = Model.generate(TokenizedChat, max_new_tokens=50)
    print(Tokenizer.batch_decode(GeneratedIds, skip_special_tokens=True)[0])

LoadModel()
GenerateText({"role": "user", "content": "\nMaximous: Pixol, I'm so glad that our holidays start on 5th December\nPixol: Wow, that's great\nPixol: Hey, Pepe when do holidays start?"})
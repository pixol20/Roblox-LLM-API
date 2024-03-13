from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from torch import float16
import json
import numpy as np
# replace with your model
MODEL_PATH = "../models/Mistral-7B-Instruct-v0.2"
JSON_PATH = "../GenerationTemplates/template.json"
Model = None
Tokenizer = None

Template = []

def LoadModel():
    global Model
    global Tokenizer
    global Template
    quantization_config = BitsAndBytesConfig(llm_int8_enable_fp32_cpu_offload=True,
                                             bnb_4bit_compute_dtype=float16
                                             )
    Model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map='cuda', quantization_config=quantization_config)
    print(Model)
    Tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    Tokenizer.pad_token = Tokenizer.eos_token
    with open(JSON_PATH, 'rb') as file:
        Template = json.load(file)


def GenerateText(History):
    TokenizedChatLen = 0
    TokenizedChat = Tokenizer.apply_chat_template(np.concatenate((Template, History)), tokenize=True, add_generation_prompt=True, return_tensors="pt").to("cuda")
    InputLen = TokenizedChat.shape[1]
    GeneratedIds = Model.generate(TokenizedChat, max_new_tokens=30, pad_token_id=Tokenizer.eos_token_id, top_p=1, do_sample=True)
    Output = Tokenizer.batch_decode(GeneratedIds[:, InputLen:], skip_special_tokens=True)[0]
    return Output


def GenerateModelInput(messages):
    resultstring = ""
    for message in messages:
        nickname = message["nickname"]
        content = message["content"]
        resultstring += f"\n{nickname}: {content}"
    return [{"role": "user", "content": resultstring}]
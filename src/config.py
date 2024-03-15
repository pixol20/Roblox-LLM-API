from torch import bfloat16
config = {
  "Server":
  {
    "host": "127.0.0.1",
    "port": 8080
  },
  "Model":
  {
    "pretrained_model_name_or_path": "../models/Mistral-7B-Instruct-v0.2",
    "config": None,
    "cache_dir": None,
    "ignore_mismatched_sizes": False,
    "force_download": False,
    "local_files_only": False,
    "token": None,
    "revision": "main",
    "use_safetensors": None,
    "device_map": "cuda"
  },
  "Quantization":
  {
    "BitsAndBytesConfig":
    {
      "load_in_8bit": False,
      "load_in_4bit": False,
      "llm_int8_treshold": 6.0,
      "llm_int8_skip_modules": None,
      "llm_int8_enable_fp32_cpu_offload": True,
      "llm_int8_has_fp16_weight": False,
      "bnb_4bit_compute_dtype": bfloat16,
      "bnb_4bit_use_double_quant": False
    }
  },
  "Generation":
  {
    # generate() args
    "generation_config" : None,
    "logits_processor": None,
    "stopping_criteria": None,
    "prefix_allowed_tokens_fn": None,
    "synced_gpus": None,
    "assistant_model": None,
    "streamer": None,
    "negative_prompt_ids": None,
    "negative_prompt_attention_mask": None,
    # Generation config
    "max_length": None,
    "max_new_tokens": 50,
    "min_length": 0,
    "min_new_tokens": None,
    "early_stopping": False,
    "max_time": None,
    "do_sample": True,
    "num_beams": 1,
    "num_beam_groups": 1,
    "penalty_alpha": None,
    "use_cache": True,
    "temperature": 1.0,
    "top_k": 50,
    "top_p": 1.3,
    "typical_p": 1.0,
    "epsilon_cutoff": 0.0,
    "eta_cutoff": 0.0,
    "diversity_penalty": 0.0,
    "repetition_penalty": 1.0,
    "encoder_repetition_penalty": 1.0,
    "length_penalty": 1.0,
    "no_repeat_ngram_size": 0,
    "bad_words_ids": None,
    "force_words_ids": None,
    "renormalize_logits": False,
    "constraints": None,
    "exponential_decay_length_penalty": None,
    "suppress_tokens": None,
    "begin_suppress_tokens": None,
    "forced_decoder_ids": None,
    "sequence_bias": None,
    "guidance_scale": None,
    "low_memory": None,
    "num_return_sequences": 1,
    "output_attentions": False,
    "output_hidden_states": False,
    "output_scores": False,
    "output_logits": False,
    "return_dict_in_generate": False
  },
  "TemplateTokenization":
  {
    "chat_template": None,
    "add_generation_prompt": True,
    "tokenize": True,
    "padding": False,
    "truncation": False,
    "max_length": None,
    "return_tensors": "pt",
    "return_dict": False,
  }
}
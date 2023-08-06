from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig


class ChatBot:
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    config = GenerationConfig(max_new_tokens=200)

    def predict(self, input: str) -> str:
        tokens = self.tokenizer(input, return_tensors="pt")
        outputs = self.model.generate(**tokens, generation_config=self.config)
        return self.tokenizer.batch_decode(outputs, skip_special_tokens=True)

from transformers import BartForConditionalGeneration, BartTokenizer

def load_bart_model():
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    return model, tokenizer

if __name__ == "__main__":
    model, tokenizer = load_bart_model()
    # print("BART model and tokenizer loaded and cached successfully.")

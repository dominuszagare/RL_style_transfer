from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction

def calculate_bleu_score_from_ids(tokenizer_, input_ids_, labels_):
    input = tokenizer_.decode(input_ids_, skip_special_tokens=True)
    labels = tokenizer_.decode(labels_, skip_special_tokens=True)
    reference = labels.split()
    hypothesis = input.split()
    return sentence_bleu([reference], hypothesis, smoothing_function=SmoothingFunction().method1)

def evaluate_model_on_test_data(model_, tokenizer_, test_dataset_with_refrences_, device):
    model_.eval()
    encoding = tokenizer_([x["input"] for x in test_dataset_with_refrences_],
        padding="longest",
        max_length=512,
        truncation=True,
        return_tensors="pt")
    encoding = encoding.to(device)
    bleu_score = 0
    for i in range(0,len(test_dataset_with_refrences_)):
        refrence_strings = test_dataset_with_refrences_[i]['ref']
        input_ids = encoding['input_ids'][i]
        generated = model_.generate(input_ids=input_ids, attention_mask=encoding['attention_mask'][i], max_length=150, num_beams=5, early_stopping=True )
        
        generated_string = tokenizer_.decode(generated[0], skip_special_tokens=True)
        refrence_strings = [x.split() for x in refrence_strings]
        generated_string = generated_string.split()
        bleu_score += sentence_bleu(refrence_strings, generated_string, smoothing_function=SmoothingFunction().method1)

    return bleu_score / len(test_dataset_with_refrences_)



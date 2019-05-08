import torch
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM

def manual_mask(text, blank_token):
    toks = text.split(' ')
    for i in range(0, len(toks)):
        if i%6 == 1 and toks[i].isalpha():
            toks[i] = blank_token
    return ' '.join(toks)

def do_ai_madlib(text_with_blanks, blank_token):
    mask_token = '[MASK]'

    bert_version = 'bert-base-cased'
    model = BertForMaskedLM.from_pretrained(bert_version)
    tokenizer = BertTokenizer.from_pretrained(bert_version)

    tokens = tokenizer.tokenize(text_with_blanks)
    mask_idxs = []
    for i in range(0, len(tokens)):
        if tokens[i] == blank_token:
            tokens[i] = mask_token
            mask_idxs.append(i)

    model.eval()
    print(tokens)
    for i in mask_idxs:
        # convert tokens to their index in the "vocabulary"
        token_ids = tokenizer.convert_tokens_to_ids(tokens)
        # create a tensor for these indices
        tokens_tensor = torch.tensor([token_ids])
        preds = model(tokens_tensor)[0,i]
        pred_id = torch.argmax(preds).item()
        pred_token = tokenizer.convert_ids_to_tokens([pred_id])[0]
        tokens[i] = pred_token

    for i in mask_idxs:
        tokens[i] = '__' + tokens[i] + '__'
    return ' '.join(tokens).replace(' ##', '')

if __name__ == '__main__':
    with open('../frogking.txt', 'r') as f:
        para = ' '.join(list(map(str.strip, f.readlines())))
    para = manual_mask(para, '_')

    print(do_ai_madlib(para, '_'))

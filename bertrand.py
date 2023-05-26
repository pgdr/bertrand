import torch
from transformers import BertTokenizer, BertForMaskedLM
from transformers import pipeline
from collections import namedtuple
import readline


Prediction = namedtuple("Prediction", "score word sentence")


def pred(score, word, sentence):
    return Prediction(
        score=round(score * 100, 1), word=word, sentence=sentence
    )


def predict(text, pipe):
    if "[MASK]" not in text:
        text = text + " [MASK] [CLS]"
    return [
        pred(
            score=e["score"],
            word=e["token_str"],
            sentence=e["sequence"],
        )
        for e in pipe(text)
    ]


def run(model):
    tokenizer = BertTokenizer.from_pretrained(model)
    bert_model = BertForMaskedLM.from_pretrained(model)
    pipe = pipeline(
        "fill-mask", model=bert_model, tokenizer=tokenizer
    )

    prevtext = {}
    while True:
        try:
            text = input("bert query: ")
        except EOFError:
            exit("")
        text = text.strip()
        if text == "q":
            exit()
        if not text:
            text = prevtext[1]
        try:
            num = int(text)
            if not 0 < num < len(prevtext) + 1:
                print("No such option")
                continue
            text = prevtext[num]
        except ValueError:
            pass
        retval = predict(text, pipe)
        print()
        for i, e in enumerate(retval):
            print(i + 1, e.sentence, e.score)
            prevtext[i + 1] = e.sentence
        print("\n")


def main():
    import sys

    if len(sys.argv) < 2:
        exit(
            "Usage: bertrand model\n"
            "e.g.   bertrand ltg/norbert2\n"
            "       bertrand bert-large-uncased\n"
            "       bertrand allenai/scibert_scivocab_uncased "
        )
    MODEL = sys.argv[1]
    run(MODEL)


if __name__ == "__main__":
    main()

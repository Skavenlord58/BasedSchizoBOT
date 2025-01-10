import time

from ufal.morphodita import *

from utils import truncate_emojis, Token, find_me

# load from file
with open("sentences.txt", "r", encoding="utf-8") as f:
    texts = f.readlines()
texts = [truncate_emojis(x.strip().lower()) for x in texts]

# measure time
start = time.monotonic()
word_count = 0

keyword = "jsem"


def analyze_sentence(tokenizer, tagger, text):
    forms = Forms()
    lemmas = TaggedLemmas()
    tokens = TokenRanges()
    global word_count
    print("Text: ", text)
    # Tag
    tokenizer.setText(text)
    toks = []
    t_iter = 0
    while tokenizer.nextSentence(forms, tokens):
        has_word = False
        sentence_end = False
        toks = []
        tagger.tag(forms, lemmas)

        for i in range(len(lemmas)):
            if sentence_end:
                has_word = False
                sentence_end = False
                toks = []

            lemma = lemmas[i]
            token = tokens[i]

            tok = Token(text[t_iter: token.start], lemma.lemma, lemma.tag, text[token.start: token.start + token.length])
            t_iter = token.start + token.length
            word_count += 1

            # interpunkce
            if tok.lemma_tag[0] == "Z":
                sentence_end = True
                if len(toks) > 0:
                    break
            # přidáváme až po jsem, ale jsem samotné vynecháváme
            if has_word and not sentence_end:
                toks.append(tok)
            # jsem
            if tok.text == keyword:
                has_word = True
        if has_word and sentence_end:
            break
    # pokud je tam další sloveso, je to špatně
    if any([tok.lemma_tag[0:2] == "VB" for tok in toks]):
        print("špatná: " + "".join([tok.text_before + tok.text for tok in toks]))
    elif any([tok.lemma_tag[0:2] == "NN" and tok.lemma_tag[3:5] == "S1" for tok in toks]):
        print("správná: " + "".join([tok.text_before + tok.text for tok in toks]))
    else:
        print("špatná:" + "".join([tok.text_before + tok.text for tok in toks]))


for text in texts:
    ok, sentence, word_count_add = find_me(text, keyword)
    word_count += word_count_add
    print("správná: " if ok else "špatná: " + sentence)

end = time.monotonic()
print("Time in seconds: ", end - start)
print("Word count: ", word_count)
print("Words per second: ", word_count / (end - start))

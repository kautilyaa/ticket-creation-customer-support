import nltk
import re

def extract_feature(text, syn_list, reg=None):
    sent = nltk.sent_tokenize(text.lower())
    words = [nltk.word_tokenize(s) for s in sent]
    stop_words = set(nltk.corpus.stopwords.words('english'))
    simp_words = []
    for s in words:
        simp_words.append([x for x in s if not(x in (stop_words.union(set(['-', ':', '.'])) - set(['from', 'to'])))])
    if (reg):
        reg = re.compile(reg)
    for token in syn_list:
        for s in simp_words:
            # OLD
            #if (token in s):

            # NEW
            tok_split = token.split()
            if (tok_split[0] in s):
                cond = True
                index = s.index(tok_split[0])
                for w in tok_split[1:]:
                    index += 1
                    try:
                        if (w != s[index]):
                            cond = False
                            break
                    except:
                        break
                if (not cond):
                    continue
                try:
                    if (reg):
                        x = reg.match(s[index+1]).group()
                        if (x != ''):
                            return x
                        else:
                            continue
                    return s[index+1]
                except:
                    continue
    return False

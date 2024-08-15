#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# sentsim.py
#
# Copyright (C) 2022 Frederic Blain (feedoo) <f.blain@sheffield.ac.uk>
#
# Licensed under the "THE BEER-WARE LICENSE" (Revision 42)
#

"""

"""

from sentence_transformers import SentenceTransformer
from scipy import spatial
import codecs

sent_it = []
with codecs.open("../data/conan_barbarian/conanthebarbarian_IT.txt", 'r', encoding='utf-8') as f_it:
    sent_it = [l.rstrip() for l in f_it]

print("File open")    
sent_en = []
with codecs.open("../data/conan_barbarian/conanthebarbarian_dialog.txt", 'r', encoding='utf-8') as f_en:
    sent_en = [l.rstrip() for l in f_en]

print("Not finished yet")

model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')
embeddings_it = model.encode(sent_it)
embeddings_en = model.encode(sent_en)

print("model ready")

with codecs.open("../data/conan_barbarian/aligned_it-en.it.txt",'w', encoding='utf-8') as f_out_it, \
        codecs.open("../data/conan_barbarian/aligned_it-en.en.txt",'w', encoding='utf-8') as f_out_en, \
        codecs.open("../data/conan_barbarian/aligned_it-en.scores.txt",'w', encoding='utf-8') as f_out_scores:

            print("ready to align")
            for it_idx in range(len(embeddings_it)):
                cosine_scores = [1 - spatial.distance.cosine(embeddings_it[it_idx],emb_en) for emb_en in embeddings_en]
                best_cosine = max(cosine_scores)
                best_match_en_idx = cosine_scores.index(best_cosine)

                f_out_it.write("{}\t{}\n".format(it_idx,sent_it[it_idx]))
                f_out_en.write("{}\t{}\n".format(best_match_en_idx,sent_en[best_match_en_idx]))
                f_out_scores.write("{}\n".format(best_cosine))

print("aligning done")

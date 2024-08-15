# Adventure_Corpus
Part of the Dissertation Project 'A cross-linguistic study of culture-bound expressions in subtitles' by Annalisa Ranzenigo. University of Málaga and University of Wolverhampton, Masters in Technology for Tranlsation and Interpreting, EM TTI.

English dialogues - Italian subtitles parallel annotated corpus of adventure-genre films.
The Italians subtitles are taken from opensubtitles.org, preprocessed and aligned to the English dialogues. 
Annotation of culture bound elements, strategies and errors. 
Italian subtitles with POS tags are available in the POS folder. 
Italian subtitles with annotation of the strategies are available in the culture-bound_it_annotations folder.
Raw parallel corpus and English annotated texts will be available after confiramtion from Film Corpus 2.0 of rights for sharing data used for reseach.

Throughout various alignment trials, I observed that existing alignment tools struggle when applied to audiovisual translation material. As a result, I tried a different alignment approach and, in collaboration with Dr. Frederic Blain, developed a Python code (sentsim.py) which aligns phrases using cosine similarity, saving the aligned sentences sorted by their scores. The process involves reading Italian and English sentences from separate files, and computing embeddings for each sentence using a pre-trained Sentence Transformer model. The final alignment methodology involved combining the code with an alignment tool available on the marketL LF aligner.

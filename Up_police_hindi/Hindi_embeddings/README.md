Embeddings are organised into the following categories:
1. Monolingual - Embeddings for a single language, generated via various methods. They are further classified into contextual and non-contextual embeddings.
2. Crosslingual - Embeddings for a pair of languages, generated via MUSE.

Note that the embeddings collected here have been generated from datasets which have been transliterated into devanagari script. The entire list of languages is :
1. as - Assamese
2. bn - Bengali
3. gu - Gujarati
4. hi - Hindi
5. kn - Kannada
6. ko - Konkani
8. ml - Malayalam
9. mr - Marathi
10. ne - Nepali
11. pa - Punjabi
12. sa - Sanskrit
13. ta - Tamil
14. te - Telugu

-----------
Monolingual
-----------

Under the monolingual category, we have embeddings generated using 5 different methods:
1. CBOW - generated using gensim library (https://github.com/RaRe-Technologies/gensim)
	- Embeddings with dimensions 50, 100, 200, 300 exist for each language
	- A min-count parameter of value 2 was used. Default values were used for all other settings
2. Skipgram - generated using gensim library (https://github.com/RaRe-Technologies/gensim)
	- Embeddings with dimensions 50, 100, 200, 300 exist for each language
	- A min-count parameter of value 2 was used. Default values were used for all other settings
3. Fasttext - generated using gensim library (https://github.com/RaRe-Technologies/gensim)
	- Embeddings with dimensions 50, 100, 200, 300 exist for each language
	- A min-count parameter of value 2 was used. Default values were used for all other settings
4. GloVe - generated using GloVe source (downloaded and built from https://nlp.stanford.edu/projects/glove/)
	- Embeddings with dimensions 50, 100, 200, 300 exist for each language except currently for Marathi
	- Default values were used for all settings
5. ELMo - generated using bilm-tf implementation (https://github.com/allenai/bilm-tf)
	- Embeddings with dimensions 512 exist for each language except currently for Sanskrit
	- Default values were used for all settings

The directory structure inside the monolingual folder is organised as follows:
<lang>/<dim>/<method>/<lang>-d<dim>-<method>.<extension>
where <lang> is the 2 letter ISO-639 abbreviation of the language, <dim> is one of 50, 100, 200 , 300 and represents the dimension of the trained model. <method> refers to either cbow (CBOW), sg (Skipgram), fasttext (FastText), glove (GloVe) or elmo (ELMo). Finally, the model will be a file at the end of this directory.

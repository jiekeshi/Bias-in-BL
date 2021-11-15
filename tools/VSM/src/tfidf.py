
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from gensim.similarities import SparseMatrixSimilarity


def compute_similarity(text_data, bug_data):

    text_content = []
    files = []
    for file, content in text_data.items():
        text_content.append(content["content"])
        files.append(file)
    dct = Dictionary(text_content)

    code_vecs = [dct.doc2bow(text) for text in text_content]
    model = TfidfModel(code_vecs, "lfn")
    index = SparseMatrixSimilarity(model[code_vecs], num_features=len(dct))
    bug_content = bug_data["AMBARI-4269.xml"]["content"]
    sims = index[dct.doc2bow(bug_content)]
    sorted_files = sorted(range(len(sims)), key=lambda k: sims[k], reverse=True)

    for i in sorted_files[:10]:
        print(files[i])



    
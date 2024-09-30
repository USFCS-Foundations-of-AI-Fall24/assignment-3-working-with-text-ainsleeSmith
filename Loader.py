## Code for loading training sets and creating documents.
import string
from operator import truediv

from Document import *
from Cluster import *
from make_dataset import create_docs


# you should be able to call this like:
# positive_docs = create_easy_documents(pos_reviews, 'pos',
#                                  filters=[not_stopword],
#                                  transforms=[convert_to_lowercase, remove_trailing_punct])
def create_easy_documents(list_of_docs, true_class, filters=None, transforms=None) :
    document_list = []
    for item in list_of_docs :
        d = Document(true_class=true_class)
        words = item
        ## deal with filters here
        for f in filters:
            words = [word for word in words if f(word)]

        ## deal with transforms here
        # for word in words :
        #     remove_trailing_punct(word)
        #     convert_to_lowercase(word)

        d.add_tokens(words)
        document_list.append(d)
    return document_list

## filters - return true if the token meets the criterion

# you do this.
def not_stopword(token) :
    if (token != "a") and (token != "an") and (token != "the") :
        return True
    return False
    #pass

def not_cat(token) :
    return token != 'cat'
    # return token is not 'cat'


# transforms - convert a token into a new format

# you do this.
def remove_trailing_punct(token) :
    for p in string.punctuation :
        if token[-1] == p :
            token = token.strip(token[-1])
    return token

# and this
def convert_to_lowercase(token) :
    return token.lower()



## homogeneity: for each cluster, what fraction of the cluster is comprised of the largest class?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_homogeneity(result, ['pos','neg'])
def compute_homogeneity(list_of_clusters, list_of_classes) :
    # hlist will be the homogeneity for each cluster.
    hlist = []

    return hlist
    # TODO how many in the pos vs neg classes

## completeness: for the dominant class in each cluster, what fraction
# of that class' members are in that cluster?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_completeness(result, ['pos','neg'])

def compute_completeness(list_of_clusters, list_of_classes) :
    # clist will be the homogeneity for each cluster.
    clist = []

    return clist
    # TODO classes are pos and neg

if __name__=="__main__" :

    pos_reviews, neg_reviews = create_docs(10,10)

    positive_docs = create_easy_documents(pos_reviews, 'pos',
                                 filters=[],
                                 transforms=[])

    negative_docs = create_easy_documents(neg_reviews, 'neg',
                                    filters=[],
                                 transforms=[])






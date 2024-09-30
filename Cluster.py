import random

from Document import *

class Cluster :
    ## a cluster is a group of documents
    def __init__(self, centroid=None, members=None):
        if centroid :
            self.centroid = centroid
        else :
            self.centroid = Document(true_class='pos')
        if members :
            self.members = members
        else :
            self.members = []

    def __repr__(self):
        return f"{self.centroid} {len(self.members)}"

    ## You do this.
    def calculate_centroid(self):
        d = Document(true_class='pos')
        token_sum = 0
        for m in self.members :
            token_sum = token_sum + sum([(m.tokens[item]) for item in m.tokens])
        avg = token_sum/len(self.members)
        # d.tokens = "avg",avg
        i = 0
        while i < avg :
            d.add_tokens("avg")
        return d
        # pass


# Call like so: k_means(2, ['pos','neg'], positive_docs + negative_docs)

def k_means(n_clusters, true_classes, data) :
    cluster_list = [Cluster(centroid=Document(true_class=item)) for item in true_classes]

    ## initially assign data randomly.
        # TODO use random function # cluster_list[random]
    for d in data :
        cluster_list[random.randint(0,n_clusters)] = d

    ## compute initial cluster centroids
    for c in cluster_list :
        c.centroid = c.calculate_centroid()

    # while not done and i < limit
    #   i++
    # TODO WHAT DOES THIS MEAN?!?!

    #   reassign each Document to the closest matching cluster using
    #   cosine similarity
    for d in data :
        closest = 100
        for c in cluster_list :
            sim = cosine_similarity(d, c.centroid)
            if  sim < closest :
                closest = sim
                c.append(data)
                # TODO remove data from its current cluster??

    #   compute the centroids of each cluster
    for c in cluster_list :
        c.centroid = c.calculate_centroid()

    return cluster_list
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
        for m in self.members: # add all the keys from the member docs to the centroid doc

            d.add_tokens(m.tokens)
        for item in d.tokens : # set the value for the tokens to the avg
            val = d.tokens[item]
            val = val / len(self.members)
            d.tokens[item] = val
        return d
        # pass


# Call like so: k_means(2, ['pos','neg'], positive_docs + negative_docs)

def k_means(n_clusters, true_classes, data) :
    cluster_list = [Cluster(centroid=Document(true_class=item)) for item in true_classes]

    ## initially assign data randomly.
        # TODO use random function # cluster_list[random]
    # index = 0
    for d in data :
        index = random.randint(0,n_clusters - 1)
        cluster_list[index].members.append(d)
        d.cluster = cluster_list[index]
        # if index == 0 :
        #     index = 1
        # elif index == 1 :
        #     index = 0
        # append to the members list
    ## compute initial cluster centroids
    for c in cluster_list :
        c.centroid = Cluster.calculate_centroid(c)

    # while not done and i < limit
    #   i++
    # ex: either all clusters are septerated or do 10
    # if nobody moves then exit loop, if somone moves then done = false
    done = False
    limit = 10
    i = 0
    while not done and (i < limit) :
        # add a member variable to the document class to tell which cluster it is in
        #   reassign each Document to the closest matching cluster using
        #   cosine similarity
        done = True
        for d in data :
            closest = 0
            best_fit = d.cluster
            for c in cluster_list :
                sim = cosine_similarity(d, c.centroid)
                if  sim > closest :
                    closest = sim
                    best_fit = c
            if best_fit != d.cluster : # if one is moved then we are not done
                done = False
                best_fit.members.append(d)
                d.cluster.members.remove(d)
                d.cluster = best_fit

        #   compute the centroids of each cluster
        for c in cluster_list :
            c.centroid = c.calculate_centroid()
        i = i + 1
    return cluster_list
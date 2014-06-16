import  random
import  numpy
import  scipy
import  pickle

def count(el, cluster):
    counter = 0.0
    for c in cluster:
        for d in c:
            if el[0] = d[0]:
                counter += d[1]
                break
    return counter

def dist(d1,cluster):
    distance = 0
    n = len(cluster)
    for element in d1:
        distance += count(element,cluster)/n
    return distance

def default_cntroids(data, k):
    return random.sample(data, k)


def k_means(data, iteration, num_clusters):
    clusters = default_clusters(data, num_clusters)

    for i in xrange(iteration):
        new_clusters = []
        for element in data.keys():
            temp = []
            for c in clusters:
                temp.append(dist(c,element))
            new_clusters[temp.index(min(temp))].append(element)
        # centroids = update_centroids()
        clusters = new_clusters
    return [clusters, centroids]

def main():
    f = open("doc.txt", 'rb')
    data = pickle.load(f)
    [clusters, centroids] = k_means(data = data,iteration = 10, num_clusters = 3)

if __name__ == '__main__':
    main()

import  random
import  numpy
import  scipy
import  pickle

def dist(d1,d2):
    return 0

def default_clusters(data, k):
    return [list(),list()]

def centroid(cluster):
    return[]

def update_centroids():
    return []

def k_means(data, iteration, num_clusters):
    [clusters, centroids] = default_clusters(data, num_clusters)

    for i in xrange(iteration):
        new_clusters = []
        for element in data:
            temp = []
            for c in centroids:
                temp.append(dist(c,element))
            new_clusters[temp.index(min(temp))].append(element)
        centroids = update_centroids()
        clusters = new_clusters
    return [clusters, centroids]

def main():
    # f = open("data.txt", 'rb')
    # data = pickle.load(f)
    data = []
    [clusters, centroids] = k_means(data = data,iteration = 10, num_clusters = 5)

if __name__ == '__main__':
    main()

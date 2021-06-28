from random import randint
from matplotlib import pyplot as plt


def compute_histogram_bins(data=[], bins=[]):
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted numbers that represents your histogram
              bin thresdholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins.
        You are not allowed to use external libraries other than those already
        imported.
    """
    histogram_bins={}                       #create an empty dictionary to save pair bin:value_count
    idx = 0
    data.sort()
    for item in data:
        for v in bins:                      #sorting data per bins
            idx = (idx + 1) % len(bins)
            next_elem = bins[idx]
            if v <= item < next_elem:
                histogram_bins[v]=histogram_bins.get(v,0)+1
        if item >= bins[-1]:                    #add values to the last bin
            histogram_bins[item]=histogram_bins.get(v,0)+1

    return (histogram_bins)


def plot_histogram(bins_count):
    """
        Question 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommend using
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """
    #get bins as x coordinates of the bars, get value_count as heights of the bars
    plt.bar(bins_count.keys(),bins_count.values(), width = 15, align='edge', color='g')
    plt.show()


if __name__ == "__main__":

    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)

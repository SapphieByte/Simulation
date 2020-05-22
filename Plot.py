from matplotlib import pyplot as plt

def plot(d):
    plt.plot(d[0], label="Employed", color="#2489FF")
    plt.plot(d[1], label="Average Money", color="#FFCC12")
    plt.plot(d[2], label="People alive (100s)", color="#23FF44")
    plt.plot(d[3], label="People alive all-time (100s)", color="#119911")
    plt.plot(d[4], label="People died all-time (100s)", color="#dd0000")
    

    plt.xlabel("Time")
    plt.ylabel("Higher Value")

    plt.legend()
    plt.show()

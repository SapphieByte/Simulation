from matplotlib import pyplot as plt

def plot(d):
    plt.plot(d[0], label="Employed", color="#2489FF")
    plt.plot(d[1], label="Average Money", color="#FFCC12")
    plt.plot(d[2], label="People alive (100s)", color="#23FF44")
    plt.plot(d[3], label="People alive all-time (100s)", color="#119911")
    plt.plot(d[4], label="People died all-time (100s)", color="#dd0000")

    plt.plot(d[5], label="Builders (100s)")
    plt.plot(d[6], label="Scientists (100s)")
    plt.plot(d[7], label="Accountants (100s)")
    plt.plot(d[8], label="Thiefs (100s)")
    plt.plot(d[9], label="Electricians (100s)")
    plt.plot(d[10], label="Cashiers/Fast-Food Workers (100s)")

    

    plt.xlabel("Time")
    plt.ylabel("Higher Value")

    plt.legend()
    plt.show()

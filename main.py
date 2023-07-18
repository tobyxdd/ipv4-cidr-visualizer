import sys
import ipaddress
import matplotlib.pyplot as plt
import matplotlib.patches as patches

IPV4_MAX = 2**32

COLOR_BG = "#DBE4EE"
COLOR_FG = "#054A91"


def cidr_to_range(cidr):
    net = ipaddress.ip_network(cidr, strict=False)
    start = int(net.network_address)
    end = int(net.broadcast_address)
    return (start, end)


def plot_cidrs(cidrs):
    fig, ax = plt.subplots(1)
    fig.canvas.manager.set_window_title("IPv4 CIDR visualizer")

    ax.add_patch(patches.Rectangle((0, 0), IPV4_MAX, 1, color=COLOR_BG))

    for cidr in cidrs:
        start, end = cidr_to_range(cidr)
        ax.add_patch(patches.Rectangle((start, 0), end - start, 1, color=COLOR_FG))

    plt.xlim([0, IPV4_MAX])
    plt.ylim([0, 1])
    plt.axis("off")
    plt.show()


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "cidrs.txt"

    with open(filename, "r") as f:
        cidrs = [line.strip() for line in f.readlines() if line.strip()]

    plot_cidrs(cidrs)


if __name__ == "__main__":
    main()

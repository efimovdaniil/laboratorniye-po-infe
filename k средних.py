import random
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# Parameters
DELTA_X = 0.2
K = 3  # Number of clusters
RANDOM_SEED = 2


def generate_circular_cluster(center_x, center_y, radius, num_points):
    points = []
    i = 0
    while i < num_points:
        x = random.uniform(center_x - 5, center_x + 5)
        y = random.uniform(center_y - 5, center_y + 5)
        if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
            points.append([x, y])
            i += 1
    return points


def assign_clusters(points, centroids):
    cluster_assignments = []
    for point in points:
        distances = []
        for centroid in centroids:
            distance = math.sqrt((point[0] - centroid[0]) ** 2 + (point[1] - centroid[1]) ** 2)
            distances.append(distance)
        cluster_idx = distances.index(min(distances))
        cluster_assignments.append(cluster_idx)
    return cluster_assignments


def update_centroids(points, cluster_assignments, k):
    new_centroids = []
    for cluster_idx in range(k):
        x_sum = 0
        y_sum = 0
        count = 0
        for i, point in enumerate(points):
            if cluster_assignments[i] == cluster_idx:
                x_sum += point[0]
                y_sum += point[1]
                count += 1
        if count > 0:  # Avoid division by zero
            x_mean = x_sum / count
            y_mean = y_sum / count
            new_centroids.append([x_mean, y_mean])
        else:
            new_centroids.append(centroids[cluster_idx])
    return new_centroids


def calculate_centroid_shift(old_centroids, new_centroids):
    shifts = []
    for i in range(len(old_centroids)):
        shift = math.sqrt(
            (new_centroids[i][0] - old_centroids[i][0]) ** 2 +
            (new_centroids[i][1] - old_centroids[i][1]) ** 2
        )
        shifts.append(shift)
    return shifts


def run_kmeans(points, k, max_iterations=100):
    """Run K-means clustering algorithm."""
    # Initialize random centroids
    random.seed(RANDOM_SEED)
    x_min = min(point[0] for point in points)
    x_max = max(point[0] for point in points)
    y_min = min(point[1] for point in points)
    y_max = max(point[1] for point in points)

    centroids = []
    for _ in range(k):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        centroids.append([x, y])

    centroid_history = [centroids.copy()]

    # Run K-means iterations
    iteration = 0
    max_shift = float('inf')

    while max_shift > DELTA_X and iteration < max_iterations:
        cluster_assignments = assign_clusters(points, centroids)

        new_centroids = update_centroids(points, cluster_assignments, k)

        shifts = calculate_centroid_shift(centroids, new_centroids)
        max_shift = max(shifts)

        centroids = new_centroids
        centroid_history.append(centroids.copy())
        iteration += 1

    return cluster_assignments, centroids, centroid_history


def visualize_kmeans(points, centroid_history):
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(bottom=0.25)

    # Plot data points
    data_scatter = ax.scatter([p[0] for p in points], [p[1] for p in points], c='blue', alpha=0.6)

    initial_centroids = ax.scatter(
        [c[0] for c in centroid_history[0]],
        [c[1] for c in centroid_history[0]],
        c='red', marker='x', s=100, label='Initial Centroids'
    )

    current_centroids = ax.scatter(
        [c[0] for c in centroid_history[0]],
        [c[1] for c in centroid_history[0]],
        c='black', marker='o', s=80, label='Current Centroids'
    )

    ax.legend()

    ax.set_title('K-средние')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    iteration_slider = Slider(
        ax=ax_slider,
        label='Iteration',
        valmin=0,
        valmax=len(centroid_history) - 1,
        valinit=0,
        valstep=1
    )

    def update(val):
        iteration = int(iteration_slider.val)
        current_centroids.set_offsets(np.array(centroid_history[iteration]))

        # Update title to show current iteration
        ax.set_title(f'K-means Clustering - Iteration {iteration}')

        # Redraw the figure
        fig.canvas.draw_idle()

    # Register the update function with the slider
    iteration_slider.on_changed(update)

    plt.show()


# Main execution
if __name__ == "__main__":
    # Generate synthetic data
    cluster1 = generate_circular_cluster(2, 3, 4, 25)
    cluster2 = generate_circular_cluster(12, 13, 5, 30)
    cluster3 = generate_circular_cluster(-8, -10, 3, 25)
    all_points = cluster1 + cluster2 + cluster3

    # Run K-means
    final_clusters, final_centroids, centroid_history = run_kmeans(all_points, K)

    # print(f"K-means converged after {len(centroid_history)-1} iterations")
    # print(f"Final centroids: {final_centroids}")

    # Visualize results
    visualize_kmeans(all_points, centroid_history)
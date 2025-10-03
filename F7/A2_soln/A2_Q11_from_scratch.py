# A2, Q11.

import random

def visualize_counts(viz_dice_faces, viz_roll_counts, viz_scaled_counts):
    print(f"{'face':>4} {'count':>8}")
    for i, face in enumerate(viz_dice_faces):
        viz_roll_count = viz_roll_counts[i]
        viz_scaled_count = viz_scaled_counts[i]
        print(f"{face:>4} {viz_roll_count:>8} {'*' * viz_scaled_count}")

N = 6
M = 2
NUM_ROLLS = 400
SCREEN_WIDTH = 40

max_score = N * M
score_counts = [0] * (max_score + 1) # maybe?

for roll_id in range(NUM_ROLLS):
    score = 0
    for m in range(M):
        score = score + random.randint(1, N)
    score_counts[score] = score_counts[score] + 1


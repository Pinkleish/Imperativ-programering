import random

# Possible Solution to the later parts of A2, (F5):

def visualize_counts(viz_dice_faces, viz_roll_counts, viz_scaled_counts):
    print(f"{'face':>4} {'count':>8}")
    for i, face in enumerate(viz_dice_faces):
        viz_roll_count = viz_roll_counts[i]
        viz_scaled_count = viz_scaled_counts[i]
        print(f"{face:>4} {viz_roll_count:>8} {'*' * viz_scaled_count}")

N = 6 # sides of dice
M = 3 # number of dice to roll on a turn
NUM_ROLLS = 4000
SCREEN_WIDTH = 40

max_score = N * M

# first element represents roll-count for 1
score_counts = [0] * max_score

faces = list(range(1, max_score + 1))

for i in range(NUM_ROLLS):
    # Roll the M dice and add up the total score
    score = 0
    for m in range(M):
        # Roll 1 dice and add its value to the score.
        roll = random.randint(1, N)
        score = score + roll

    score_index = score - 1 # Roll 1 is the first (zeroth) element
    score_counts[score_index] = score_counts[score_index] + 1

# Find the max count with a linear search:
max_count = -1
for count in score_counts:
    if max_count < count:
        max_count = count

# Compute the scaling factor:
scaling_factor =  SCREEN_WIDTH / max_count

# Create a new array of scaled counts:
scaled_counts = [0] * len(score_counts)
for i in range(len(score_counts)):
    scaled_counts[i] = int(score_counts[i] * scaling_factor)


# for M dice, this is now a list of possible scores for M dice,
# instead of the face values themselves:
# e.g. for M = 2, range 1,..,6*6
faces = range(1, max_score + 1)


visualize_counts(faces, score_counts, scaled_counts)
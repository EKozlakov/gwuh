# Author: Aleese Mukhamedjanova
# Date: 09/24/2023
# Description: Taking the number 123456, determines a permutation such that the left most digit is evenly divisible
# by 1, the two left most digits are evenly divisible by 2, the three left most digits are divisible by 3, and so on.

# The smallest correct permutation is 123654, and the elapsed time is 0.0 seconds.

import time
startTime = time.time()

finished = False

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

# --------------------
# DETERMINE POSITION 1
for a in range(1, 7):

    if a % 1 != 0:
        continue

    # --------------------
    # DETERMINE POSITION 2
    for b in range(1, 7):

        if b == a:
            continue

        numString = str(a) + str(b)

        if int(numString) % 2 != 0:
            continue

        # --------------------
        # DETERMINE POSITION 3
        for c in range(1, 7):

            if c == b or c == a:
                continue

            numString = str(a) + str(b) + str(c)

            if int(numString) % 3 != 0:
                continue

            # --------------------
            # DETERMINE POSITION 4
            for d in range(1, 7):

                if d == c or d == b or d == a:
                    continue

                numString = str(a) + str(b) + str(c) + str(d)

                if int(numString) % 4 != 0:
                    continue

                # --------------------
                # DETERMINE POSITION 5
                for e in range(1, 7):

                    if e == d or e == c or e == b or e == a:
                        continue

                    numString = str(a) + str(b) + str(c) + str(d) + str(e)

                    if int(numString) % 5 != 0:
                        continue

                    # --------------------
                    # DETERMINE POSITION 6
                    for f in range(1, 7):

                        if f == e or f == d or f == c or f == b or f == a:
                            continue

                        numString = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)

                        if int(numString) % 6 != 0:
                            continue
                        else:
                            finished = True
                            break

                    if finished:
                        break
                if finished:
                    break
            if finished:
                break
        if finished:
            break
    if finished:
        break

print(f"The smallest correct permutation is {a}{b}{c}{d}{e}{f}")

print(f"Total time elapsed is {time.time() - startTime} seconds")

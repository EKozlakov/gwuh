# Author: Aleese Mukhamedjanova
# Date: 09/24/2023
# Description: Taking the number 1234567890, determines a permutation such that the left most digit is evenly divisible
# # by 1, the two left most digits are evenly divisible by 2, the three left most digits are divisible by 3, and so on.

# The smallest correct permutation is 3816547290, and the elapsed time is 0.0020003318786621094 seconds.

import time
startTime = time.time()

finished = False

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0

# --------------------
# DETERMINE POSITION 1
for a in range(0, 10):

    if a % 1 != 0:
        continue

    # --------------------
    # DETERMINE POSITION 2
    for b in range(0, 10):

        if b == a:
            continue

        numString = str(a) + str(b)

        if int(numString) % 2 != 0:
            continue

        # --------------------
        # DETERMINE POSITION 3
        for c in range(0, 10):

            if c == b or c == a:
                continue

            numString = str(a) + str(b) + str(c)

            if int(numString) % 3 != 0:
                continue

            # --------------------
            # DETERMINE POSITION 4
            for d in range(0, 10):

                if d == c or d == b or d == a:
                    continue

                numString = str(a) + str(b) + str(c) + str(d)

                if int(numString) % 4 != 0:
                    continue

                # --------------------
                # DETERMINE POSITION 5
                for e in range(0, 10):

                    if e == d or e == c or e == b or e == a:
                        continue

                    numString = str(a) + str(b) + str(c) + str(d) + str(e)

                    if int(numString) % 5 != 0:
                        continue

                    # --------------------
                    # DETERMINE POSITION 6
                    for f in range(0, 10):

                        if f == e or f == d or f == c or f == b or f == a:
                            continue

                        numString = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)

                        if int(numString) % 6 != 0:
                            continue

                        # --------------------
                        # DETERMINE POSITION 7
                        for g in range(0, 10):

                            if g == f or g == e or g == d or g == c or g == b or g == a:
                                continue

                            numString = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g)

                            if int(numString) % 7 != 0:
                                continue

                            # --------------------
                            # DETERMINE POSITION 8
                            for h in range(0, 10):

                                if h == g or h == f or h == e or h == d or h == c or h == b or h == a:
                                    continue

                                numString = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h)

                                if int(numString) % 8 != 0:
                                    continue

                                # --------------------
                                # DETERMINE POSITION 9
                                for i in range(0, 10):

                                    if i == h or i == g or i == f or i == e or i == d or i == c or i == b or i == a:
                                        continue

                                    numString = (str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) +
                                                 str(i))

                                    if int(numString) % 9 != 0:
                                        continue

                                    # --------------------
                                    # DETERMINE POSITION 10
                                    for j in range(0, 10):

                                        if j == i or j == h or j == g or j == f or j == e or j == d or j == c or j == b or j == a:
                                            continue

                                        numString = (str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(
                                            h) + str(i)) + str(j)

                                        if int(numString) % 10 != 0:
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
                if finished:
                    break
            if finished:
                break
        if finished:
            break
    if finished:
        break

print(f"The smallest correct permutation is {a}{b}{c}{d}{e}{f}{g}{h}{i}{j}")

print(f"Total time elapsed is {time.time() - startTime} seconds")

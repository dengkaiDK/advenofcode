# Code solution for day 11
# Time 2022-09-12
import numpy as np
import copy


class Solution:
    def __init__(self):
        self.input = np.array([list(line.strip()) for line in open("input.txt", 'r')], dtype = int)

    def run(self):
        epoch = 500 # for part 2
        # epoch = 100 # for part 1
        flashes = 0
        w, h = self.input.shape
        energy = copy.copy(self.input)
        for i in range(0, epoch):
            energy = energy + 1
            flash_coordinates = list(np.argwhere(energy == 10))
            flash_flag = {(x,y): True for x, y in flash_coordinates}
            while len(flash_coordinates) > 0:
                x, y = flash_coordinates.pop(0)
                energy[x, y] = 0  # reset energy
                # update energy of neighbors
                if x > 0 and (x-1, y) not in flash_flag:
                    energy[x-1, y] += 1
                    if energy[x-1, y] > 9:
                        flash_coordinates.append([x-1, y])
                        flash_flag[(x-1, y)] = True
                if x < w-1 and (x+1, y) not in flash_flag:
                    energy[x+1, y] += 1
                    if energy[x+1, y] > 9:
                        flash_coordinates.append([x+1, y])
                        flash_flag[(x+1, y)] = True
                if y > 0 and (x, y-1) not in flash_flag:
                    energy[x, y-1] += 1
                    if energy[x, y-1] > 9:
                        flash_coordinates.append([x, y-1])
                        flash_flag[(x, y-1)] = True
                if y < h-1 and (x, y+1) not in flash_flag:
                    energy[x, y+1] += 1
                    if energy[x, y+1] > 9:
                        flash_coordinates.append([x, y+1])
                        flash_flag[(x, y+1)] = True
                if x > 0 and y > 0 and (x-1, y-1) not in flash_flag:
                    energy[x-1, y-1] += 1
                    if energy[x-1, y-1] > 9:
                        flash_coordinates.append([x-1, y-1])
                        flash_flag[(x-1, y-1)] = True
                if x < w-1 and y < h-1 and (x+1, y+1) not in flash_flag:
                    energy[x+1, y+1] += 1
                    if energy[x+1, y+1] > 9:
                        flash_coordinates.append([x+1, y+1])
                        flash_flag[(x+1, y+1)] = True
                if x > 0 and y < h-1 and (x-1, y+1) not in flash_flag:
                    energy[x-1, y+1] += 1
                    if energy[x-1, y+1] > 9:
                        flash_coordinates.append([x-1, y+1])
                        flash_flag[(x-1, y+1)] = True
                if x < w-1 and y > 0 and (x+1, y-1) not in flash_flag:
                    energy[x+1, y-1] += 1
                    if energy[x+1, y-1] > 9:
                        flash_coordinates.append([x+1, y-1])
                        flash_flag[(x+1, y-1)] = True

            flashes += len(flash_flag)
            # for Part 2
            if len(flash_flag) == w * h:
                print(i + 1, ' Step to flash simultaneously')
                break

        return flashes



if __name__ == "__main__":
    solution = Solution()
    print(solution.run())
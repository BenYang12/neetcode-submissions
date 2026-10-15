class UnionFind:
    def __init__(self, size):
        # parent[i] = -1 means cell i is WATER (not part of any island yet).
        # parent[i] >= 0 means cell i is LAND, and parent[i] points
        # toward the root of its island.
        self.parent = [-1] * size

        # rank[i] = upper bound on the height of the tree rooted at i.
        # Used so we always attach the shorter tree under the taller one.
        self.rank = [0] * size

        # Number of islands right now (number of separate land trees).
        self.count = 0

    def add_land(self, x):
        # If x is already land (a duplicate position), do nothing.
        # Without this check, we'd count the same cell as a new island twice.
        if self.parent[x] >= 0:
            return
        self.parent[x] = x      # x becomes the root of a brand new 1-cell island
        self.count += 1         # one more island exists

    def is_land(self, x):
        # Shorter equivalent: return self.parent[x] >= 0
        return self.parent[x] >= 0

    def number_of_islands(self):
        return self.count

    def find(self, x):
        # Full path compression (recursive): after finding the root,
        # point x directly at it so future finds are instant.
        # Recursion depth is safe because union by rank keeps trees short.
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)     # root of x's island
        yset = self.find(y)     # root of y's island

        # Same root means they're already the same island.
        # Return WITHOUT touching count. This is what prevents
        # double-subtracting when a new cell touches one island twice.
        if xset == yset:
            return

        # Union by rank: hang the shorter tree under the taller one.
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            # Equal heights: pick one as root, and it grows one level taller.
            self.parent[yset] = xset
            self.rank[xset] += 1

        # Two islands just became one.
        self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # Direction offsets, read in pairs (x[i], y[i]):
        # (-1,0) = up, (1,0) = down, (0,-1) = left, (0,1) = right
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        dsu = UnionFind(m * n)  # one slot per grid cell, all water at first
        answer = []

        for position in positions:
            r, c = position[0], position[1]

            # Flatten (r, c) to a single index: row r starts at r * n.
            land_position = r * n + c
            dsu.add_land(land_position)         # count goes up by 1 (if new)

            for i in range(4):
                neighbor_x = r + x[i]
                neighbor_y = c + y[i]

                # Bounds check FIRST, before computing the index.
                # An off-grid neighbor can produce a valid-looking but wrong
                # index (e.g., column -1 wraps to the previous row's last cell).
                if 0 <= neighbor_x < m and 0 <= neighbor_y < n:
                    neighbor_position = neighbor_x * n + neighbor_y
                    if dsu.is_land(neighbor_position):
                        dsu.union(land_position, neighbor_position)  # count may go down

            answer.append(dsu.number_of_islands())

        return answer
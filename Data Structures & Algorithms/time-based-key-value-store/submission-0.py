class TimeMap:

    def __init__(self):
        self.timemapdict = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemapdict:
            self.timemapdict[key] = [(timestamp, value)]
        else:
            self.timemapdict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timemapdict[key]
        l , r = 0, len(arr) - 1
        value = ""

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                value = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return value


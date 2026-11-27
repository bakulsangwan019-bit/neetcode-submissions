class TimeMap:
    
    def __init__(self):
        self.timestamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamp:
            self.timestamp[key] = []
        self.timestamp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp:
            return ""
            
        timestamps = self.timestamp[key]
        left = 0
        right = len(timestamps)-1

        while right >= left:
            mid = (left+right)//2
            if timestamps[mid][0] <= timestamp:
                if timestamps[mid][0] == timestamp:
                    right = mid
                    break
                else:
                    left = mid + 1
            else:
                right = mid - 1
                
        if right >= 0:
            return(timestamps[right][1])
        else:
            return("")

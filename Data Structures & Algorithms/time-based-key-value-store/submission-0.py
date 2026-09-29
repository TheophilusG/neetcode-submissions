class TimeMap:

    def __init__(self):
        self.hashs = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashs[key] = [value, timestamp] 

    def get(self, key: str, timestamp: int) -> str:
        
        for x in self.hashs:
            if x == key:
                return self.hashs[key][0]

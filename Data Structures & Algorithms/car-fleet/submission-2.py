class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #postion of the car array = postion of ith card [i] in miles
        # speed of the car array = speed[i] speed of the car in m/hour 

        #destination = postion[target] miles 

        carfleet = []
        pair = [(p, s) for p, s in zip(position, speed)]

        pair.sort(reverse=True)
        for p, s in pair:
            carfleet.append((target-p)/s)
            if len(carfleet) >=2:
                carfleet.pop()
        return len(carfleet)
        #for i in range(len(postion)):
         


        

        
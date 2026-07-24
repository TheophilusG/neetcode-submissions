class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #postion of the car array = postion of ith card [i] in miles
        #speed of the car array = speed[i] speed of the car in m/hour 
        
        # creating pair of the postion, speed 
        # after soring the cars based on the location 
        # we can check if the car behind reaches the destination <= the car ahead 
                # they must have met in the middle hence a car fleet
                # time to destination = (destination - positon of card) / speed of the car 
        
        # we can use the time 
        # we keep the ttd of the head car(
            #delete ttd of the car behind

        # we go from right to left of the sorted postions of the car 
            # add the front car to the stack 
            # add the behind car to the stack
                #compare of ttd of front > ttd of the back 
                    #pop the top of the stack 
                
        
        pairs = [[p,s] for p, s in zip(position, speed)] #creating a pair of two arrays 

        car_fleet = []
        for p, s in sorted(pairs)[::-1]: #we are reversing the sorted order
            car_fleet.append((target-p)/s)
            if len(car_fleet) >= 2 and car_fleet[-1]<= car_fleet[-2]:
                car_fleet.pop()
        return len(car_fleet)






         


        

        
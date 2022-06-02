class Solution:
    def distanceBetweenBusStops(self, distance: [int], start: int, destination: int) -> int:
        a=0
        b=0
        if start>destination:start,destination=destination,start
        for i in range(start,destination):
            a+=distance[i]
        b=sum(distance)-a
        return min(a,b)
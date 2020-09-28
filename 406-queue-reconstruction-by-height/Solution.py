from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if len(people) <= 1:
            return people
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        new_people = [people[0]]
        for i in people[1:]:
            new_people.insert(i[1], i)
        return new_people

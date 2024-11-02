import bisect
#using bisect because bisect_left is effectively binary search


class StateList:
    def __init__(self):
        self.states = []

    def __insert__(self, latest_state_to_insert):
        #check first
        insert_point = bisect.bisect_left(self.states, latest_state_to_insert)
        #if not already in let's put it in
        #checks that the insert point is somewhere in and that it's not a value already there
        if insert_point >= len(self.states) or self.states[insert_point] != latest_state_to_insert:
            self.states.insert(insert_point, latest_state_to_insert)

    def __contains__(self, latest_state_to_insert):
        position = bisect.bisect_left(self.states, latest_state_to_insert)
        return position < len(self.states) and self.states[position] == latest_state_to_insert


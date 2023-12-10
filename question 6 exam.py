class PosIntChecker:
    def __init__(self, strlist):
        if isinstance(strlist, list): # first precondition, checking for list input type
            if not all(isinstance(x, str) for x in strlist): # second precondition, checking for str type in input list
                print("List must only contain strings")
            else:
                self._strlist = strlist
        else:
            print("Input needs to be a list")
        
        self._posintlist = [] # empty list to add all positive integers to

    def checker(self):
        for i in self._strlist:
            if i.isdigit():
                str_to_int = int(i)
                if str_to_int >= 1:
                    self._posintlist.append(str_to_int)
        
        if not all(isinstance(x, int) for x in self._posintlist): # First postcondition, ensuring all elements of new list are ints
            print("All elements of result list must be integers") # prints error if they're not.
        if not all(x >= 1 for x in self._posintlist): # Second postcondition, ensuring that all ints are positive
            print("All elements must be positive integers") # prints error if they're not.

        print(self._posintlist)
            




mock_list = ["Only letters",
             "23",
             "-44",
             "Letters here",
             "5"]

positive_integer_check = PosIntChecker(mock_list)
positive_integer_check.checker()
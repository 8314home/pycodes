
# ex-3 Write a Python program to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
# These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.


class py_solution:
    def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

# 4. Write a Python class to get all possible unique subsets from a set of distinct integers. - Go to the editor
# Input : [4, 5, 6]
# Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]


class Py_Sol_Comb(object):
    def combinations_elems(self, l):
        import itertools
        l_final = []
        k = 0
        while k <= len(l):
            for i in itertools.combinations(l, k):
    #   k is deciding at a time how many numbers are being taken
    #   combinations(iterable, r) --> combinations object
    #   Return successive r-length combinations of elements in the iterable.
                l_final.append(list(i))
            k += 1
        return l_final


class SumFinder(object):

    def __init__(self):
        self.sum_finder_dict = dict()

    def sum_finder_function(self, list_of_num: list, target_num: int):
        for i, value in enumerate(list_of_num):
            if (target_num - value) in self.sum_finder_dict:
                return i, self.sum_finder_dict[(target_num - value)]
            else:
                self.sum_finder_dict[value] = i
        return None, None


if __name__ == "__main__":
    print(py_solution().is_valid_parenthese("(){}[]"))
    print(py_solution().is_valid_parenthese("()[{)}"))
    print(py_solution().is_valid_parenthese("()"))

    source_list = [10,11,9,30,15,20]
    target_value = 50
    sf = SumFinder()
    a, b = sf.sum_finder_function(source_list, target_value)
    print(f"Sum finder combination index a-{a} , b-{b} "
          f"from list -{source_list} for target value- {target_value} 0 based index")

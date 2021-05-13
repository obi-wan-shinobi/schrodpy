class subSpace:
    def __init__(self,lb, ub):
        self.lower_limit = lb
        self.upper_limit = ub

    def __str__(self):
        return f'Sub Space: (boundaries: {lower_limit, upper_limit})'

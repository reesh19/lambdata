"""Common and useful functions"""

class DFAnalysis:

    def __init__(self , DataFrame):
        self.df = DataFrame

    def null_count(self):
        self.df.isnull().sum().sum()
    
    def randomize(self, seed=19)
        self.df.shuffle( random_state = seed )

df = pd.DataFrame( { "A" : [ 1 , 2 , 3 ] , 
                     "B" : [ 4 , 5 , 6 ] , 
                     "C" : [ 7 , 8 , 9 ] } )

test = helper_function(df)

print( test.null_count() )
print()
print( test.randomize( 19 ) )
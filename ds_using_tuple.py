zoo = ('python', 'elephant', 'penguin')
print('Number of animals in zoo is', len(zoo))

new_zoo = ('monkey', 'camel', zoo)
print('number of cages in the new zoo is', len(new_zoo))
print('All animals in the new zoo are', new_zoo)
print('animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', zoo[2])
print('Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))
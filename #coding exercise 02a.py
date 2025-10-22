#coding exercise 02a.2
#a = int(input('Enter A: '))
#b = int(input('Enter B: '))
#if (a % 2) == 0 and (b % 2) == 0:
#    print('both numbers are even. ')

#def monkey_trouble(a_smile, b_smile)
#    if a_smile and b_smile:
#        print (True)
#    elif (not a_smile) and (not b_smile):
#        print (True)
#    else:
#        print (False)
#
#    if a_smile == b_smile:
#        print (True)
#    else:
#        print (False)

#n = 1
#while n <= 5:
#    print(n)
#    n = n + 1

#for x in range(1, 16, 3):
#        print(f'{x = }')
#
#for y in range(1, 16, 3):
#        print(f'{y = }')
#
#for z in range(1, 16, 3):
#        print(f'{z = }')

# coding excercise 02b.2 (hard mode)
#
#x = 11
#
#estimate = x/2
#epsilon = 0.00001
#while abs(estimate ** 2 - x) > epsilon:
#    adjustment = abs(estimate ** 2 - x) / 4
#    if (estimate ** 2 -x) < 0:
#        # our estimate is too big
#        estimate += adjustment
#    else:
#        # our estimate is too small
#        estimate -= adjustment
#print(f'{estimate}')
#print(f'{math.sqrt(x) = }')

#option homework problem
#max = 1000
#total = 0
#for i in range(1, max):
#    if (i % 3) == 0 or (i % 5) == 0:
#        #print(f'{i = }')
#        total += i
#print(f'the sum of multiples of 3 & 5: {total}')
#
#for i in range(100000000000000000):
#    pass 

#n = 0
#while n < 10:
#   m = n - 1

#customer_name = 'barbara'
#spam = f'''
#dear {customer_name},

#buy more of our stuff, we're broke.
#
#sincerely,
#the company
#'''
#
#multiline = 'line 1\nline 2'
#
#print(f'{spam[2:20:3] = }')
#print(f'{spam[::-1] = }')
#print(f'{len(spam) = }')
#
#for f in multiline:
#    print(f'{f = }')
#
##coding excersise 03a.1
#full_name =  'ahmed abdullah'
#first_name = ''
#last_name = ''
#space_index = -1
#for index in range(len(full_name)):
#   if full_name[index] == ' ':
#      space_index = index
#      break
#if space_index != -1:
#    first_name = full_name[0:space_index]
#    last_name = full_name[space_index + 1:]
#else:
#    first_name = full_name
#    last_name = ''
#print (f'{first_name = }')
#print (f'{last_name = }')
# When looping over range(2, 5), the numbers included are 2, 3, and 4.

# The most appropriate data structure is a list.
# A list is the most appropriate data structure for this purpose.


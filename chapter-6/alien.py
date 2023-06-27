alien_0 = {'x-position': 0, 'points': 5, 'y-position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x-position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x-position'] = alien_0['x-position'] + x_increment
print('New x-position: ' + str(alien_0['x-position']))
alien_0['speed'] = 'fast'
print(alien_0)

del alien_0['points']
print(alien_0)
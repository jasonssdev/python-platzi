# List

dj_artists = ['Fred Again', 'Tiesto', 'Armin Van Buren', 'James Hype'] 

time_tracks = [3.5, 5.8, 10.56, 5.3, 1.9]

print(len(dj_artists))
print(len(time_tracks))

print(dj_artists[0])
print(dj_artists[0:3])

print(max(time_tracks))
print(min(time_tracks))

time_tracks.append(False)
print(time_tracks)

time_tracks.insert(0, 0.0)
print(time_tracks)

print(time_tracks.index(0.0))

print(time_tracks.pop(-1))

a = [1,2,3,4,5]
b = a

print(a)
print(b)

del a [0]

print(id(a))
print(id(b))

c = a[:]

print(id(a))
print(id(b))
print(id(c))

a.append(6)
print(id(a))
print(id(b))
print(id(c))


matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix[0][1])
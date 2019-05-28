#https://www.codechef.com/problems/JOHNY

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    songs = [int(__) for __ in input().strip().split()]
    k = int(input().strip()) - 1
    j_song = songs[k]
    position = 1
    for song in songs:
        if song < j_song: position += 1
    print(position)
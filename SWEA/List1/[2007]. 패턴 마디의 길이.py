# 문제 조건이 이상하다. 명세가.. 흠.
t = int(input())

for _ in range(1, t + 1):
	string = ''
	word = input()
	res = 0
	#
	for i in range(len(word)):
		# 문자를 하나씩 임시 문자열 string에 추가
		string += word[i]
		# 지금까지 쌓인 string이 이 다음 문자열에서 반복되는지 체크
		if string == word[i + 1:i + len(string) + 1]:
			res = len(string)
			# break를 넣어 주어야 이 문제에 맞는 듯
			# 없는 게 문맥상으로는 더 말이 된다.
			break

	print('#{} {}'.format(_, res))
'''
3
KOREAKOREAKOREAKOREAKOREAKOREA
SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
GALAXYGALAXYGALAXYGALAXYGALAXY

5
7
6
'''

def solution(genres, plays):
    answer = []
    gensum = {}
    musicnum = {}

    # 장르별 총 재생 수 계산 및 각 곡의 재생 수 저장
    for i in range(len(genres)):
        if genres[i] in gensum:
            gensum[genres[i]] += plays[i]
        else:
            gensum[genres[i]] = plays[i]
        # musicnum에는 각 곡의 인덱스와 재생 수 저장
        if genres[i] in musicnum:
            musicnum[genres[i]].append((i, plays[i]))
        else:
            musicnum[genres[i]] = [(i, plays[i])]

    # 장르별 총 재생 수를 기준으로 내림차순 정렬
    total = sorted(gensum.items(), key=lambda x: x[1], reverse=True)

    # 각 장르별로 상위 두 곡 선택
    for genre, _ in total:
        # 해당 장르 내에서 재생 횟수 기준으로 내림차순 정렬
        songs = sorted(musicnum[genre], key=lambda x: x[1], reverse=True)
        # 상위 두 곡의 인덱스를 answer에 추가
        answer.extend([song[0] for song in songs[:2]])

    return answer
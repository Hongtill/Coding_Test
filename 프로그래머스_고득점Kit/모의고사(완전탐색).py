def solution(answers):
    answer = []
    
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    scores = [0, 0, 0]
    
    for i, answer in enumerate(answers):
        # 1번 수포자 채점
        if answer == patterns[0][i % len(patterns[0])]:
            scores[0] += 1
        # 2번 수포자 채점
        if answer == patterns[1][i % len(patterns[1])]:
            scores[1] += 1
        # 3번 수포자 채점
        if answer == patterns[2][i % len(patterns[2])]:
            scores[2] += 1
        
    max_score = max(scores)
    
    answer = []

    for i, score in enumerate(scores):
        if score == max_score:
            answer.append(i + 1)
    
    
    return answer

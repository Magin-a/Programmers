def solution(A, B):
    answer = 0 #최종 출력 결과
    #두 팀 배정받은 수 정열
    A.sort()
    B.sort()
    
    
    i_a, i_b = 0, 0 #각팀 번호 index
    while len(B) != i_b: 
        #A팀의 수와 i_b 팀 수 비교
        if A[i_a] < B[i_b]:
            answer += 1
            i_a += 1
            i_b += 1
        
        else:
            i_b += 1
            
    
    return answer #B팀이 얻는 최고 점수

A, B = [2, 2, 2, 2], [2,2,6,8]
print(solution(A, B))

#1) 각팀의 숫자 배정
#2) !!최소 숫자로 승리!!

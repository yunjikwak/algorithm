import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    
    T = int(input())
    
    # 방향: U D L R
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    DIR_MAP = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    OPPOSITE = [1, 0, 3, 2]
    
    for _ in range(T):
        N, M = map(int, input().split())
        
        # 구슬 정보를 리스트로 저장
        marbles = []
        for _ in range(M):
            line = input().strip().split()
            x, y, d_str = int(line[0]) - 1, int(line[1]) - 1, line[2]
            d = DIR_MAP[d_str]
            marbles.append((x, y, d))
        
        # 최적화: 구슬이 없으면 바로 0 출력
        if not marbles:
            print(0)
            continue
        
        # 시뮬레이션 - 더 aggressive한 최적화
        seen_states = set()
        
        for round_num in range(2 * N):
            if not marbles:
                break
            
            # 상태 해시를 만들어 순환 패턴 감지
            state_hash = tuple(sorted(marbles))
            if state_hash in seen_states:
                break
            seen_states.add(state_hash)
            
            # 위치별 구슬 개수를 직접 계산
            position_count = {}
            position_dirs = {}
            
            # 각 구슬을 이동시키기
            for x, y, d in marbles:
                nx, ny = x + dx[d], y + dy[d]
                
                # 경계 내부인 경우
                if 0 <= nx < N and 0 <= ny < N:
                    pos = (nx, ny)
                else:
                    # 경계에 부딪힌 경우 반대 방향으로 반사
                    pos = (x, y)
                    d = OPPOSITE[d]
                
                if pos not in position_count:
                    position_count[pos] = 0
                    position_dirs[pos] = []
                
                position_count[pos] += 1
                position_dirs[pos].append(d)
            
            # 다음 라운드 구슬들 생성 (충돌하지 않은 구슬들만)
            marbles = []
            for pos, count in position_count.items():
                if count == 1:
                    x, y = pos
                    marbles.append((x, y, position_dirs[pos][0]))
        
        print(len(marbles))

solve()
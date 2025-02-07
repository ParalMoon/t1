import pygame

# Pygame 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("큐브 시뮬레이션")

# 색상 표

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
PINK = (255, 182, 193)
BLUE = (50, 50, 255)
CYAN = (0, 255, 255)

color = {

"WHITE" : (255, 255, 255),
"BLACK" : (0, 0, 0),
"RED" : (200, 50, 50),
"PINK" : (255, 182, 193),
"BLUE" : (50, 50, 255),
"CYAN" : (0, 255, 255)

}

# 노드 위치 정의
node_positions = {
    1: (100, 50), 2: (300, 50),
    3: (150, 150), 4: (250, 150),
    5: (150, 250), 6: (250, 250),
    7: (100, 350), 8: (300, 350)
}

# 노드 라벨 (기본 숫자)
node_labels = {n : str(n) for n in range(1,9)}
node_colors = {1: (200, 50, 50), 2: (255, 182, 193), 3: (50, 50, 255), 
               4: (0, 255, 255), 5: (255, 182, 193), 6: (200, 50, 50), 7: (0, 255, 255), 8: (50, 50, 255)}

# 회전할 노드 그룹 정의
rotating_node_out = [1, 2, 8, 7]
rotating_node_in = [3, 4, 6, 5]
rotating_node_left = [1, 3, 5, 7]
rotating_node_right = [4, 2, 8, 6]
rotating_node_up = [1, 2, 4, 3]
rotating_node_down = [5, 6, 8, 7]

# Pygame 폰트 설정 (최적화)
font = pygame.font.Font(None, 36)

# 게임 루프 변수
running = True
clock = pygame.time.Clock()


# 드래그 관련 변수
dragging_node = None

def draw_nodes():
    """현재 노드들을 화면에 그림"""
    screen.fill(WHITE)  # 배경 지우기
    for node, pos in node_positions.items():
        pygame.draw.circle(screen, node_colors[int(node_labels[node])], pos, 20)  # 원으로 노드 표현
        text = font.render(node_labels[node], True, BLACK)
        screen.blit(text, (pos[0] - 10, pos[1] - 10))  # 숫자 표시
    pygame.display.update()  # 화면 업데이트


def rotate_nodes(clockwise, rotate_node):
    """노드 그룹을 시계 방향 또는 반시계 방향으로 회전"""
    global node_labels 

    new_labels = {}  # 임시 딕셔너리 사용 (안전한 업데이트)
    
    if clockwise:
        for i in range(len(rotate_node)):
            new_labels[rotate_node[i]] = node_labels[rotate_node[i - 1]]
    else:
        for i in range(len(rotate_node)):
            new_labels[rotate_node[i - 1]] = node_labels[rotate_node[i]]

    # 기존 노드 라벨을 업데이트
    node_labels.update(new_labels)


# 최초 화면 그리기
draw_nodes()

# 게임 루프
while running:
    clock.tick(60)  # 초당 60 프레임 유지

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                print("O 키 눌림 - 바깥쪽 노드 시계 방향 회전")
                rotate_nodes(True, rotating_node_out)
            elif event.key == pygame.K_p:
                print("P 키 눌림 - 바깥쪽 노드 반시계 방향 회전")
                rotate_nodes(False, rotating_node_out)

            elif event.key == pygame.K_d:
                print("D 키 눌림 - 안쪽 노드 시계 방향 회전")
                rotate_nodes(True, rotating_node_in)
            elif event.key == pygame.K_f:
                print("F 키 눌림 - 안쪽 노드 반시계 방향 회전")
                rotate_nodes(False, rotating_node_in)

            elif event.key == pygame.K_a:
                print("A 키 눌림 - 왼쪽 노드 시계 방향 회전")
                rotate_nodes(True, rotating_node_left)
            elif event.key == pygame.K_s:
                print("S 키 눌림 - 왼쪽 노드 반시계 방향 회전")
                rotate_nodes(False, rotating_node_left)

            elif event.key == pygame.K_g:
                print("G 키 눌림 - 오른쪽 노드 시계 방향 회전")
                rotate_nodes(True, rotating_node_right)
            elif event.key == pygame.K_h:
                print("H 키 눌림 - 오른쪽 노드 반시계 방향 회전")
                rotate_nodes(False, rotating_node_right)

            elif event.key == pygame.K_e:
                print("E 키 눌림 - 위쪽 노드 시계 방향 회전")
                rotate_nodes(True, rotating_node_up)
            elif event.key == pygame.K_r:
                print("R 키 눌림 - 위쪽 노드 반시계 방향 회전")
                rotate_nodes(False, rotating_node_up)

            elif event.key == pygame.K_c:
                print("C 키 눌림 - 아래쪽 노드 시계 방향 회전")
                rotate_nodes(True, rotating_node_down)
            elif event.key == pygame.K_v:
                print("V 키 눌림 - 아래쪽 노드 반시계 방향 회전")
                rotate_nodes(False, rotating_node_down)

            # 노드 다시 그리기
            draw_nodes()


        # 마우스 클릭 이벤트 (노드 선택)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for node, pos in node_positions.items():
                distance = ((mouse_x - pos[0]) ** 2 + (mouse_y - pos[1]) ** 2) ** 0.5
                if distance < 20:  # 반지름 20 이내 클릭 시 선택
                    dragging_node = node
                    break
        # 마우스 이동 이벤트 (노드 드래그)
        elif event.type == pygame.MOUSEMOTION and dragging_node is not None:
            node_positions[dragging_node] = event.pos
            draw_nodes()

        # 마우스 버튼을 놓았을 때 (드래그 종료)
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging_node = None


pygame.quit()

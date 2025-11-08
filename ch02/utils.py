import numpy as np
import matplotlib.pyplot as plt

# 투입 데이터
inputs = [[0, 0], [1, 0], [0, 1], [1, 1]]

def visualize(w1, w2, b, output):
    if w2 == 0: return

    # 결정경계 시각화용 변수
    x1_range = np.linspace(-0.5, 1.5, 100)
    x2_boundary = (-w1 / w2) * x1_range - (b / w2)
    y2s = [1.5, -0.5]
    color_output_1 = 'lightcoral'
    color_output_0 = 'lightblue'

    # 그래프 그리기
    plt.figure(figsize=(6, 6))
    plt.plot(x1_range, x2_boundary, 'g-', label="boundary")

    if w2 > 0:
        plt.fill_between(x1_range, x2_boundary, y2s[0], color=color_output_1, alpha=0.3)
        plt.fill_between(x1_range, x2_boundary, y2s[1], color=color_output_0, alpha=0.3)
    else:
        plt.fill_between(x1_range, x2_boundary, y2s[::-1][0], color=color_output_1, alpha=0.3)
        plt.fill_between(x1_range, x2_boundary, y2s[::-1][1], color=color_output_0, alpha=0.3)

    # 범례 중복 생성 방지용 상태 변수
    plotted_output_0 = False
    plotted_output_1 = False

    # 입력 데이터를 산점도로 표시
    for [x1, x2] in inputs:
        print(f"{x1}, {x2} → {output.__name__} → {output(x1, x2)}")
        is_activate = output(x1, x2) == 1
        current_output = output(x1, x2)

        if current_output == 0:
            # 출력 0 (비활성화)는 파란색 동그라미로 표시
            label = 'Output 0' if not plotted_output_0 else None
            plt.plot(x1, x2, 'bo', markersize=10, markeredgecolor='black', label=label)
            plotted_output_0 = True
        else:
            # 출력 1 (활성화)는 빨간색 세모로 표시
            label = 'Output 1' if not plotted_output_1 else None
            plt.plot(x1, x2, 'r^', markersize=10, markeredgecolor='black', label=label)
            plotted_output_1 = True

    plt.title(fr'{output.__name__} gate perceptron → $\mathbf{{w}}=({w1}, {w2}), \mathbf{{b}}={b}$', fontsize=14)
    plt.xlim(-0.5, 1.5)
    plt.ylim(-0.5, 1.5)
    plt.legend(loc='lower left')

    plt.show()
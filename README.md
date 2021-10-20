# branch-and-bound-algorithm

Regret-based Branch & Bound algorithm by Litte et al.(1963)

## 요구사항

### 1. jobs matrix

- jobs의 개수는 최소 10개
  - 커맨드 라인에서 jobs의 개수 n을 입력받을 수 있다
  - 매트릭스는 nxn 사이즈로 초기화 된다
- 각 job의 set-up time은 [1, 30] 범위의 실수로 랜덤 생성된다
- (i, j) _s.t. i==j_ 원소의 경우 무한값(불가능 루트)으로 초기화 된다
- 연산
  - show() : show matrix
  - size() : return [row 개수, column 개수]
  - get_element(i, j) : return (i, j) element
  - pick_row(i) : row i
  - pick_column(j) : get column j
  - min(i, axis)
    - axis = 0 : get min value of row i
    - axis = 1 : get min value of column i
  - delete(i, axis)
    - axis = 0 : delete row i
    - axis = 1 : delete column i
  - reduce(i, axis)
    - update (i, j) s.t. [ i-> * -> j] 가 불가능한 경우 // 고민할 필요
  - calculate_regret(i, j) : (i, j) 원소의 regret을 구한다

# branch-and-bound-algorithm

Regret-based Branch & Bound algorithm by Litte et al.(1963)

## 요구사항

### 1. jobs matrix

- [ ] Matrix 초기화
  - [ ] 커맨드 라인에서 jobs의 개수 n을 입력받을 수 있다
  - [x] 매트릭스는 nxn 사이즈로 초기화 된다
- [x] 각 job의 set-up time은 [1, 30] 범위의 정수로 랜덤 생성된다
- [x] (i, j) _s.t. i==j_ 원소의 경우 무한값(불가능 루트)으로 초기화 된다
- 연산
  - [x] show() : show matrix
  - [x] size() : return [row 개수, column 개수]
  - [x] get_element(i, j) : return (i, j) element
  - [x] pick_row(i) : row i
  - [x] pick_column(j) : get column j
  - [x] min(i, axis)
    - axis = 0 : get min value of row i
    - axis = 1 : get min value of column i
  - [ ] delete(i, axis)
    - axis = 0 : delete row i
    - axis = 1 : delete column i
  - [x] reduce(i, axis)
    - [x] lower bound 누적
    - [x] row_reduce
    - [x] col_reduce
    - [x] lower_bound 업데이트
  - [ ] calculate_regret(i, j) : (i, j) 원소의 regret을 구한다
  - [ ] update (i, j) s.t. [ i-> * -> j] 가 불가능한 경우 // 고민할 필요

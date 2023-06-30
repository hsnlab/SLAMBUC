graph [
  directed 1
  name "test_tree_par_btree"
  node [
    id 0
    label "P"
  ]
  node [
    id 1
    label "1"
    time 81
    mem 2
  ]
  node [
    id 2
    label "2"
    time 84
    mem 1
  ]
  node [
    id 3
    label "3"
    time 40
    mem 1
  ]
  node [
    id 4
    label "4"
    time 39
    mem 1
  ]
  node [
    id 5
    label "5"
    time 31
    mem 2
  ]
  node [
    id 6
    label "6"
    time 80
    mem 1
  ]
  node [
    id 7
    label "7"
    time 96
    mem 1
  ]
  node [
    id 8
    label "8"
    time 98
    mem 2
  ]
  node [
    id 9
    label "9"
    time 64
    mem 1
  ]
  node [
    id 10
    label "10"
    time 34
    mem 1
  ]
  edge [
    source 0
    target 1
    rate 1
    data 19
  ]
  edge [
    source 1
    target 2
    rate 2
    data 9
  ]
  edge [
    source 2
    target 3
    rate 3
    data 8
  ]
  edge [
    source 3
    target 4
    rate 2
    data 19
  ]
  edge [
    source 3
    target 5
    rate 1
    data 7
  ]
  edge [
    source 3
    target 6
    rate 2
    data 9
  ]
  edge [
    source 6
    target 7
    rate 2
    data 10
  ]
  edge [
    source 6
    target 8
    rate 2
    data 11
  ]
  edge [
    source 8
    target 9
    rate 3
    data 5
  ]
  edge [
    source 9
    target 10
    rate 3
    data 14
  ]
]

graph [
  directed 1
  name "test_tree_par"
  node [
    id 0
    label "P"
  ]
  node [
    id 1
    label "1"
    time 86
    mem 3
  ]
  node [
    id 2
    label "2"
    time 72
    mem 1
  ]
  node [
    id 3
    label "3"
    time 68
    mem 1
  ]
  node [
    id 4
    label "4"
    time 4
    mem 1
  ]
  node [
    id 5
    label "5"
    time 40
    mem 1
  ]
  node [
    id 6
    label "6"
    time 8
    mem 3
  ]
  node [
    id 7
    label "7"
    time 61
    mem 1
  ]
  node [
    id 8
    label "8"
    time 14
    mem 2
  ]
  node [
    id 9
    label "9"
    time 88
    mem 3
  ]
  node [
    id 10
    label "10"
    time 48
    mem 1
  ]
  edge [
    source 0
    target 1
    rate 1
    data 20
  ]
  edge [
    source 1
    target 2
    rate 1
    data 2
  ]
  edge [
    source 2
    target 3
    rate 2
    data 17
  ]
  edge [
    source 2
    target 4
    rate 3
    data 14
  ]
  edge [
    source 3
    target 5
    rate 2
    data 3
  ]
  edge [
    source 3
    target 6
    rate 3
    data 12
  ]
  edge [
    source 4
    target 7
    rate 1
    data 9
  ]
  edge [
    source 6
    target 8
    rate 1
    data 17
  ]
  edge [
    source 8
    target 9
    rate 1
    data 15
  ]
  edge [
    source 8
    target 10
    rate 2
    data 7
  ]
]

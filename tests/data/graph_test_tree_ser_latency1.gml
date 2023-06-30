graph [
  directed 1
  name "test_tree_ser_latency1"
  node [
    id 0
    label "P"
  ]
  node [
    id 1
    label "1"
    time 14
    mem 1
  ]
  node [
    id 2
    label "2"
    time 17
    mem 1
  ]
  node [
    id 3
    label "3"
    time 71
    mem 1
  ]
  node [
    id 4
    label "4"
    time 79
    mem 2
  ]
  node [
    id 5
    label "5"
    time 67
    mem 1
  ]
  node [
    id 6
    label "6"
    time 27
    mem 1
  ]
  node [
    id 7
    label "7"
    time 99
    mem 1
  ]
  node [
    id 8
    label "8"
    time 42
    mem 1
  ]
  node [
    id 9
    label "9"
    time 25
    mem 1
  ]
  node [
    id 10
    label "10"
    time 96
    mem 1
  ]
  edge [
    source 0
    target 1
    rate 2
    data 19
  ]
  edge [
    source 1
    target 2
    rate 3
    data 20
  ]
  edge [
    source 2
    target 3
    rate 1
    data 9
  ]
  edge [
    source 2
    target 4
    rate 3
    data 2
  ]
  edge [
    source 2
    target 5
    rate 3
    data 6
  ]
  edge [
    source 5
    target 6
    rate 3
    data 9
  ]
  edge [
    source 6
    target 7
    rate 1
    data 6
  ]
  edge [
    source 7
    target 8
    rate 1
    data 10
  ]
  edge [
    source 8
    target 9
    rate 1
    data 16
  ]
  edge [
    source 8
    target 10
    rate 2
    data 17
  ]
]

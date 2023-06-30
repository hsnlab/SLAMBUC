graph [
  directed 1
  name "test_tree_ser_latency2"
  node [
    id 0
    label "P"
  ]
  node [
    id 1
    label "1"
    time 4
    mem 1
  ]
  node [
    id 2
    label "2"
    time 9
    mem 3
  ]
  node [
    id 3
    label "3"
    time 83
    mem 3
  ]
  node [
    id 4
    label "4"
    time 74
    mem 2
  ]
  node [
    id 5
    label "5"
    time 5
    mem 2
  ]
  node [
    id 6
    label "6"
    time 75
    mem 1
  ]
  node [
    id 7
    label "7"
    time 75
    mem 1
  ]
  node [
    id 8
    label "8"
    time 95
    mem 1
  ]
  node [
    id 9
    label "9"
    time 79
    mem 2
  ]
  node [
    id 10
    label "10"
    time 62
    mem 1
  ]
  edge [
    source 0
    target 1
    rate 2
    data 6
  ]
  edge [
    source 1
    target 2
    rate 1
    data 6
  ]
  edge [
    source 1
    target 3
    rate 1
    data 20
  ]
  edge [
    source 1
    target 4
    rate 3
    data 18
  ]
  edge [
    source 3
    target 5
    rate 2
    data 1
  ]
  edge [
    source 4
    target 6
    rate 3
    data 15
  ]
  edge [
    source 5
    target 7
    rate 2
    data 18
  ]
  edge [
    source 6
    target 8
    rate 1
    data 11
  ]
  edge [
    source 6
    target 9
    rate 2
    data 19
  ]
  edge [
    source 7
    target 10
    rate 1
    data 18
  ]
]

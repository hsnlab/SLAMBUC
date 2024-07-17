# Table of Contents

* [slambuc](#slambuc)
* [slambuc.alg.service.common](#slambuc.alg.service.common)
  * [Flavor](#slambuc.alg.service.common.Flavor)
    * [mem](#slambuc.alg.service.common.Flavor.mem)
    * [ncore](#slambuc.alg.service.common.Flavor.ncore)
    * [cfactor](#slambuc.alg.service.common.Flavor.cfactor)
    * [name](#slambuc.alg.service.common.Flavor.name)
* [slambuc.alg.service](#slambuc.alg.service)
* [slambuc.alg.chain.ser.greedy](#slambuc.alg.chain.ser.greedy)
  * [ichain\_blocks](#slambuc.alg.chain.ser.greedy.ichain_blocks)
  * [greedy\_ser\_chain\_partitioning](#slambuc.alg.chain.ser.greedy.greedy_ser_chain_partitioning)
* [slambuc.alg.chain.ser.ilp](#slambuc.alg.chain.ser.ilp)
  * [ifeasible\_greedy\_blocks](#slambuc.alg.chain.ser.ilp.ifeasible_greedy_blocks)
  * [ifeasible\_blocks](#slambuc.alg.chain.ser.ilp.ifeasible_blocks)
  * [build\_chain\_cfg\_model](#slambuc.alg.chain.ser.ilp.build_chain_cfg_model)
  * [chain\_cfg\_partitioning](#slambuc.alg.chain.ser.ilp.chain_cfg_partitioning)
  * [recreate\_blocks\_from\_xvars](#slambuc.alg.chain.ser.ilp.recreate_blocks_from_xvars)
  * [extract\_blocks\_from\_xvars](#slambuc.alg.chain.ser.ilp.extract_blocks_from_xvars)
  * [build\_greedy\_chain\_mtx\_model](#slambuc.alg.chain.ser.ilp.build_greedy_chain_mtx_model)
  * [build\_chain\_mtx\_model](#slambuc.alg.chain.ser.ilp.build_chain_mtx_model)
  * [chain\_mtx\_partitioning](#slambuc.alg.chain.ser.ilp.chain_mtx_partitioning)
  * [recreate\_blocks\_from\_xmatrix](#slambuc.alg.chain.ser.ilp.recreate_blocks_from_xmatrix)
  * [extract\_blocks\_from\_xmatrix](#slambuc.alg.chain.ser.ilp.extract_blocks_from_xmatrix)
* [slambuc.alg.chain.ser](#slambuc.alg.chain.ser)
* [slambuc.alg.chain.sp.min](#slambuc.alg.chain.sp.min)
  * [hop\_limited\_shortest\_path](#slambuc.alg.chain.sp.min.hop_limited_shortest_path)
  * [sp\_chain\_partitioning](#slambuc.alg.chain.sp.min.sp_chain_partitioning)
* [slambuc.alg.chain](#slambuc.alg.chain)
* [slambuc.alg.chain.dp.greedy](#slambuc.alg.chain.dp.greedy)
  * [ichain\_blocks](#slambuc.alg.chain.dp.greedy.ichain_blocks)
  * [greedy\_chain\_partitioning](#slambuc.alg.chain.dp.greedy.greedy_chain_partitioning)
* [slambuc.alg.chain.dp.mtx](#slambuc.alg.chain.dp.mtx)
  * [State](#slambuc.alg.chain.dp.mtx.State)
    * [barr](#slambuc.alg.chain.dp.mtx.State.barr)
    * [cost](#slambuc.alg.chain.dp.mtx.State.cost)
    * [lat](#slambuc.alg.chain.dp.mtx.State.lat)
  * [chain\_partitioning](#slambuc.alg.chain.dp.mtx.chain_partitioning)
  * [extract\_barr](#slambuc.alg.chain.dp.mtx.extract_barr)
  * [vec\_chain\_partitioning](#slambuc.alg.chain.dp.mtx.vec_chain_partitioning)
  * [extract\_vec\_barr](#slambuc.alg.chain.dp.mtx.extract_vec_barr)
* [slambuc.alg.chain.dp.min](#slambuc.alg.chain.dp.min)
  * [min\_chain\_partitioning](#slambuc.alg.chain.dp.min.min_chain_partitioning)
  * [extract\_min\_barr](#slambuc.alg.chain.dp.min.extract_min_barr)
* [slambuc.alg.chain.dp](#slambuc.alg.chain.dp)
* [slambuc.alg.tree.ser.bicriteria](#slambuc.alg.tree.ser.bicriteria)
  * [WeightedSubBTreePart](#slambuc.alg.tree.ser.bicriteria.WeightedSubBTreePart)
    * [weight](#slambuc.alg.tree.ser.bicriteria.WeightedSubBTreePart.weight)
    * [barr](#slambuc.alg.tree.ser.bicriteria.WeightedSubBTreePart.barr)
  * [biheuristic\_btree\_partitioning](#slambuc.alg.tree.ser.bicriteria.biheuristic_btree_partitioning)
  * [biheuristic\_tree\_partitioning](#slambuc.alg.tree.ser.bicriteria.biheuristic_tree_partitioning)
  * [WeightedSubLTreePart](#slambuc.alg.tree.ser.bicriteria.WeightedSubLTreePart)
    * [weight](#slambuc.alg.tree.ser.bicriteria.WeightedSubLTreePart.weight)
    * [top\_lat](#slambuc.alg.tree.ser.bicriteria.WeightedSubLTreePart.top_lat)
    * [mul](#slambuc.alg.tree.ser.bicriteria.WeightedSubLTreePart.mul)
    * [barr](#slambuc.alg.tree.ser.bicriteria.WeightedSubLTreePart.barr)
  * [bifptas\_ltree\_partitioning](#slambuc.alg.tree.ser.bicriteria.bifptas_ltree_partitioning)
  * [bifptas\_tree\_partitioning](#slambuc.alg.tree.ser.bicriteria.bifptas_tree_partitioning)
  * [WeightedDualSubLTreePart](#slambuc.alg.tree.ser.bicriteria.WeightedDualSubLTreePart)
    * [mem](#slambuc.alg.tree.ser.bicriteria.WeightedDualSubLTreePart.mem)
    * [top\_lat](#slambuc.alg.tree.ser.bicriteria.WeightedDualSubLTreePart.top_lat)
    * [mul](#slambuc.alg.tree.ser.bicriteria.WeightedDualSubLTreePart.mul)
    * [barr](#slambuc.alg.tree.ser.bicriteria.WeightedDualSubLTreePart.barr)
  * [bifptas\_dual\_ltree\_partitioning](#slambuc.alg.tree.ser.bicriteria.bifptas_dual_ltree_partitioning)
  * [bifptas\_dual\_tree\_partitioning](#slambuc.alg.tree.ser.bicriteria.bifptas_dual_tree_partitioning)
* [slambuc.alg.tree.ser.pseudo\_mp](#slambuc.alg.tree.ser.pseudo_mp)
  * [isubtree\_cutoffs](#slambuc.alg.tree.ser.pseudo_mp.isubtree_cutoffs)
  * [get\_cpu\_splits](#slambuc.alg.tree.ser.pseudo_mp.get_cpu_splits)
  * [isubtree\_sync\_cutoffs](#slambuc.alg.tree.ser.pseudo_mp.isubtree_sync_cutoffs)
  * [isubtree\_splits](#slambuc.alg.tree.ser.pseudo_mp.isubtree_splits)
  * [pseudo\_mp\_btree\_partitioning](#slambuc.alg.tree.ser.pseudo_mp.pseudo_mp_btree_partitioning)
  * [pseudo\_mp\_ltree\_partitioning](#slambuc.alg.tree.ser.pseudo_mp.pseudo_mp_ltree_partitioning)
* [slambuc.alg.tree.ser.greedy](#slambuc.alg.tree.ser.greedy)
  * [isubtrees\_exhaustive](#slambuc.alg.tree.ser.greedy.isubtrees_exhaustive)
  * [greedy\_ser\_tree\_partitioning](#slambuc.alg.tree.ser.greedy.greedy_ser_tree_partitioning)
* [slambuc.alg.tree.ser.ilp\_cplex](#slambuc.alg.tree.ser.ilp_cplex)
  * [build\_tree\_cfg\_cpo\_model](#slambuc.alg.tree.ser.ilp_cplex.build_tree_cfg_cpo_model)
  * [tree\_cpo\_partitioning](#slambuc.alg.tree.ser.ilp_cplex.tree_cpo_partitioning)
  * [recreate\_subtrees\_from\_cpo\_xdict](#slambuc.alg.tree.ser.ilp_cplex.recreate_subtrees_from_cpo_xdict)
  * [build\_greedy\_tree\_cplex\_model](#slambuc.alg.tree.ser.ilp_cplex.build_greedy_tree_cplex_model)
  * [build\_tree\_cplex\_model](#slambuc.alg.tree.ser.ilp_cplex.build_tree_cplex_model)
  * [tree\_cplex\_partitioning](#slambuc.alg.tree.ser.ilp_cplex.tree_cplex_partitioning)
  * [extract\_subtrees\_from\_cplex\_xmatrix](#slambuc.alg.tree.ser.ilp_cplex.extract_subtrees_from_cplex_xmatrix)
* [slambuc.alg.tree.ser.pseudo](#slambuc.alg.tree.ser.pseudo)
  * [SubBTreePart](#slambuc.alg.tree.ser.pseudo.SubBTreePart)
    * [cost](#slambuc.alg.tree.ser.pseudo.SubBTreePart.cost)
    * [barr](#slambuc.alg.tree.ser.pseudo.SubBTreePart.barr)
  * [pseudo\_btree\_partitioning](#slambuc.alg.tree.ser.pseudo.pseudo_btree_partitioning)
  * [SubLTreePart](#slambuc.alg.tree.ser.pseudo.SubLTreePart)
    * [cost](#slambuc.alg.tree.ser.pseudo.SubLTreePart.cost)
    * [mul](#slambuc.alg.tree.ser.pseudo.SubLTreePart.mul)
    * [barr](#slambuc.alg.tree.ser.pseudo.SubLTreePart.barr)
  * [pseudo\_ltree\_partitioning](#slambuc.alg.tree.ser.pseudo.pseudo_ltree_partitioning)
* [slambuc.alg.tree.ser.ilp](#slambuc.alg.tree.ser.ilp)
  * [ifeasible\_greedy\_subtrees](#slambuc.alg.tree.ser.ilp.ifeasible_greedy_subtrees)
  * [ifeasible\_subtrees](#slambuc.alg.tree.ser.ilp.ifeasible_subtrees)
  * [build\_tree\_cfg\_model](#slambuc.alg.tree.ser.ilp.build_tree_cfg_model)
  * [tree\_cfg\_partitioning](#slambuc.alg.tree.ser.ilp.tree_cfg_partitioning)
  * [tree\_hybrid\_partitioning](#slambuc.alg.tree.ser.ilp.tree_hybrid_partitioning)
  * [extract\_subtrees\_from\_xdict](#slambuc.alg.tree.ser.ilp.extract_subtrees_from_xdict)
  * [recreate\_subtrees\_from\_xdict](#slambuc.alg.tree.ser.ilp.recreate_subtrees_from_xdict)
  * [build\_greedy\_tree\_mtx\_model](#slambuc.alg.tree.ser.ilp.build_greedy_tree_mtx_model)
  * [build\_tree\_mtx\_model](#slambuc.alg.tree.ser.ilp.build_tree_mtx_model)
  * [tree\_mtx\_partitioning](#slambuc.alg.tree.ser.ilp.tree_mtx_partitioning)
  * [recreate\_subtrees\_from\_xmatrix](#slambuc.alg.tree.ser.ilp.recreate_subtrees_from_xmatrix)
  * [extract\_subtrees\_from\_xmatrix](#slambuc.alg.tree.ser.ilp.extract_subtrees_from_xmatrix)
  * [all\_tree\_mtx\_partitioning](#slambuc.alg.tree.ser.ilp.all_tree_mtx_partitioning)
* [slambuc.alg.tree.ser](#slambuc.alg.tree.ser)
* [slambuc.alg.tree.layout.ilp](#slambuc.alg.tree.layout.ilp)
  * [ifeasible\_gen\_subtrees](#slambuc.alg.tree.layout.ilp.ifeasible_gen_subtrees)
  * [build\_gen\_tree\_cfg\_model](#slambuc.alg.tree.layout.ilp.build_gen_tree_cfg_model)
  * [tree\_gen\_hybrid\_partitioning](#slambuc.alg.tree.layout.ilp.tree_gen_hybrid_partitioning)
  * [recreate\_st\_from\_gen\_xdict](#slambuc.alg.tree.layout.ilp.recreate_st_from_gen_xdict)
  * [build\_gen\_tree\_mtx\_model](#slambuc.alg.tree.layout.ilp.build_gen_tree_mtx_model)
  * [tree\_gen\_mtx\_partitioning](#slambuc.alg.tree.layout.ilp.tree_gen_mtx_partitioning)
  * [extract\_st\_from\_gen\_xmatrix](#slambuc.alg.tree.layout.ilp.extract_st_from_gen_xmatrix)
  * [all\_gen\_tree\_mtx\_partitioning](#slambuc.alg.tree.layout.ilp.all_gen_tree_mtx_partitioning)
* [slambuc.alg.tree.layout](#slambuc.alg.tree.layout)
* [slambuc.alg.tree](#slambuc.alg.tree)
* [slambuc.alg.tree.dp.greedy](#slambuc.alg.tree.dp.greedy)
  * [ichains\_exhaustive](#slambuc.alg.tree.dp.greedy.ichains_exhaustive)
  * [ifeasible\_chains](#slambuc.alg.tree.dp.greedy.ifeasible_chains)
  * [greedy\_tree\_partitioning](#slambuc.alg.tree.dp.greedy.greedy_tree_partitioning)
* [slambuc.alg.tree.dp.min](#slambuc.alg.tree.dp.min)
  * [MinTBlock](#slambuc.alg.tree.dp.min.MinTBlock)
    * [w](#slambuc.alg.tree.dp.min.MinTBlock.w)
    * [c](#slambuc.alg.tree.dp.min.MinTBlock.c)
    * [sum\_cost](#slambuc.alg.tree.dp.min.MinTBlock.sum_cost)
    * [cost](#slambuc.alg.tree.dp.min.MinTBlock.cost)
    * [mem](#slambuc.alg.tree.dp.min.MinTBlock.mem)
    * [max\_rate](#slambuc.alg.tree.dp.min.MinTBlock.max_rate)
    * [cpu](#slambuc.alg.tree.dp.min.MinTBlock.cpu)
  * [min\_tree\_partitioning](#slambuc.alg.tree.dp.min.min_tree_partitioning)
  * [extract\_min\_blocks](#slambuc.alg.tree.dp.min.extract_min_blocks)
* [slambuc.alg.tree.dp.seq](#slambuc.alg.tree.dp.seq)
  * [TBlock](#slambuc.alg.tree.dp.seq.TBlock)
    * [w](#slambuc.alg.tree.dp.seq.TBlock.w)
    * [sum\_cost](#slambuc.alg.tree.dp.seq.TBlock.sum_cost)
    * [cumsum](#slambuc.alg.tree.dp.seq.TBlock.cumsum)
    * [mem](#slambuc.alg.tree.dp.seq.TBlock.mem)
    * [max\_rate](#slambuc.alg.tree.dp.seq.TBlock.max_rate)
    * [cpu](#slambuc.alg.tree.dp.seq.TBlock.cpu)
  * [seq\_tree\_partitioning](#slambuc.alg.tree.dp.seq.seq_tree_partitioning)
  * [extract\_blocks](#slambuc.alg.tree.dp.seq.extract_blocks)
* [slambuc.alg.tree.dp.meta](#slambuc.alg.tree.dp.meta)
  * [TPart](#slambuc.alg.tree.dp.meta.TPart)
    * [barr](#slambuc.alg.tree.dp.meta.TPart.barr)
    * [cost](#slambuc.alg.tree.dp.meta.TPart.cost)
  * [meta\_tree\_partitioning](#slambuc.alg.tree.dp.meta.meta_tree_partitioning)
* [slambuc.alg.tree.dp.seq\_state](#slambuc.alg.tree.dp.seq_state)
  * [cacheless\_chain\_partitioning](#slambuc.alg.tree.dp.seq_state.cacheless_chain_partitioning)
  * [stateful\_chain\_partitioning](#slambuc.alg.tree.dp.seq_state.stateful_chain_partitioning)
* [slambuc.alg.tree.dp](#slambuc.alg.tree.dp)
* [slambuc.alg.tree.par.pseudo\_mp](#slambuc.alg.tree.par.pseudo_mp)
  * [pseudo\_par\_mp\_ltree\_partitioning](#slambuc.alg.tree.par.pseudo_mp.pseudo_par_mp_ltree_partitioning)
* [slambuc.alg.tree.par.greedy](#slambuc.alg.tree.par.greedy)
  * [isubtrees\_exhaustive](#slambuc.alg.tree.par.greedy.isubtrees_exhaustive)
  * [greedy\_par\_tree\_partitioning](#slambuc.alg.tree.par.greedy.greedy_par_tree_partitioning)
* [slambuc.alg.tree.par.pseudo](#slambuc.alg.tree.par.pseudo)
  * [SubParBTreePart](#slambuc.alg.tree.par.pseudo.SubParBTreePart)
    * [cost](#slambuc.alg.tree.par.pseudo.SubParBTreePart.cost)
    * [top\_cost](#slambuc.alg.tree.par.pseudo.SubParBTreePart.top_cost)
    * [top\_blk](#slambuc.alg.tree.par.pseudo.SubParBTreePart.top_blk)
    * [barr](#slambuc.alg.tree.par.pseudo.SubParBTreePart.barr)
  * [pseudo\_par\_btree\_partitioning](#slambuc.alg.tree.par.pseudo.pseudo_par_btree_partitioning)
  * [pseudo\_par\_ltree\_partitioning](#slambuc.alg.tree.par.pseudo.pseudo_par_ltree_partitioning)
* [slambuc.alg.tree.par.ilp](#slambuc.alg.tree.par.ilp)
  * [ifeasible\_par\_greedy\_subtrees](#slambuc.alg.tree.par.ilp.ifeasible_par_greedy_subtrees)
  * [ifeasible\_par\_subtrees](#slambuc.alg.tree.par.ilp.ifeasible_par_subtrees)
  * [build\_par\_tree\_cfg\_model](#slambuc.alg.tree.par.ilp.build_par_tree_cfg_model)
  * [tree\_par\_cfg\_partitioning](#slambuc.alg.tree.par.ilp.tree_par_cfg_partitioning)
  * [tree\_par\_hybrid\_partitioning](#slambuc.alg.tree.par.ilp.tree_par_hybrid_partitioning)
  * [build\_greedy\_par\_tree\_mtx\_model](#slambuc.alg.tree.par.ilp.build_greedy_par_tree_mtx_model)
  * [build\_par\_tree\_mtx\_model](#slambuc.alg.tree.par.ilp.build_par_tree_mtx_model)
  * [tree\_par\_mtx\_partitioning](#slambuc.alg.tree.par.ilp.tree_par_mtx_partitioning)
  * [all\_par\_tree\_mtx\_partitioning](#slambuc.alg.tree.par.ilp.all_par_tree_mtx_partitioning)
* [slambuc.alg.tree.par](#slambuc.alg.tree.par)
* [slambuc.alg.ext.greedy](#slambuc.alg.ext.greedy)
  * [get\_bounded\_greedy\_block](#slambuc.alg.ext.greedy.get_bounded_greedy_block)
  * [min\_weight\_greedy\_partitioning](#slambuc.alg.ext.greedy.min_weight_greedy_partitioning)
  * [get\_feasible\_cpath\_split](#slambuc.alg.ext.greedy.get_feasible_cpath_split)
  * [get\_min\_cpath\_split](#slambuc.alg.ext.greedy.get_min_cpath_split)
  * [min\_weight\_partition\_heuristic](#slambuc.alg.ext.greedy.min_weight_partition_heuristic)
  * [min\_lat\_partition\_heuristic](#slambuc.alg.ext.greedy.min_lat_partition_heuristic)
* [slambuc.alg.ext.baseline](#slambuc.alg.ext.baseline)
  * [baseline\_singleton\_partitioning](#slambuc.alg.ext.baseline.baseline_singleton_partitioning)
  * [baseline\_no\_partitioning](#slambuc.alg.ext.baseline.baseline_no_partitioning)
* [slambuc.alg.ext.min\_cut](#slambuc.alg.ext.min_cut)
  * [min\_weight\_subchain\_split](#slambuc.alg.ext.min_cut.min_weight_subchain_split)
  * [min\_weight\_chain\_decomposition](#slambuc.alg.ext.min_cut.min_weight_chain_decomposition)
  * [min\_weight\_ksplit](#slambuc.alg.ext.min_cut.min_weight_ksplit)
  * [min\_weight\_ksplit\_clustering](#slambuc.alg.ext.min_cut.min_weight_ksplit_clustering)
  * [min\_weight\_tree\_clustering](#slambuc.alg.ext.min_cut.min_weight_tree_clustering)
* [slambuc.alg.ext.csp](#slambuc.alg.ext.csp)
  * [encode\_state](#slambuc.alg.ext.csp.encode_state)
  * [decode\_state](#slambuc.alg.ext.csp.decode_state)
  * [ibuild\_gen\_csp\_dag](#slambuc.alg.ext.csp.ibuild_gen_csp_dag)
  * [csp\_tree\_partitioning](#slambuc.alg.ext.csp.csp_tree_partitioning)
  * [csp\_gen\_tree\_partitioning](#slambuc.alg.ext.csp.csp_gen_tree_partitioning)
  * [extract\_grp\_from\_path](#slambuc.alg.ext.csp.extract_grp_from_path)
* [slambuc.alg.ext](#slambuc.alg.ext)
* [slambuc.alg](#slambuc.alg)
  * [T\_BLOCK](#slambuc.alg.T_BLOCK)
  * [T\_PART](#slambuc.alg.T_PART)
  * [T\_RESULTS](#slambuc.alg.T_RESULTS)
  * [T\_IBLOCK](#slambuc.alg.T_IBLOCK)
  * [T\_BARRS](#slambuc.alg.T_BARRS)
* [slambuc.alg.util](#slambuc.alg.util)
  * [verify\_limits](#slambuc.alg.util.verify_limits)
  * [encode\_blk](#slambuc.alg.util.encode_blk)
  * [decode\_blk](#slambuc.alg.util.decode_blk)
  * [ipostorder\_dfs](#slambuc.alg.util.ipostorder_dfs)
  * [ipostorder\_tabu\_dfs](#slambuc.alg.util.ipostorder_tabu_dfs)
  * [ipostorder\_edges](#slambuc.alg.util.ipostorder_edges)
  * [ileft\_right\_dfs](#slambuc.alg.util.ileft_right_dfs)
  * [ileft\_right\_dfs\_idx](#slambuc.alg.util.ileft_right_dfs_idx)
  * [ichain](#slambuc.alg.util.ichain)
  * [ibacktrack\_chain](#slambuc.alg.util.ibacktrack_chain)
  * [isubchains](#slambuc.alg.util.isubchains)
  * [iflattened\_tree](#slambuc.alg.util.iflattened_tree)
  * [isubtree\_bfs](#slambuc.alg.util.isubtree_bfs)
  * [isubtrees](#slambuc.alg.util.isubtrees)
  * [itop\_subtree\_nodes](#slambuc.alg.util.itop_subtree_nodes)
  * [induced\_subtrees](#slambuc.alg.util.induced_subtrees)
  * [ipowerset](#slambuc.alg.util.ipowerset)
  * [iser\_mul\_factor](#slambuc.alg.util.iser_mul_factor)
  * [ipar\_mul\_factor](#slambuc.alg.util.ipar_mul_factor)
  * [igen\_mul\_factor](#slambuc.alg.util.igen_mul_factor)
  * [leaf\_label\_nodes](#slambuc.alg.util.leaf_label_nodes)
  * [ith\_child](#slambuc.alg.util.ith_child)
  * [child\_idx](#slambuc.alg.util.child_idx)
  * [top\_subtree\_block](#slambuc.alg.util.top_subtree_block)
  * [path\_blocks](#slambuc.alg.util.path_blocks)
  * [recreate\_subchain\_blocks](#slambuc.alg.util.recreate_subchain_blocks)
  * [recreate\_subtree\_blocks](#slambuc.alg.util.recreate_subtree_blocks)
  * [split\_chain](#slambuc.alg.util.split_chain)
  * [split\_path](#slambuc.alg.util.split_path)
  * [x\_eval](#slambuc.alg.util.x_eval)
  * [recalculate\_ser\_partitioning](#slambuc.alg.util.recalculate_ser_partitioning)
  * [recalculate\_partitioning](#slambuc.alg.util.recalculate_partitioning)
  * [block\_memory](#slambuc.alg.util.block_memory)
  * [block\_cpu](#slambuc.alg.util.block_cpu)
  * [block\_cost](#slambuc.alg.util.block_cost)
  * [block\_latency](#slambuc.alg.util.block_latency)
  * [ser\_block\_memory](#slambuc.alg.util.ser_block_memory)
  * [ser\_block\_memory\_opt](#slambuc.alg.util.ser_block_memory_opt)
  * [ser\_block\_memory\_pes](#slambuc.alg.util.ser_block_memory_pes)
  * [ser\_block\_memory\_pes2](#slambuc.alg.util.ser_block_memory_pes2)
  * [ser\_block\_cost](#slambuc.alg.util.ser_block_cost)
  * [ser\_block\_latency](#slambuc.alg.util.ser_block_latency)
  * [ser\_block\_submemory](#slambuc.alg.util.ser_block_submemory)
  * [ser\_block\_subcost](#slambuc.alg.util.ser_block_subcost)
  * [ser\_block\_sublatency](#slambuc.alg.util.ser_block_sublatency)
  * [ser\_subtree\_memory](#slambuc.alg.util.ser_subtree_memory)
  * [ser\_subtree\_cost](#slambuc.alg.util.ser_subtree_cost)
  * [ser\_pes\_subchain\_latency](#slambuc.alg.util.ser_pes_subchain_latency)
  * [ser\_subchain\_latency](#slambuc.alg.util.ser_subchain_latency)
  * [par\_inst\_count](#slambuc.alg.util.par_inst_count)
  * [par\_subtree\_memory](#slambuc.alg.util.par_subtree_memory)
  * [par\_subtree\_cost](#slambuc.alg.util.par_subtree_cost)
  * [par\_subchain\_latency](#slambuc.alg.util.par_subchain_latency)
  * [gen\_subtree\_memory](#slambuc.alg.util.gen_subtree_memory)
  * [gen\_subtree\_cost](#slambuc.alg.util.gen_subtree_cost)
  * [gen\_subchain\_latency](#slambuc.alg.util.gen_subchain_latency)
* [slambuc.gen.cluster.job\_tree](#slambuc.gen.cluster.job_tree)
  * [convert\_tasks\_to\_dag](#slambuc.gen.cluster.job_tree.convert_tasks_to_dag)
  * [igenerate\_job\_tree](#slambuc.gen.cluster.job_tree.igenerate_job_tree)
  * [igenerate\_syn\_tree](#slambuc.gen.cluster.job_tree.igenerate_syn_tree)
  * [generate\_all\_job\_trees](#slambuc.gen.cluster.job_tree.generate_all_job_trees)
  * [generate\_syn\_job\_trees](#slambuc.gen.cluster.job_tree.generate_syn_job_trees)
  * [generate\_mixed\_job\_trees](#slambuc.gen.cluster.job_tree.generate_mixed_job_trees)
* [slambuc.gen.cluster](#slambuc.gen.cluster)
* [slambuc.gen.cluster.syn\_job](#slambuc.gen.cluster.syn_job)
  * [draw](#slambuc.gen.cluster.syn_job.draw)
* [slambuc.gen.microservice.power\_ba\_graph](#slambuc.gen.microservice.power_ba_graph)
  * [wrand\_sample](#slambuc.gen.microservice.power_ba_graph.wrand_sample)
  * [generate\_power\_ba\_graph](#slambuc.gen.microservice.power_ba_graph.generate_power_ba_graph)
  * [generate\_power\_ba\_tree](#slambuc.gen.microservice.power_ba_graph.generate_power_ba_tree)
* [slambuc.gen.microservice.faas\_tree](#slambuc.gen.microservice.faas_tree)
  * [ifunc\_attributes](#slambuc.gen.microservice.faas_tree.ifunc_attributes)
  * [get\_faas\_tree](#slambuc.gen.microservice.faas_tree.get_faas_tree)
  * [verify\_faas\_tree](#slambuc.gen.microservice.faas_tree.verify_faas_tree)
  * [generate\_all\_faas\_trees](#slambuc.gen.microservice.faas_tree.generate_all_faas_trees)
* [slambuc.gen.microservice](#slambuc.gen.microservice)
* [slambuc.gen.io](#slambuc.gen.io)
  * [encode\_service\_tree](#slambuc.gen.io.encode_service_tree)
  * [decode\_service\_tree](#slambuc.gen.io.decode_service_tree)
  * [save\_trees\_to\_file](#slambuc.gen.io.save_trees_to_file)
  * [get\_tree\_from\_file](#slambuc.gen.io.get_tree_from_file)
  * [iload\_trees\_from\_file](#slambuc.gen.io.iload_trees_from_file)
  * [load\_hist\_params](#slambuc.gen.io.load_hist_params)
* [slambuc.gen](#slambuc.gen)
* [slambuc.gen.transform](#slambuc.gen.transform)
  * [faasify\_dag\_by\_duplication](#slambuc.gen.transform.faasify_dag_by_duplication)
  * [transform\_autonomous\_caching](#slambuc.gen.transform.transform_autonomous_caching)
* [slambuc.gen.random.random\_tree](#slambuc.gen.random.random_tree)
  * [RUNTIME](#slambuc.gen.random.random_tree.RUNTIME)
  * [MEMORY](#slambuc.gen.random.random_tree.MEMORY)
  * [DATA](#slambuc.gen.random.random_tree.DATA)
  * [RATE](#slambuc.gen.random.random_tree.RATE)
  * [generate\_random\_trees](#slambuc.gen.random.random_tree.generate_random_trees)
  * [generate\_all\_random\_trees](#slambuc.gen.random.random_tree.generate_all_random_trees)
* [slambuc.gen.random](#slambuc.gen.random)
* [slambuc.misc.generator](#slambuc.misc.generator)
  * [get\_random\_chain\_data](#slambuc.misc.generator.get_random_chain_data)
  * [get\_random\_chain](#slambuc.misc.generator.get_random_chain)
  * [get\_random\_tree](#slambuc.misc.generator.get_random_tree)
* [slambuc.misc.plot](#slambuc.misc.plot)
  * [draw\_tree](#slambuc.misc.plot.draw_tree)
  * [draw\_state\_dag](#slambuc.misc.plot.draw_state_dag)
* [slambuc.misc](#slambuc.misc)
* [slambuc.misc.util](#slambuc.misc.util)
  * [get\_cplex\_path](#slambuc.misc.util.get_cplex_path)
  * [get\_cpo\_path](#slambuc.misc.util.get_cpo_path)
  * [get\_glpk\_path](#slambuc.misc.util.get_glpk_path)
  * [is\_compatible](#slambuc.misc.util.is_compatible)
  * [get\_chain\_k\_min](#slambuc.misc.util.get_chain_k_min)
  * [get\_chain\_c\_min](#slambuc.misc.util.get_chain_c_min)
  * [get\_chain\_c\_max](#slambuc.misc.util.get_chain_c_max)
  * [get\_chain\_k\_max](#slambuc.misc.util.get_chain_k_max)
  * [get\_chain\_k\_opt](#slambuc.misc.util.get_chain_k_opt)
  * [get\_chain\_c\_opt](#slambuc.misc.util.get_chain_c_opt)
  * [prune\_chain](#slambuc.misc.util.prune_chain)
  * [print\_chain\_summary](#slambuc.misc.util.print_chain_summary)
  * [evaluate\_chain\_partitioning](#slambuc.misc.util.evaluate_chain_partitioning)
  * [print\_block\_stat](#slambuc.misc.util.print_block_stat)
  * [print\_chain\_partition\_result](#slambuc.misc.util.print_chain_partition_result)
  * [print\_tree\_summary](#slambuc.misc.util.print_tree_summary)
  * [print\_tree\_block\_stat](#slambuc.misc.util.print_tree_block_stat)
  * [print\_cpath\_stat](#slambuc.misc.util.print_cpath_stat)
  * [evaluate\_tree\_partitioning](#slambuc.misc.util.evaluate_tree_partitioning)
  * [print\_ser\_tree\_block\_stat](#slambuc.misc.util.print_ser_tree_block_stat)
  * [print\_ser\_cpath\_stat](#slambuc.misc.util.print_ser_cpath_stat)
  * [evaluate\_ser\_tree\_partitioning](#slambuc.misc.util.evaluate_ser_tree_partitioning)
  * [print\_par\_tree\_block\_stat](#slambuc.misc.util.print_par_tree_block_stat)
  * [print\_par\_cpath\_stat](#slambuc.misc.util.print_par_cpath_stat)
  * [evaluate\_par\_tree\_partitioning](#slambuc.misc.util.evaluate_par_tree_partitioning)
  * [evaluate\_gen\_tree\_partitioning](#slambuc.misc.util.evaluate_gen_tree_partitioning)
  * [print\_ser\_chain\_summary](#slambuc.misc.util.print_ser_chain_summary)
  * [print\_ser\_block\_stat](#slambuc.misc.util.print_ser_block_stat)
  * [evaluate\_ser\_chain\_partitioning](#slambuc.misc.util.evaluate_ser_chain_partitioning)
  * [print\_lp\_desc](#slambuc.misc.util.print_lp_desc)
  * [convert\_var\_dict](#slambuc.misc.util.convert_var_dict)
  * [print\_var\_matrix](#slambuc.misc.util.print_var_matrix)
  * [print\_pulp\_matrix\_values](#slambuc.misc.util.print_pulp_matrix_values)
  * [print\_cplex\_matrix\_values](#slambuc.misc.util.print_cplex_matrix_values)
  * [print\_cost\_coeffs](#slambuc.misc.util.print_cost_coeffs)
  * [print\_lat\_coeffs](#slambuc.misc.util.print_lat_coeffs)

<a id="slambuc"></a>

# slambuc

<a id="slambuc.alg.service.common"></a>

# slambuc.alg.service.common

<a id="slambuc.alg.service.common.Flavor"></a>

## Flavor Objects

```python
class Flavor(typing.NamedTuple)
```

Store subtree partitioning attributes for a given subcase.

<a id="slambuc.alg.service.common.Flavor.mem"></a>

#### mem

Available memory

<a id="slambuc.alg.service.common.Flavor.ncore"></a>

#### ncore

Available relative vCPU cores

<a id="slambuc.alg.service.common.Flavor.cfactor"></a>

#### cfactor

Relative cost factor

<a id="slambuc.alg.service.common.Flavor.name"></a>

#### name

```python
@property
def name() -> str
```

String representation of the given flavor.

<a id="slambuc.alg.service"></a>

# slambuc.alg.service

<a id="slambuc.alg.chain.ser.greedy"></a>

# slambuc.alg.chain.ser.greedy

<a id="slambuc.alg.chain.ser.greedy.ichain_blocks"></a>

#### ichain\_blocks

```python
def ichain_blocks(memory: list[int], M: int) -> T_PART_GEN
```

Calculates all combinations of chain cuts with respect to the *memory* values and constraint *M*.

Block memories are calculated assuming serialized platform execution model.

The calculation is improved compared to brute force to only start calculating cuts from minimal cut size *c_min*.

**Arguments**:

- `memory`: list of node memory values
- `M`: upper memory limit

**Returns**:

Generator over M-feasible cuts.

<a id="slambuc.alg.chain.ser.greedy.greedy_ser_chain_partitioning"></a>

#### greedy\_ser\_chain\_partitioning

```python
def greedy_ser_chain_partitioning(runtime: list[int],
                                  memory: list[int],
                                  rate: list[int],
                                  data: list[int],
                                  M: int = math.inf,
                                  L: int = math.inf,
                                  start: int = 0,
                                  end: int = None,
                                  delay: int = 1) -> T_RESULTS
```

Calculates all minimal-cost partitioning outcomes of a given chain by applying exhaustive search.

Parameters are the same as the partitioning algorithms in ``slambuc.alg.chain.ser.ilp``.

Block metrics are calculated assuming serialized platform execution model.

**Arguments**:

- `runtime`: running times in ms
- `memory`: memory requirements in MB
- `rate`: avg. rate of function invocations
- `data`: input data fetching delay in ms
- `M`: upper memory bound of the partition blocks (in MB)
- `L`: latency limit defined on the critical path in the form of subchain[start -> end] (in ms)
- `delay`: invocation delay between blocks
- `start`: head node of the latency-limited subchain
- `end`: tail node of the latency-limited subchain

**Returns**:

list if min-cost partitions, related optimal cost and latency

<a id="slambuc.alg.chain.ser.ilp"></a>

# slambuc.alg.chain.ser.ilp

<a id="slambuc.alg.chain.ser.ilp.ifeasible_greedy_blocks"></a>

#### ifeasible\_greedy\_blocks

```python
def ifeasible_greedy_blocks(memory: list[int], M: int) -> T_IBLOCK_GEN
```

Generate all feasible (connected) blocks that meet the memory constraint *M* in a greedy manner.

Block memories are calculated assuming serialized platform execution model.

**Arguments**:

- `memory`: list of node memory values
- `M`: upper block memory limit

**Returns**:

generator of blocks

<a id="slambuc.alg.chain.ser.ilp.ifeasible_blocks"></a>

#### ifeasible\_blocks

```python
def ifeasible_blocks(memory: list[int], M: int) -> T_IBLOCK_GEN
```

Generate all feasible (connected) blocks that meet the memory constraint *M* assuming serialized executions.

**Arguments**:

- `memory`: list of node memory values
- `M`: upper block memory limit

**Returns**:

generator of blocks

<a id="slambuc.alg.chain.ser.ilp.build_chain_cfg_model"></a>

#### build\_chain\_cfg\_model

```python
def build_chain_cfg_model(
        runtime: list[int],
        memory: list[int],
        rate: list[int],
        data: list[int],
        M: int = math.inf,
        L: int = math.inf,
        start: int = 0,
        end: int = None,
        delay: int = 1) -> tuple[lp.LpProblem, dict[lp.LpVariable]]
```

Generate the configuration ILP model for chains.

Block metrics are calculated assuming serialized platform execution model.

**Returns**:

tuple of the created LP model and the dict of created decision variables

<a id="slambuc.alg.chain.ser.ilp.chain_cfg_partitioning"></a>

#### chain\_cfg\_partitioning

```python
def chain_cfg_partitioning(runtime: list[int],
                           memory: list[int],
                           rate: list[int],
                           data: list[int],
                           M: int = math.inf,
                           L: int = math.inf,
                           start: int = 0,
                           end: int = None,
                           delay: int = 1,
                           solver: lp.LpSolver = None) -> T_RESULTS
```

Calculates minimal-cost partitioning of a chain based on the configuration ILP formalization.

Block metrics are calculated assuming serialized platform execution model.

**Arguments**:

- `runtime`: running times in ms
- `memory`: memory requirements in MB
- `rate`: avg. rate of function invocations
- `data`: input data fetching delay in ms
- `M`: upper memory bound of the partition blocks (in MB)
- `L`: latency limit defined on the critical path in the form of subchain[start -> end] (in ms)
- `start`: head node of the latency-limited subchain
- `end`: tail node of the latency-limited subchain
- `delay`: invocation delay between blocks
- `solver`: specific solver class (default: COIN-OR CBC)

**Returns**:

tuple of partitioning blocks, optimal cost, and the calculated latency of the subchain

<a id="slambuc.alg.chain.ser.ilp.recreate_blocks_from_xvars"></a>

#### recreate\_blocks\_from\_xvars

```python
def recreate_blocks_from_xvars(X: dict[tuple[int, int], lp.LpVariable],
                               n: int) -> T_PART
```

Extract barrier nodes from variable dict and recreate partitioning blocks.

**Arguments**:

- `X`: dict of decision variables
- `n`: chain size

**Returns**:

partition blocks

<a id="slambuc.alg.chain.ser.ilp.extract_blocks_from_xvars"></a>

#### extract\_blocks\_from\_xvars

```python
def extract_blocks_from_xvars(
        X: dict[tuple[int, int], lp.LpVariable]) -> T_PART
```

Extract interval boundaries [b, w] relying on the decision variable's structure.

**Arguments**:

- `X`: dict of decision variables

**Returns**:

partition blocks

<a id="slambuc.alg.chain.ser.ilp.build_greedy_chain_mtx_model"></a>

#### build\_greedy\_chain\_mtx\_model

```python
def build_greedy_chain_mtx_model(
        runtime: list[int],
        memory: list[int],
        rate: list[int],
        data: list[int],
        M: int = math.inf,
        L: int = math.inf,
        delay: int = 1) -> tuple[lp.LpProblem, list[list[lp.LpVariable]]]
```

Generate the matrix ILP model for chains by calculating block metrics greedily using utility functions.

Block metrics are calculated assuming serialized platform execution model.

**Returns**:

tuple of the created LP model and the dict of created decision variables

<a id="slambuc.alg.chain.ser.ilp.build_chain_mtx_model"></a>

#### build\_chain\_mtx\_model

```python
def build_chain_mtx_model(
        runtime: list[int],
        memory: list[int],
        rate: list[int],
        data: list[int],
        M: int = math.inf,
        L: int = math.inf,
        delay: int = 1) -> tuple[lp.LpProblem, list[list[lp.LpVariable]]]
```

Generate the matrix ILP model for chains.

Block metrics are calculated assuming serialized platform execution model.

**Returns**:

tuple of the created model and list of decision variables

<a id="slambuc.alg.chain.ser.ilp.chain_mtx_partitioning"></a>

#### chain\_mtx\_partitioning

```python
def chain_mtx_partitioning(runtime: list[int],
                           memory: list[int],
                           rate: list[int],
                           data: list[int],
                           M: int = math.inf,
                           L: int = math.inf,
                           delay: int = 1,
                           solver: lp.LpSolver = None,
                           **kwargs) -> T_RESULTS
```

Calculates minimal-cost partitioning of a chain based on the matrix ILP formalization.

Block metrics are calculated assuming serialized platform execution model.

**Arguments**:

- `runtime`: running times in ms
- `memory`: memory requirements in MB
- `rate`: avg. rate of function invocations
- `data`: input data fetching delay in ms
- `M`: upper memory bound of the partition blocks (in MB)
- `L`: latency limit defined on the critical path in the form of subchain[start -> end] (in ms)
- `delay`: invocation delay between blocks
- `solver`: specific solver class (default: COIN-OR CBC)

**Returns**:

tuple of partitioning blocks, optimal cost, and the calculated latency of the subchain

<a id="slambuc.alg.chain.ser.ilp.recreate_blocks_from_xmatrix"></a>

#### recreate\_blocks\_from\_xmatrix

```python
def recreate_blocks_from_xmatrix(X: list[list[lp.LpVariable]]) -> T_PART
```

Extract barrier nodes from decision variable matrix and recreate partitioning blocks.

**Arguments**:

- `X`: matrix of decision variables

**Returns**:

partition blocks

<a id="slambuc.alg.chain.ser.ilp.extract_blocks_from_xmatrix"></a>

#### extract\_blocks\_from\_xmatrix

```python
def extract_blocks_from_xmatrix(X: list[list[lp.LpVariable]]) -> T_PART
```

Extract interval boundaries [b, w] directly from decision variable matrix.

**Arguments**:

- `X`: matrix of decision variables

**Returns**:

partition blocks

<a id="slambuc.alg.chain.ser"></a>

# slambuc.alg.chain.ser

<a id="slambuc.alg.chain.sp.min"></a>

# slambuc.alg.chain.sp.min

<a id="slambuc.alg.chain.sp.min.hop_limited_shortest_path"></a>

#### hop\_limited\_shortest\_path

```python
def hop_limited_shortest_path(
        dag: nx.DiGraph,
        source: str | int,
        target: str | int,
        max_hops: int = math.inf) -> tuple[int, int, list[int | str]]
```

Calculate the shortest path in graph 'dag' between 'source' and 'target' with the hop limit 'max_hops'.

**Arguments**:

- `dag`: state graph
- `source`: start node in 'dag'
- `target`: end node in 'dag'
- `max_hops`: hop limit of for the path

**Returns**:

calculated sum weights, hop count, nodes of the shortest path

<a id="slambuc.alg.chain.sp.min.sp_chain_partitioning"></a>

#### sp\_chain\_partitioning

```python
def sp_chain_partitioning(runtime: list,
                          memory: list,
                          rate: list,
                          M: int = math.inf,
                          N: int = math.inf,
                          L: int = math.inf,
                          delay: int = 1,
                          unit: int = 100) -> T_RESULTS
```

Calculates minimal-cost partitioning of a chain based on the node properties of *running time*, *memory usage* and

*invocation rate* with respect to an upper bound **M** on the total memory of blocks and a latency constraint **L**
defined on the subchain between *start* and *end* nodes.

Partitioning is based on the shortest path calculation of the state graph of feasible blocks.

**Arguments**:

- `runtime`: running times in ms
- `memory`: memory requirements in MB
- `rate`: avg. rate of function invocations
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks
- `L`: latency limit defined on the critical path in the form of subchain[start -> end] (in ms)
- `delay`: invocation delay between blocks
- `unit`: rounding unit for the cost calculation (default: 100 ms)

**Returns**:

tuple of barrier nodes, sum cost of the partitioning, and the calculated edge cuts

<a id="slambuc.alg.chain"></a>

# slambuc.alg.chain

<a id="slambuc.alg.chain.dp.greedy"></a>

# slambuc.alg.chain.dp.greedy

<a id="slambuc.alg.chain.dp.greedy.ichain_blocks"></a>

#### ichain\_blocks

```python
def ichain_blocks(memory: list[int], rate: list[int], N: int,
                  M: int) -> T_PART_GEN
```

Calculates all combination of chain cuts with respect to *memory* and *rate* values and the constraint **M**.

The calculation is improved compared to brute force to only start calculating cuts from minimal cut size *c_min*.

**Arguments**:

- `memory`: list of node memory values
- `rate`: list of invocation rate values
- `N`: number of vCPU cores
- `M`: upper memory limit

**Returns**:

Generator over M-feasible cuts.

<a id="slambuc.alg.chain.dp.greedy.greedy_chain_partitioning"></a>

#### greedy\_chain\_partitioning

```python
def greedy_chain_partitioning(runtime: list[int],
                              memory: list[int],
                              rate: list[int],
                              M: int = math.inf,
                              N: int = math.inf,
                              L: int = math.inf,
                              start: int = 0,
                              end: int = None,
                              delay: int = 1,
                              unit: int = 100) -> list[T_RESULTS]
```

Calculates all minimal-cost partitioning outcomes of a given chain by applying exhaustive search.

Parameters are the same as the partitioning algorithms in ``slambuc.alg.chain.dp.mtx``
and ``slambuc.alg.chain.dp.min``.

**Arguments**:

- `runtime`: running times in ms
- `memory`: memory requirements in MB
- `rate`: avg. rate of function invocations
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks
- `L`: latency limit defined on the critical path in the form of subchain[start -> end] (in ms)
- `delay`: invocation delay between blocks
- `start`: head node of the latency-limited subchain
- `end`: tail node of the latency-limited subchain
- `unit`: rounding unit for the cost calculation (default: 100 ms)

**Returns**:

list if min-cost partitions, related optimal cost and latency

<a id="slambuc.alg.chain.dp.mtx"></a>

# slambuc.alg.chain.dp.mtx

<a id="slambuc.alg.chain.dp.mtx.State"></a>

## State Objects

```python
class State(typing.NamedTuple)
```

Store block attributes for a given DP subcase.

<a id="slambuc.alg.chain.dp.mtx.State.barr"></a>

#### barr

Barrier/heading node of the last block in the given subcase partitioning

<a id="slambuc.alg.chain.dp.mtx.State.cost"></a>

#### cost

Sum cost of the partitioning

<a id="slambuc.alg.chain.dp.mtx.State.lat"></a>

#### lat

Sum latency of the partitioning regarding the limited subchain[start, end]

<a id="slambuc.alg.chain.dp.mtx.chain_partitioning"></a>

#### chain\_partitioning

```python
def chain_partitioning(
        runtime: list,
        memory: list,
        rate: list,
        M: int = math.inf,
        N: int = math.inf,
        L: int = math.inf,
        start: int = 0,
        end: int = None,
        delay: int = 1,
        unit: int = 100,
        ret_dp: bool = False) -> tuple[T_BARRS | list[list[State]], int, int]
```

Calculates minimal-cost partitioning of a chain based on the node properties of *running time*, *memory usage* and

*invocation rate* with respect to an upper bound **M** on the total memory of blocks and a latency constraint **L**
defined on the subchain between *start* and *end* nodes.

Cost calculation relies on the rounding *unit* and number of vCPU cores *N*, whereas platform invocation *delay*
is used for latency calculations.

Details in: J. Czentye, I. Pelle and B. Sonkoly, "Cost-optimal Operation of Latency Constrained Serverless
Applications: From Theory to Practice," NOMS 2023-2023 IEEE/IFIP Network Operations and Management Symposium,
Miami, FL, USA, 2023, pp. 1-10, doi: 10.1109/NOMS56928.2023.10154412.

**Arguments**:

- `runtime`: running times in ms
- `memory`: memory requirements in MB
- `rate`: avg. rate of function invocations
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks
- `L`: latency limit defined on the critical path in the form of subchain[start -> end] (in ms)
- `delay`: invocation delay between blocks
- `start`: head node of the latency-limited subchain
- `end`: tail node of the latency-limited subchain
- `unit`: rounding unit for the cost calculation (default: 100 ms)
- `ret_dp`: return the calculated DP matrix instead of barrier nodes

**Returns**:

tuple of barrier nodes, sum cost of the partitioning, and the calculated latency on the subchain

<a id="slambuc.alg.chain.dp.mtx.extract_barr"></a>

#### extract\_barr

```python
def extract_barr(DP: list[list[State]], k: int) -> T_BARRS
```

Extract barrier nodes form DP matrix by iteratively backtracking the minimal cost subcases started from *k*.

**Arguments**:

- `DP`: DP matrix containing subcase *States*
- `k`: number of optimal cuts

**Returns**:

list of barrier nodes

<a id="slambuc.alg.chain.dp.mtx.vec_chain_partitioning"></a>

#### vec\_chain\_partitioning

```python
def vec_chain_partitioning(
        runtime: list,
        memory: list,
        rate: list,
        M: int = np.inf,
        N: int = np.inf,
        L: int = np.inf,
        start: int = 0,
        end: int = None,
        delay: int = 1,
        unit: int = 100,
        ret_dp: bool = False) -> tuple[T_BARRS | np.ndarray, int, int]
```

Calculates minimal-cost partitioning of a chain based on the node properties of *runtime*, *memory* and *rate* with

respect to an upper bound **M** on the total memory of blocks and a latency constraint **L** defined on the subchain
between *start* and *end* nodes leveraging vectorized operations.

Cost calculation relies on the rounding *unit* and number of vCPU cores *N*, whereas platform invocation *delay*
is used for latency calculations.

Details in: J. Czentye, I. Pelle and B. Sonkoly, "Cost-optimal Operation of Latency Constrained Serverless
Applications: From Theory to Practice," NOMS 2023-2023 IEEE/IFIP Network Operations and Management Symposium,
Miami, FL, USA, 2023, pp. 1-10, doi: 10.1109/NOMS56928.2023.10154412.

**Arguments**:

- `runtime`: running times in ms
- `memory`: memory requirements in MB
- `rate`: avg. rate of function invocations
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks
- `L`: latency limit defined on the critical path in the form of subchain[start -> end] (in ms)
- `delay`: invocation delay between blocks
- `start`: head node of the latency-limited subchain
- `end`: tail node of the latency-limited subchain
- `unit`: rounding unit for the cost calculation (default: 100 ms)
- `ret_dp`: return the calculated DP matrix instead of the barrier nodes

**Returns**:

tuple of barrier nodes, sum cost of the partitioning, and the calculated latency on the subchain

<a id="slambuc.alg.chain.dp.mtx.extract_vec_barr"></a>

#### extract\_vec\_barr

```python
def extract_vec_barr(DP: np.ndarray, k: int) -> T_BARRS
```

Extract barrier nodes from vectorized DP matrix by iteratively backtracking the minimal cost subcases from *k*.

**Arguments**:

- `DP`: DP matrix containing subcase *States*
- `k`: number of optimal cuts

**Returns**:

list of barrier nodes

<a id="slambuc.alg.chain.dp.min"></a>

# slambuc.alg.chain.dp.min

<a id="slambuc.alg.chain.dp.min.min_chain_partitioning"></a>

#### min\_chain\_partitioning

```python
def min_chain_partitioning(runtime: list[int],
                           memory: list[int],
                           rate: list[int],
                           M: int = math.inf,
                           N: int = math.inf,
                           L: int = math.inf,
                           start: int = 0,
                           end: int = None,
                           delay: int = 1,
                           unit: int = 100) -> T_BRESULTS
```

Calculates minimal-cost partitioning of a chain based on the node properties of *running time*, *memory usage* and

*invocation rate* with respect to an upper bound **M** on the total memory of blocks and a latency constraint **L**
defined on the subchain between *start* and *end* nodes.

Cost calculation relies on the rounding *unit* and number of vCPU cores *N*, whereas platform invocation *delay*
is used for latency calculations.

It gives optimal result only in case the cost function regarding the chain attributes is sub-additive,
that is k_opt = k_min is guaranteed for each case.

Instead of full partitioning it only returns the list of barrier nodes.

**Arguments**:

- `runtime`: running times in ms
- `memory`: memory requirements in MB
- `rate`: avg. rate of function invocations
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks
- `L`: latency limit defined on the critical path in the form of subchain[start -> end] (in ms)
- `delay`: invocation delay between blocks
- `start`: head node of the latency-limited subchain
- `end`: tail node of the latency-limited subchain
- `unit`: rounding unit for the cost calculation (default: 100 ms)

**Returns**:

tuple of barrier nodes, sum cost of the partitioning, and the calculated latency on the subchain

<a id="slambuc.alg.chain.dp.min.extract_min_barr"></a>

#### extract\_min\_barr

```python
def extract_min_barr(DP: list[State]) -> T_BARRS
```

Extract barrier nodes form DP list by iteratively backtracking minimal cost subcases.

**Arguments**:

- `DP`: dynamic programming structure storing intermediate *States*

**Returns**:

list of barrier nodes

<a id="slambuc.alg.chain.dp"></a>

# slambuc.alg.chain.dp

<a id="slambuc.alg.tree.ser.bicriteria"></a>

# slambuc.alg.tree.ser.bicriteria

<a id="slambuc.alg.tree.ser.bicriteria.WeightedSubBTreePart"></a>

## WeightedSubBTreePart Objects

```python
class WeightedSubBTreePart(typing.NamedTuple)
```

Store subtree partitioning attributes for a given edge-weighted subcase.

<a id="slambuc.alg.tree.ser.bicriteria.WeightedSubBTreePart.weight"></a>

#### weight

Cumulative weights of covered edges in the subtree partitioning

<a id="slambuc.alg.tree.ser.bicriteria.WeightedSubBTreePart.barr"></a>

#### barr

Barrier/heading nodes of the given subtree partitioning

<a id="slambuc.alg.tree.ser.bicriteria.biheuristic_btree_partitioning"></a>

#### biheuristic\_btree\_partitioning

```python
def biheuristic_btree_partitioning(tree: nx.DiGraph,
                                   root: int = 1,
                                   M: int = math.inf,
                                   L: int = math.inf,
                                   cp_end: int = None,
                                   delay: int = 1,
                                   Epsilon: float = 0.0,
                                   Lambda: float = 0.0,
                                   bidirectional: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes, while
applying the bottom-up tree traversal approach.

Cost approximation ratio *Epsilon* controls the maximum deviation from the cost-optimal partitioning
(Epsilon=0.0 enforces the algorithm to calculate exact solution) in exchange for reduces subcase calculations.

Latency approximation ratio (*Lambda*) controls the maximum deviation with respect to the latency limit $L$
(Lambda=0.0 enforces no rounding) in exchange for reduces subcase calculations.

Block metrics are calculated based on serialized execution platform model.

Provide suboptimal partitioning due to the simplified and inaccurate latency rounding.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `Epsilon`: weight factor for state space trimming (0 <= Eps < 1, Eps = 0 falls back to exact calc.)
- `Lambda`: latency factor for state space trimming (0 <= Lambda, Lambda = 0 falls back to exact calc.)
- `bidirectional`: use bidirectional subcase elimination (may introduce quadratic increase in the worst case)

**Returns**:

tuple of optimal partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.tree.ser.bicriteria.biheuristic_tree_partitioning"></a>

#### biheuristic\_tree\_partitioning

```python
def biheuristic_tree_partitioning(tree: nx.DiGraph,
                                  root: int = 1,
                                  M: int = math.inf,
                                  L: int = math.inf,
                                  cp_end: int = None,
                                  delay: int = 1,
                                  Epsilon: float = 0.0,
                                  Lambda: float = 0.0,
                                  bidirectional: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes, while
applying the bottom-up tree traversal approach.

Provide suboptimal partitioning due to the simplified and inaccurate latency rounding.

Recalculates original sum cost and latency metrics.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `Epsilon`: weight factor for state space trimming (0 <= Eps < 1, Eps = 0 falls back to exact calc.)
- `Lambda`: latency factor for state space trimming (0 <= Lambda, Lambda = 0 falls back to exact calc.)
- `bidirectional`: use bidirectional subcase elimination (may introduce quadratic increase in the worst case)

**Returns**:

tuple of optimal partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.tree.ser.bicriteria.WeightedSubLTreePart"></a>

## WeightedSubLTreePart Objects

```python
class WeightedSubLTreePart(typing.NamedTuple)
```

Store subtree partitioning attributes for a given edge-weighted subcase.

<a id="slambuc.alg.tree.ser.bicriteria.WeightedSubLTreePart.weight"></a>

#### weight

Cumulative weights of covered edges in the subtree partitioning

<a id="slambuc.alg.tree.ser.bicriteria.WeightedSubLTreePart.top_lat"></a>

#### top\_lat

Calculated latency for the topmost partition block

<a id="slambuc.alg.tree.ser.bicriteria.WeightedSubLTreePart.mul"></a>

#### mul

Last serialization multiplier of the top/first block of the subtree partitioning

<a id="slambuc.alg.tree.ser.bicriteria.WeightedSubLTreePart.barr"></a>

#### barr

Barrier/heading nodes of the given subtree partitioning

<a id="slambuc.alg.tree.ser.bicriteria.bifptas_ltree_partitioning"></a>

#### bifptas\_ltree\_partitioning

```python
def bifptas_ltree_partitioning(tree: nx.DiGraph,
                               root: int = 1,
                               M: int = math.inf,
                               L: int = math.inf,
                               cp_end: int = None,
                               delay: int = 1,
                               Epsilon: float = 0.0,
                               Lambda: float = 0.0,
                               bidirectional: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes, while
applying the left-right tree traversal approach.

Cost approximation ratio *Epsilon* controls the maximum deviation from the cost-optimal partitioning
(Epsilon=0.0 enforces the algorithm to calculate exact solution) in exchange for reduces subcase calculations.

Latency violation ratio (*Lambda*) controls the maximum violating deviation from the latency limit $L$
(Lambda=0.0 enforces no violation)  in exchange for reduces subcase calculations.

Block metrics are calculated based on serialized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `Epsilon`: weight factor for state space trimming (0 <= Eps < 1, Eps = 0 falls back to exact calc.)
- `Lambda`: latency factor for state space trimming (0 <= Lambda, Lambda = 0 falls back to exact calc.)
- `bidirectional`: use bidirectional subcase elimination (may introduce quadratic increase in the worst case)

**Returns**:

tuple of optimal partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.tree.ser.bicriteria.bifptas_tree_partitioning"></a>

#### bifptas\_tree\_partitioning

```python
def bifptas_tree_partitioning(tree: nx.DiGraph,
                              root: int = 1,
                              M: int = math.inf,
                              L: int = math.inf,
                              cp_end: int = None,
                              delay: int = 1,
                              Epsilon: float = 0.0,
                              Lambda: float = 0.0,
                              bidirectional: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes, while
applying the left-right tree traversal approach.

Recalculates original sum cost and latency metrics.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `Epsilon`: weight factor for state space trimming (0 <= Eps < 1, Eps = 0 falls back to exact calc.)
- `Lambda`: latency factor for state space trimming (0 <= Lambda, Lambda = 0 falls back to exact calc.)
- `bidirectional`: use bidirectional subcase elimination (may introduce quadratic increase in the worst case)

**Returns**:

tuple of optimal partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.tree.ser.bicriteria.WeightedDualSubLTreePart"></a>

## WeightedDualSubLTreePart Objects

```python
class WeightedDualSubLTreePart(typing.NamedTuple)
```

Store subtree partitioning attributes for a given edge-weighted subcase.

<a id="slambuc.alg.tree.ser.bicriteria.WeightedDualSubLTreePart.mem"></a>

#### mem

Memory demand of the topmost block in the subtree partitioning

<a id="slambuc.alg.tree.ser.bicriteria.WeightedDualSubLTreePart.top_lat"></a>

#### top\_lat

Calculated latency for the topmost partition block

<a id="slambuc.alg.tree.ser.bicriteria.WeightedDualSubLTreePart.mul"></a>

#### mul

Last serialization multiplier of the top/first block of the subtree partitioning

<a id="slambuc.alg.tree.ser.bicriteria.WeightedDualSubLTreePart.barr"></a>

#### barr

Barrier/heading nodes of the given subtree partitioning

<a id="slambuc.alg.tree.ser.bicriteria.bifptas_dual_ltree_partitioning"></a>

#### bifptas\_dual\_ltree\_partitioning

```python
def bifptas_dual_ltree_partitioning(tree: nx.DiGraph,
                                    root: int = 1,
                                    M: int = math.inf,
                                    L: int = math.inf,
                                    cp_end: int = None,
                                    delay: int = 1,
                                    Epsilon: float = 0.0,
                                    Lambda: float = 0.0,
                                    bidirectional: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes, while
applying the left-right tree traversal approach.

Cost approximation ratio *Epsilon* controls the maximum deviation from the cost-optimal partitioning
(Epsilon=0.0 enforces the algorithm to calculate exact solution) in exchange for reduces subcase calculations.

Latency violation ratio (*Lambda*) controls the maximum violating deviation from the latency limit $L$
(Lambda=0.0 enforces no violation)  in exchange for reduces subcase calculations.

Instead of direct cost calculations, the cumulative overheads of externalized states are subject to minimization
as a different formalization of the same optimization problem.

Block metrics are calculated based on serialized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `Epsilon`: weight factor for state space trimming (0 <= Eps < 1, Eps = 0 falls back to exact calc.)
- `Lambda`: latency factor for state space trimming (0 <= Lambda, Lambda = 0 falls back to exact calc.)
- `bidirectional`: use bidirectional subcase elimination (may introduce quadratic increase in the worst case)

**Returns**:

tuple of optimal partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.tree.ser.bicriteria.bifptas_dual_tree_partitioning"></a>

#### bifptas\_dual\_tree\_partitioning

```python
def bifptas_dual_tree_partitioning(tree: nx.DiGraph,
                                   root: int = 1,
                                   M: int = math.inf,
                                   L: int = math.inf,
                                   cp_end: int = None,
                                   delay: int = 1,
                                   Epsilon: float = 0.0,
                                   Lambda: float = 0.0,
                                   bidirectional: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes, while
applying a different formalization of the optimal partitioning problem.

Cost approximation ratio *Epsilon* controls the maximum deviation from the cost-optimal partitioning
(Epsilon=0.0 enforces the algorithm to calculate exact solution) in exchange for reduces subcase calculations.

Latency violation ratio (*Lambda*) controls the maximum violating deviation from the latency limit $L$
(Lambda=0.0 enforces no violation)  in exchange for reduces subcase calculations.

Block metrics are calculated based on serialized execution platform model.

Recalculates original sum cost and latency metrics.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `Epsilon`: weight factor for state space trimming (0 <= Eps < 1, Eps = 0 falls back to exact calc.)
- `Lambda`: latency factor for state space trimming (0 <= Lambda, Lambda = 0 falls back to exact calc.)
- `bidirectional`: use bidirectional subcase elimination (may introduce quadratic increase in the worst case)

**Returns**:

tuple of optimal partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.tree.ser.pseudo_mp"></a>

# slambuc.alg.tree.ser.pseudo\_mp

<a id="slambuc.alg.tree.ser.pseudo_mp.isubtree_cutoffs"></a>

#### isubtree\_cutoffs

```python
def isubtree_cutoffs(tree: nx.DiGraph,
                     root: int = 1,
                     lb: int = 1,
                     ub: int = math.inf) -> tuple[tuple[int, int], int]
```

Recursively return edges that cut off non-trivial subtrees from *tree* with size between *lb* and *ub*.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `lb`: lower size bound
- `ub`: upper size bound

**Returns**:

cut barrier node, branches and subtree root

<a id="slambuc.alg.tree.ser.pseudo_mp.get_cpu_splits"></a>

#### get\_cpu\_splits

```python
def get_cpu_splits(tree: nx.DiGraph,
                   root: int = 1,
                   workers: int = None) -> tuple[tuple[int, int]]
```

Calculate the cuts for parallelization based on *workers* count and subtree size heuristics.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `workers`: workers count

**Returns**:

cut edges

<a id="slambuc.alg.tree.ser.pseudo_mp.isubtree_sync_cutoffs"></a>

#### isubtree\_sync\_cutoffs

```python
def isubtree_sync_cutoffs(
        tree: nx.DiGraph,
        root: int = 1,
        size: int = math.inf) -> Generator[tuple[tuple[int], int, set[int]]]
```

Recursively return edges that cut off non-trivial subtrees from *tree* with given *size*.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `size`: subtree min size

**Returns**:

generator of cut edge, subtree root, and related branches

<a id="slambuc.alg.tree.ser.pseudo_mp.isubtree_splits"></a>

#### isubtree\_splits

```python
def isubtree_splits(
        tree: nx.DiGraph,
        root: int = 1) -> Generator[tuple[tuple[int], int, set[int]]]
```

Return the heuristic cutoff edges of given *tree* along with the mandatory synchronization points by assuming

the subtree size equals *sqrt(n)*.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph

**Returns**:

generator of cut edge, subtree root, and related branches

<a id="slambuc.alg.tree.ser.pseudo_mp.pseudo_mp_btree_partitioning"></a>

#### pseudo\_mp\_btree\_partitioning

```python
def pseudo_mp_btree_partitioning(tree: nx.DiGraph,
                                 root: int = 1,
                                 M: int = math.inf,
                                 L: int = math.inf,
                                 cp_end: int = None,
                                 delay: int = 1,
                                 bidirectional: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes.

Partitioning is calculated using the bottom-up tree traversal approach.

Arbitrary disjoint subtrees are partitioned in separate subprocesses.

Block metrics are calculated based on serialized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `bidirectional`: use bidirectional subcase elimination (may introduce quadratic increase in the worst case)

**Returns**:

tuple of optimal partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.tree.ser.pseudo_mp.pseudo_mp_ltree_partitioning"></a>

#### pseudo\_mp\_ltree\_partitioning

```python
def pseudo_mp_ltree_partitioning(tree: nx.DiGraph,
                                 root: int = 1,
                                 M: int = math.inf,
                                 L: int = math.inf,
                                 cp_end: int = None,
                                 delay: int = 1,
                                 bidirectional: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes.

Partitioning is calculated using the left-right tree traversal approach.

Arbitrary disjoint subtrees are partitioned in separate subprocesses.

Block metrics are calculated based on serialized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `bidirectional`: use bidirectional subcase elimination (may introduce quadratic increase in the worst case)

**Returns**:

tuple of optimal partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.tree.ser.greedy"></a>

# slambuc.alg.tree.ser.greedy

<a id="slambuc.alg.tree.ser.greedy.isubtrees_exhaustive"></a>

#### isubtrees\_exhaustive

```python
def isubtrees_exhaustive(tree: nx.DiGraph, root: int, M: int) -> T_BARRS_GEN
```

Calculate all combinations of edge cuts and returns only if it is feasible wrt. the memory limit *M*.

Block metrics are calculated based on serialized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound in MB

**Returns**:

generator of chain partitions

<a id="slambuc.alg.tree.ser.greedy.greedy_ser_tree_partitioning"></a>

#### greedy\_ser\_tree\_partitioning

```python
def greedy_ser_tree_partitioning(tree: nx.DiGraph,
                                 root: int = 1,
                                 M: int = math.inf,
                                 L: int = math.inf,
                                 cp_end: int = None,
                                 delay: int = 1) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) by iterating over all possible cuttings.

Block metrics are calculated based on serialized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `delay`: invocation delay between blocks

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.ser.ilp_cplex"></a>

# slambuc.alg.tree.ser.ilp\_cplex

<a id="slambuc.alg.tree.ser.ilp_cplex.build_tree_cfg_cpo_model"></a>

#### build\_tree\_cfg\_cpo\_model

```python
def build_tree_cfg_cpo_model(
    tree: nx.DiGraph,
    root: int = 1,
    M: int = math.inf,
    L: int = math.inf,
    cpath: set[int] = frozenset(),
    delay: int = 1,
    isubtrees: iter = ifeasible_subtrees
) -> tuple[cpo.CpoModel, list[cpo.CpoIntVar]]
```

Generate the configuration CP model.

**Returns**:

tuple of the created model and list of decision variables

<a id="slambuc.alg.tree.ser.ilp_cplex.tree_cpo_partitioning"></a>

#### tree\_cpo\_partitioning

```python
def tree_cpo_partitioning(tree: nx.DiGraph,
                          root: int = 1,
                          M: int = math.inf,
                          L: int = math.inf,
                          cp_end: int = None,
                          delay: int = 1,
                          **kwargs) -> T_RESULTS
```

Calculates minimal-cost partitioning of a tree based on configuration CP formulation.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rate
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `delay`: invocation delay between blocks

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.ser.ilp_cplex.recreate_subtrees_from_cpo_xdict"></a>

#### recreate\_subtrees\_from\_cpo\_xdict

```python
def recreate_subtrees_from_cpo_xdict(
        tree: nx.DiGraph, result: cpo.CpoSolveResult,
        Xn: dict[int, list[cpo.CpoIntVar]]) -> T_PART
```

Extract barrier nodes from variable names (x_{b}_{w}) and recreate partitioning blocks.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `result`: result object
- `Xn`: specific structure of decision variables

**Returns**:

calculated partitioning

<a id="slambuc.alg.tree.ser.ilp_cplex.build_greedy_tree_cplex_model"></a>

#### build\_greedy\_tree\_cplex\_model

```python
def build_greedy_tree_cplex_model(
        tree: nx.DiGraph,
        root: int = 1,
        M: int = math.inf,
        L: int = math.inf,
        cpath: set[int] = frozenset(),
        delay: int = 1
) -> tuple[cpx.Model, dict[int, dict[int, docplex.mp.dvar]]]
```

Generate the matrix ILP model using CPLEX Python binding.

**Returns**:

tuple of the created model and list of decision variables

<a id="slambuc.alg.tree.ser.ilp_cplex.build_tree_cplex_model"></a>

#### build\_tree\_cplex\_model

```python
def build_tree_cplex_model(
        tree: nx.DiGraph,
        root: int = 1,
        M: int = math.inf,
        L: int = math.inf,
        cpath: set[int] = frozenset(),
        delay: int = 1
) -> tuple[cpx.Model, dict[int, dict[int, docplex.mp.dvar]]]
```

Generate the matrix ILP model using CPLEX Python binding.

**Returns**:

tuple of the created model and list of decision variables

<a id="slambuc.alg.tree.ser.ilp_cplex.tree_cplex_partitioning"></a>

#### tree\_cplex\_partitioning

```python
def tree_cplex_partitioning(tree: nx.DiGraph,
                            root: int = 1,
                            M: int = math.inf,
                            L: int = math.inf,
                            cp_end: int = None,
                            delay: int = 1,
                            **kwargs) -> T_RESULTS
```

Calculates minimal-cost partitioning of a tree based on matrix CPLEX ILP formulation.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rate
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `delay`: invocation delay between blocks

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.ser.ilp_cplex.extract_subtrees_from_cplex_xmatrix"></a>

#### extract\_subtrees\_from\_cplex\_xmatrix

```python
def extract_subtrees_from_cplex_xmatrix(
        X: dict[int, dict[int, docplex.mp.dvar]]) -> T_PART
```

Extract barrier nodes from variable matrix(dict-of-dict) and recreate partitioning blocks.

**Arguments**:

- `X`: specific structure of decision variables

**Returns**:

calculated partitioning

<a id="slambuc.alg.tree.ser.pseudo"></a>

# slambuc.alg.tree.ser.pseudo

<a id="slambuc.alg.tree.ser.pseudo.SubBTreePart"></a>

## SubBTreePart Objects

```python
class SubBTreePart(typing.NamedTuple)
```

Store subtree partitioning attributes for a given subcase.

<a id="slambuc.alg.tree.ser.pseudo.SubBTreePart.cost"></a>

#### cost

Sum cost of the subtree partitioning

<a id="slambuc.alg.tree.ser.pseudo.SubBTreePart.barr"></a>

#### barr

Barrier/heading nodes of the given subtree partitioning

<a id="slambuc.alg.tree.ser.pseudo.pseudo_btree_partitioning"></a>

#### pseudo\_btree\_partitioning

```python
def pseudo_btree_partitioning(tree: nx.DiGraph,
                              root: int = 1,
                              M: int = math.inf,
                              L: int = math.inf,
                              cp_end: int = None,
                              delay: int = 1,
                              bidirectional: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes, while
applying bottom-up tree traversal approach.

Block metrics are calculated based on serialized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `bidirectional`: use bidirectional subcase elimination (may introduce quadratic increase in the worst case)

**Returns**:

tuple of optimal partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.tree.ser.pseudo.SubLTreePart"></a>

## SubLTreePart Objects

```python
class SubLTreePart(typing.NamedTuple)
```

Store subtree partitioning attributes for a given subcase.

<a id="slambuc.alg.tree.ser.pseudo.SubLTreePart.cost"></a>

#### cost

Sum cost of the subtree partitioning

<a id="slambuc.alg.tree.ser.pseudo.SubLTreePart.mul"></a>

#### mul

Last serialization multiplier of the top/first block of the subtree partitioning

<a id="slambuc.alg.tree.ser.pseudo.SubLTreePart.barr"></a>

#### barr

Barrier/heading nodes of the given subtree partitioning

<a id="slambuc.alg.tree.ser.pseudo.pseudo_ltree_partitioning"></a>

#### pseudo\_ltree\_partitioning

```python
def pseudo_ltree_partitioning(tree: nx.DiGraph,
                              root: int = 1,
                              M: int = math.inf,
                              L: int = math.inf,
                              cp_end: int = None,
                              delay: int = 1,
                              bidirectional: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes, while
applying left-right tree traversal approach.

Block metrics are calculated based on serialized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `bidirectional`: use bidirectional subcase elimination (may introduce quadratic increase in the worst case)

**Returns**:

tuple of optimal partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.tree.ser.ilp"></a>

# slambuc.alg.tree.ser.ilp

<a id="slambuc.alg.tree.ser.ilp.ifeasible_greedy_subtrees"></a>

#### ifeasible\_greedy\_subtrees

```python
def ifeasible_greedy_subtrees(tree: nx.DiGraph, root: int,
                              M: int) -> Generator[tuple[int, set[int]]]
```

Generate feasible subtrees in a combinatorial way, which meet the connectivity and memory constraint *M*.

Block metrics are calculated based on serialized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)

**Returns**:

generator of subtree root and regarding subtree nodes

<a id="slambuc.alg.tree.ser.ilp.ifeasible_subtrees"></a>

#### ifeasible\_subtrees

```python
def ifeasible_subtrees(
        tree: nx.DiGraph,
        root: int,
        M: int,
        filtered: bool = True) -> Generator[tuple[int, set[int]]]
```

Generate M-feasible(connected) subtrees and roots in a bottom-up way, which meet the memory constraint *M*.

Block metrics are calculated based on serialized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `filtered`: filter our infeasible subtrees

**Returns**:

generator of subtree root and regarding subtree nodes

<a id="slambuc.alg.tree.ser.ilp.build_tree_cfg_model"></a>

#### build\_tree\_cfg\_model

```python
def build_tree_cfg_model(
    tree: nx.DiGraph,
    root: int = 1,
    M: int = math.inf,
    L: int = math.inf,
    cpath: set[int] = frozenset(),
    delay: int = 1,
    isubtrees: iter = ifeasible_subtrees
) -> tuple[lp.LpProblem, dict[int, list[lp.LpVariable]]]
```

Generate the configuration ILP model using serialized metric calculation.

**Returns**:

tuple of the created model and list of decision variables

<a id="slambuc.alg.tree.ser.ilp.tree_cfg_partitioning"></a>

#### tree\_cfg\_partitioning

```python
def tree_cfg_partitioning(tree: nx.DiGraph,
                          root: int = 1,
                          M: int = math.inf,
                          L: int = math.inf,
                          cp_end: int = None,
                          delay: int = 1,
                          solver: lp.LpSolver = None,
                          timeout: int = None,
                          **lpargs) -> T_RESULTS
```

Calculates minimal-cost partitioning of a tree based on configuration LP formulation and greedy subcase

generation.

Block metrics are calculated based on serialized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `delay`: invocation delay between blocks
- `solver`: specific solver class (default: COIN-OR CBC)
- `timeout`: time limit in sec
- `lpargs`: additional LP solver parameters

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.ser.ilp.tree_hybrid_partitioning"></a>

#### tree\_hybrid\_partitioning

```python
def tree_hybrid_partitioning(tree: nx.DiGraph,
                             root: int = 1,
                             M: int = math.inf,
                             L: int = math.inf,
                             cp_end: int = None,
                             delay: int = 1,
                             solver: lp.LpSolver = None,
                             timeout: int = None,
                             **lpargs) -> T_RESULTS
```

Calculates minimal-cost partitioning of a tree based on configuration LP formulation and hybrid subcase

generation.

Block metrics are calculated based on serialized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `delay`: invocation delay between blocks
- `solver`: specific solver class (default: COIN-OR CBC)
- `timeout`: time limit in sec
- `lpargs`: additional LP solver parameters

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.ser.ilp.extract_subtrees_from_xdict"></a>

#### extract\_subtrees\_from\_xdict

```python
def extract_subtrees_from_xdict(model: lp.LpProblem) -> T_PART
```

Recreate partitioning blocks from metadata cached in variables objects.

**Arguments**:

- `model`: LP problem model

**Returns**:

calculated partitioning

<a id="slambuc.alg.tree.ser.ilp.recreate_subtrees_from_xdict"></a>

#### recreate\_subtrees\_from\_xdict

```python
def recreate_subtrees_from_xdict(tree: nx.DiGraph,
                                 Xn: dict[int, list[lp.LpVariable]]) -> T_PART
```

Extract barrier nodes from variable names (x_{b}_{w}) and recreate partitioning blocks.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `Xn`: specific structure of decision variables

**Returns**:

calculated partitioning

<a id="slambuc.alg.tree.ser.ilp.build_greedy_tree_mtx_model"></a>

#### build\_greedy\_tree\_mtx\_model

```python
def build_greedy_tree_mtx_model(
    tree: nx.DiGraph,
    root: int = 1,
    M: int = math.inf,
    L: int = math.inf,
    cpath: set[int] = frozenset(),
    subchains: bool = False,
    delay: int = 1
) -> tuple[lp.LpProblem, dict[int, dict[int, lp.LpVariable]]]
```

Generate the matrix ILP model in a greedy manner.

Block metrics are calculated based on serialized execution platform model.

**Returns**:

tuple of the created model and list of decision variables

<a id="slambuc.alg.tree.ser.ilp.build_tree_mtx_model"></a>

#### build\_tree\_mtx\_model


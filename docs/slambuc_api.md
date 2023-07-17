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
  * [min\_weight\_partition\_heuristic](#slambuc.alg.ext.greedy.min_weight_partition_heuristic)
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

Store subtree partitioning attributes for a given subcase

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

String representation of the given flavor

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
    delay: int = 1
) -> tuple[lp.LpProblem, dict[int, dict[int, lp.LpVariable]]]
```

Generate the matrix ILP model in a greedy manner.

Block metrics are calculated based on serialized execution platform model.

**Returns**:

tuple of the created model and list of decision variables

<a id="slambuc.alg.tree.ser.ilp.build_tree_mtx_model"></a>

#### build\_tree\_mtx\_model

```python
def build_tree_mtx_model(
    tree: nx.DiGraph,
    root: int = 1,
    M: int = math.inf,
    L: int = math.inf,
    cpath: set[int] = frozenset(),
    delay: int = 1
) -> tuple[lp.LpProblem, dict[int, dict[int, lp.LpVariable]]]
```

Generate the matrix ILP model directly from formulas.

Block metrics are calculated based on serialized execution platform model.

**Returns**:

tuple of the created model and list of decision variables

<a id="slambuc.alg.tree.ser.ilp.tree_mtx_partitioning"></a>

#### tree\_mtx\_partitioning

```python
def tree_mtx_partitioning(tree: nx.DiGraph,
                          root: int = 1,
                          M: int = math.inf,
                          L: int = math.inf,
                          cp_end: int = None,
                          delay: int = 1,
                          solver: lp.LpSolver = None,
                          timeout: int = None,
                          **lpargs) -> T_RESULTS
```

Calculates minimal-cost partitioning of a tree based on the matrix ILP formulation.

Block metrics are calculated based on serialized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rate
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

<a id="slambuc.alg.tree.ser.ilp.recreate_subtrees_from_xmatrix"></a>

#### recreate\_subtrees\_from\_xmatrix

```python
def recreate_subtrees_from_xmatrix(
        tree: nx.DiGraph, X: dict[int, dict[int, lp.LpVariable]]) -> T_PART
```

Extract barrier nodes from variable matrix(dict-of-dict) and recreate partitioning blocks.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `X`: specific structure of decision variables

**Returns**:

calculated partitioning

<a id="slambuc.alg.tree.ser.ilp.extract_subtrees_from_xmatrix"></a>

#### extract\_subtrees\_from\_xmatrix

```python
def extract_subtrees_from_xmatrix(
        X: dict[int, dict[int, lp.LpVariable]]) -> T_PART
```

Extract barrier nodes from variable matrix(dict-of-dict) and recreate partitioning blocks.

**Arguments**:

- `X`: specific structure of decision variables

**Returns**:

calculated partitioning

<a id="slambuc.alg.tree.ser.ilp.all_tree_mtx_partitioning"></a>

#### all\_tree\_mtx\_partitioning

```python
def all_tree_mtx_partitioning(tree: nx.DiGraph,
                              root: int = 1,
                              M: int = math.inf,
                              L: int = math.inf,
                              cp_end: int = None,
                              delay: int = 1,
                              solver: lp.LpSolver = None,
                              timeout: int = None,
                              **lpargs) -> tuple[list[list[int]], int, int]
```

Calculates all minimal-cost partitioning variations of a tree based on matrix ILP formulation.

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

<a id="slambuc.alg.tree.ser"></a>

# slambuc.alg.tree.ser

<a id="slambuc.alg.tree.layout.ilp"></a>

# slambuc.alg.tree.layout.ilp

<a id="slambuc.alg.tree.layout.ilp.ifeasible_gen_subtrees"></a>

#### ifeasible\_gen\_subtrees

```python
def ifeasible_gen_subtrees(tree: nx.DiGraph,
                           root: int,
                           M: int,
                           N: int = 1) -> Generator[tuple[int, set[int]]]
```

Generate M-feasible(connected) subtrees and roots in bottom-up way, which meet the memory constraint *M*.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks

**Returns**:

generator of subtree root and regarding subtree nodes

<a id="slambuc.alg.tree.layout.ilp.build_gen_tree_cfg_model"></a>

#### build\_gen\_tree\_cfg\_model

```python
def build_gen_tree_cfg_model(
        tree: nx.DiGraph,
        root: int = 1,
        flavors: list[Flavor] = (Flavor(), ),
        exec_calc: collections.abc.Callable[[int, int, int],
                                            int] = lambda i, t, n: t,
        L: int = math.inf,
        cp_end: int = None,
        delay: int = 1) -> tuple[lp.LpProblem, list[lp.LpVariable]]
```

Generate the configuration ILP model with the given *flavors*.

**Returns**:

tuple of the created model and list of decision variables

<a id="slambuc.alg.tree.layout.ilp.tree_gen_hybrid_partitioning"></a>

#### tree\_gen\_hybrid\_partitioning

```python
def tree_gen_hybrid_partitioning(tree: nx.DiGraph,
                                 root: int = 1,
                                 flavors: list[Flavor] = (Flavor(), ),
                                 exec_calc: collections.abc.Callable[
                                     [int, int, int], int] = lambda i, t, n: t,
                                 L: int = math.inf,
                                 cp_end: int = None,
                                 delay: int = 1,
                                 solver: lp.LpSolver = None,
                                 timeout: int = None,
                                 **lpargs) -> T_FRESULTS
```

Calculate minimal-cost partitioning of a tree based on configuration LP formulation and given *flavors*.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `flavors`: list of flavors resources given by the tuple of available *(memory, relative CPU cores)*
- `exec_calc`: function that calculates the effective runtimes from reference runtime and available CPU cores
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `delay`: invocation delay between blocks
- `solver`: specific solver class (default: COIN-OR CBC)
- `timeout`: time limit in sec
- `lpargs`: additional LP solver parameters

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.layout.ilp.recreate_st_from_gen_xdict"></a>

#### recreate\_st\_from\_gen\_xdict

```python
def recreate_st_from_gen_xdict(
        tree: nx.DiGraph, X: dict[Flavor,
                                  dict[int, list[lp.LpVariable]]]) -> T_FPART
```

Extract barrier nodes from variable names (x_{b}_{w}) and recreate partitioning blocks.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `X`: internal structure of decision variables

**Returns**:

partition blocks

<a id="slambuc.alg.tree.layout.ilp.build_gen_tree_mtx_model"></a>

#### build\_gen\_tree\_mtx\_model

```python
def build_gen_tree_mtx_model(
    tree: nx.DiGraph,
    root: int = 1,
    flavors: list[Flavor] = (Flavor(), ),
    exec_calc: collections.abc.Callable[[int, int, int],
                                        int] = lambda i, t, n: t,
    L: int = math.inf,
    cp_end: int = None,
    delay: int = 1
) -> tuple[lp.LpProblem, dict[int, dict[int, dict[int, lp.LpVariable]]]]
```

Generate the matrix ILP model with the given *flavors*.

**Returns**:

tuple of the created model and list of decision variables

<a id="slambuc.alg.tree.layout.ilp.tree_gen_mtx_partitioning"></a>

#### tree\_gen\_mtx\_partitioning

```python
def tree_gen_mtx_partitioning(tree: nx.DiGraph,
                              root: int = 1,
                              flavors: list[Flavor] = (Flavor(), ),
                              exec_calc: collections.abc.Callable[
                                  [int, int, int], int] = lambda i, t, n: t,
                              L: int = math.inf,
                              cp_end: int = None,
                              delay: int = 1,
                              solver: lp.LpSolver = None,
                              timeout: int = None,
                              **lpargs) -> T_FRESULTS
```

Calculate minimal-cost partitioning of a tree based on matrix LP formulation and given *flavors*.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `flavors`: list of flavors resources given by the tuple of available *(memory, relative CPU cores)*
- `exec_calc`: function that calculates the effective runtimes from reference runtime and available CPU cores
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `delay`: invocation delay between blocks
- `solver`: specific solver class (default: COIN-OR CBC)
- `timeout`: time limit in sec
- `lpargs`: additional LP solver parameters

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.layout.ilp.extract_st_from_gen_xmatrix"></a>

#### extract\_st\_from\_gen\_xmatrix

```python
def extract_st_from_gen_xmatrix(
        X: dict[Flavor, dict[int, dict[int, lp.LpVariable]]]) -> T_FPART
```

Extract barrier nodes from variable matrix(dict-of-dict) and recreate partitioning blocks.

**Arguments**:

- `X`: internal structure of decision variables

**Returns**:

partition blocks

<a id="slambuc.alg.tree.layout.ilp.all_gen_tree_mtx_partitioning"></a>

#### all\_gen\_tree\_mtx\_partitioning

```python
def all_gen_tree_mtx_partitioning(tree: nx.DiGraph,
                                  root: int = 1,
                                  flavors: list[Flavor] = (Flavor(), ),
                                  exec_calc: collections.abc.Callable[
                                      [int, int, int],
                                      int] = lambda i, t, n: t,
                                  L: int = math.inf,
                                  cp_end: int = None,
                                  delay: int = 1,
                                  solver: lp.LpSolver = None,
                                  timeout: int = None,
                                  **lpargs) -> list[T_FPART]
```

Calculate all minimal-cost partitioning variations of a tree based on matrix ILP formulation and *flavors*.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `flavors`: list of flavors resources given by the tuple of available *(memory, relative CPU cores)*
- `exec_calc`: function that calculates the effective runtimes from reference runtime and available CPU cores
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `delay`: invocation delay between blocks
- `solver`: specific solver class (default: COIN-OR CBC)
- `timeout`: time limit in sec
- `lpargs`: additional LP solver parameters

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.layout"></a>

# slambuc.alg.tree.layout

<a id="slambuc.alg.tree"></a>

# slambuc.alg.tree

<a id="slambuc.alg.tree.dp.greedy"></a>

# slambuc.alg.tree.dp.greedy

<a id="slambuc.alg.tree.dp.greedy.ichains_exhaustive"></a>

#### ichains\_exhaustive

```python
def ichains_exhaustive(tree: nx.DiGraph, root: int, M: int,
                       N: int) -> Generator[list[int]]
```

Calculate all combination of edge cuts and returns only if it is feasible wrt. the chain connectivity, M, and N.

Calculation is improved compared to brute force to only start calculating cuts from c_min.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound in MB
- `N`: upper CPU core bound

**Returns**:

generator of chain partitions

<a id="slambuc.alg.tree.dp.greedy.ifeasible_chains"></a>

#### ifeasible\_chains

```python
def ifeasible_chains(tree: nx.DiGraph, root: int, M: int,
                     N: int) -> Generator[list[int]]
```

Calculate only feasible chain partitions and returns the one which meets the limits M and N.

Calculation is improved compared to brute force to only calculate chain partitions based on the branching nodes.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound in MB
- `N`: upper CPU core bound

**Returns**:

generator of chain partitions

<a id="slambuc.alg.tree.dp.greedy.greedy_tree_partitioning"></a>

#### greedy\_tree\_partitioning

```python
def greedy_tree_partitioning(tree: nx.DiGraph,
                             root: int = 1,
                             M: int = math.inf,
                             N: int = math.inf,
                             L: int = math.inf,
                             cp_end: int = None,
                             delay: int = 1,
                             unit: int = 100,
                             ichains=ifeasible_chains,
                             only_cuts: bool = False) -> list[T_RESULTS]
```

Calculates minimal-cost partitioning of a service graph(tree) by iterating over all possible cuttings.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `unit`: rounding unit for the cost calculation (default: 100 ms)
- `ichains`: generator of chain partitions
- `only_cuts`: return the number of cuts instead of the calculated latency

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.dp.min"></a>

# slambuc.alg.tree.dp.min

<a id="slambuc.alg.tree.dp.min.MinTBlock"></a>

## MinTBlock Objects

```python
class MinTBlock(typing.NamedTuple)
```

Store subtree attributes for a given min subcase.

<a id="slambuc.alg.tree.dp.min.MinTBlock.w"></a>

#### w

Tailing node of the first block of the subtree partitioning

<a id="slambuc.alg.tree.dp.min.MinTBlock.c"></a>

#### c

Number of cuts the given subtree partitioning introduce on the critical path

<a id="slambuc.alg.tree.dp.min.MinTBlock.sum_cost"></a>

#### sum\_cost

Sum cost of the subtree partitioning

<a id="slambuc.alg.tree.dp.min.MinTBlock.cost"></a>

#### cost

Cost of the first block (with tail node w) in the subtree partitioning

<a id="slambuc.alg.tree.dp.min.MinTBlock.mem"></a>

#### mem

Sum memory of the first block

<a id="slambuc.alg.tree.dp.min.MinTBlock.max_rate"></a>

#### max\_rate

Maximum rate value of internal edge in the first block

<a id="slambuc.alg.tree.dp.min.MinTBlock.cpu"></a>

#### cpu

Sum CPU core need of the first block

<a id="slambuc.alg.tree.dp.min.min_tree_partitioning"></a>

#### min\_tree\_partitioning

```python
def min_tree_partitioning(tree: nx.DiGraph,
                          root: int = 1,
                          M: int = math.inf,
                          N: int = math.inf,
                          L: int = math.inf,
                          cp_end: int = None,
                          delay: int = 1,
                          unit: int = 100,
                          full: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes.

Cost calculation relies on the rounding *unit* and number of vCPU cores *N*, whereas platform invocation *delay*
is used for latency calculations.

It gives optimal result only in case the cost function regarding the chain attributes is sub-additive,
that is k_opt = k_min is guaranteed for each case.

Instead of full partitioning it only returns the list of barrier nodes.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `unit`: rounding unit for the cost calculation (default: 100 ms)
- `full`: return full blocks or just their ending nodes

**Returns**:

tuple of optimal partition, sum cost of the partitioning, and optimal number of cuts

<a id="slambuc.alg.tree.dp.min.extract_min_blocks"></a>

#### extract\_min\_blocks

```python
def extract_min_blocks(tree: nx.DiGraph,
                       DP: list[collections.deque[MinTBlock]],
                       root: int,
                       full: bool = True) -> T_BLOCK
```

Extract subtree roots of partitioning from the tailing nodes stored in the *DP* matrix.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `DP`: dynamic programming structure storing intermediate *MinTBlock* subcases
- `root`: root node of the graph
- `full`: calculate full blocks

**Returns**:

partitioning blocks

<a id="slambuc.alg.tree.dp.seq"></a>

# slambuc.alg.tree.dp.seq

<a id="slambuc.alg.tree.dp.seq.TBlock"></a>

## TBlock Objects

```python
class TBlock(typing.NamedTuple)
```

Store subtree attributes for a given seq subcase.

<a id="slambuc.alg.tree.dp.seq.TBlock.w"></a>

#### w

Tailing node of the first block of the subtree partitioning

<a id="slambuc.alg.tree.dp.seq.TBlock.sum_cost"></a>

#### sum\_cost

Sum cost of the subtree partitioning

<a id="slambuc.alg.tree.dp.seq.TBlock.cumsum"></a>

#### cumsum

Sum (cumulative) runtime of the first block (with tail node w) in the partitioning

<a id="slambuc.alg.tree.dp.seq.TBlock.mem"></a>

#### mem

Sum memory of the first block

<a id="slambuc.alg.tree.dp.seq.TBlock.max_rate"></a>

#### max\_rate

Maximum rate value of internal edge in the first block

<a id="slambuc.alg.tree.dp.seq.TBlock.cpu"></a>

#### cpu

Sum CPU core need of the first block

<a id="slambuc.alg.tree.dp.seq.seq_tree_partitioning"></a>

#### seq\_tree\_partitioning

```python
def seq_tree_partitioning(tree: nx.DiGraph,
                          root: int = 1,
                          M: int = math.inf,
                          N: int = math.inf,
                          L: int = math.inf,
                          cp_end: int = None,
                          delay: int = 1,
                          unit: int = 100,
                          full: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes leveraging
a bottom-up tree traversal approach.

Cost calculation relies on the rounding *unit* and number of vCPU cores *N*, whereas platform invocation *delay*
is used for latency calculations.

Details in: J. Czentye, I. Pelle and B. Sonkoly, "Cost-optimal Operation of Latency Constrained Serverless
Applications: From Theory to Practice," NOMS 2023-2023 IEEE/IFIP Network Operations and Management Symposium,
Miami, FL, USA, 2023, pp. 1-10, doi: 10.1109/NOMS56928.2023.10154412.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `unit`: rounding unit for the cost calculation (default: 100 ms)
- `full`: return full blocks or just their ending nodes

**Returns**:

tuple of optimal partition, sum cost of the partitioning, and optimal number of cuts

<a id="slambuc.alg.tree.dp.seq.extract_blocks"></a>

#### extract\_blocks

```python
def extract_blocks(tree: nx.DiGraph,
                   DP: list[collections.defaultdict[
                       collections.deque[TBlock]]],
                   root: int,
                   cp_end: int,
                   c_opt: int,
                   full: bool = True) -> T_PART
```

Extract subtree roots of partitioning from the tailing nodes stored in the *DP* matrix.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `DP`: dynamic programming structure storing intermediate *TBlock* subcases
- `root`: root node of the graph
- `cp_end`: tail node of the critical path
- `c_opt`: calculated optimal cut size
- `full`: calculate full blocks

**Returns**:

partitioning blocks

<a id="slambuc.alg.tree.dp.meta"></a>

# slambuc.alg.tree.dp.meta

<a id="slambuc.alg.tree.dp.meta.TPart"></a>

## TPart Objects

```python
class TPart(typing.NamedTuple)
```

Store subtree attributes for a given meta subcase.

<a id="slambuc.alg.tree.dp.meta.TPart.barr"></a>

#### barr

Barrier/heading nodes of the given subtree partitioning

<a id="slambuc.alg.tree.dp.meta.TPart.cost"></a>

#### cost

Sum cost of the partitioning

<a id="slambuc.alg.tree.dp.meta.meta_tree_partitioning"></a>

#### meta\_tree\_partitioning

```python
def meta_tree_partitioning(tree: nx.DiGraph,
                           root: int = 1,
                           M: int = math.inf,
                           N: int = math.inf,
                           L: int = math.inf,
                           cp_end: int = None,
                           delay: int = 1,
                           unit: int = 100,
                           only_barr: bool = False,
                           partition=chain_partitioning,
                           barriers=extract_barr) -> T_BRESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes using
the *partition* function to partition subchains independently.

Cost calculation relies on the rounding *unit* and number of vCPU cores *N*, whereas platform invocation *delay*
is used for latency calculations.

It gives optimal result only in case the cost function regarding the chain attributes is sub-additive,
that is k_opt = k_min is guaranteed for each case.

Instead of full partitioning it only returns the list of barrier nodes.

Details in: J. Czentye, I. Pelle and B. Sonkoly, "Cost-optimal Operation of Latency Constrained Serverless
Applications: From Theory to Practice," NOMS 2023-2023 IEEE/IFIP Network Operations and Management Symposium,
Miami, FL, USA, 2023, pp. 1-10, doi: 10.1109/NOMS56928.2023.10154412.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `unit`: rounding unit for the cost calculation (default: 100 ms)
- `only_barr`: return the subtree roots (barrier nodes) instead of full node partitioning
- `partition`: function that partitions chain into blocks wrt. M and L
- `barriers`: function that extracts barrier nodes from _partition_'s returned data structure

**Returns**:

tuple of barrier nodes, sum cost of the partitioning, and optimal number of cuts

<a id="slambuc.alg.tree.dp.seq_state"></a>

# slambuc.alg.tree.dp.seq\_state

<a id="slambuc.alg.tree.dp.seq_state.cacheless_chain_partitioning"></a>

#### cacheless\_chain\_partitioning

```python
def cacheless_chain_partitioning(tree: nx.DiGraph,
                                 root: int = 1,
                                 M: int = math.inf,
                                 N: int = 1,
                                 L: int = math.inf,
                                 cp_end: int = None,
                                 delay: int = 1,
                                 valid: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning using *seq_tree_partitioning* without considering data externalization.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `valid`: return only L-feasible solutions

**Returns**:

tuple of optimal partition, sum cost of the partitioning, and optimal number of cuts

<a id="slambuc.alg.tree.dp.seq_state.stateful_chain_partitioning"></a>

#### stateful\_chain\_partitioning

```python
def stateful_chain_partitioning(tree: nx.DiGraph,
                                root: int = 1,
                                M: int = math.inf,
                                N: int = 1,
                                L: int = math.inf,
                                cp_end: int = None,
                                delay: int = 1) -> T_RESULTS
```

Calculates minimal-cost partitioning using *seq_tree_partitioning* while considering data implicit state

externalization.

Input tree is preprocessed and function runtimes are altered to incorporate data read/write overheads.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks

**Returns**:

tuple of optimal partition, sum cost of the partitioning, and optimal number of cuts

<a id="slambuc.alg.tree.dp"></a>

# slambuc.alg.tree.dp

<a id="slambuc.alg.tree.par.pseudo_mp"></a>

# slambuc.alg.tree.par.pseudo\_mp

<a id="slambuc.alg.tree.par.pseudo_mp.pseudo_par_mp_ltree_partitioning"></a>

#### pseudo\_par\_mp\_ltree\_partitioning

```python
def pseudo_par_mp_ltree_partitioning(tree: nx.DiGraph,
                                     root: int = 1,
                                     M: int = math.inf,
                                     L: int = math.inf,
                                     N: int = 1,
                                     cp_end: int = None,
                                     delay: int = 1,
                                     bidirectional: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes.

Partitioning is calculated using the left-right tree traversal approach.

Arbitrary disjoint subtrees are partitioned in separate subprocesses.

Block metrics are calculated based on parallelized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `N`: available CPU core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `bidirectional`: use bidirectional subcase elimination (may introduce quadratic increase in the worst case)

**Returns**:

tuple of optimal partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.tree.par.greedy"></a>

# slambuc.alg.tree.par.greedy

<a id="slambuc.alg.tree.par.greedy.isubtrees_exhaustive"></a>

#### isubtrees\_exhaustive

```python
def isubtrees_exhaustive(tree: nx.DiGraph,
                         root: int,
                         M: int,
                         N: int = 1) -> T_BARRS_GEN
```

Calculate all combinations of edge cuts and returns only if it is feasible wrt. the memory limit *M*.

Block metrics are calculated based on parallelized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound in MB
- `N`: available CPU core count

**Returns**:

generator of feasible subtrees' barrier nodes

<a id="slambuc.alg.tree.par.greedy.greedy_par_tree_partitioning"></a>

#### greedy\_par\_tree\_partitioning

```python
def greedy_par_tree_partitioning(tree: nx.DiGraph,
                                 root: int = 1,
                                 M: int = math.inf,
                                 L: int = math.inf,
                                 N: int = 1,
                                 cp_end: int = None,
                                 delay: int = 1) -> T_RESULTS
```

Calculate minimal-cost partitioning of a service graph(tree) by greedily iterating over all possible cuttings.

Block metrics are calculated based on parallelized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `L`: latency limit defined on the critical path (in ms)
- `N`: available CPU core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `delay`: invocation delay between blocks

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.par.pseudo"></a>

# slambuc.alg.tree.par.pseudo

<a id="slambuc.alg.tree.par.pseudo.SubParBTreePart"></a>

## SubParBTreePart Objects

```python
class SubParBTreePart(typing.NamedTuple)
```

Store subtree partitioning attributes for a given subcase.

<a id="slambuc.alg.tree.par.pseudo.SubParBTreePart.cost"></a>

#### cost

Optimal sum cost of the subtree partitioning (OPT)

<a id="slambuc.alg.tree.par.pseudo.SubParBTreePart.top_cost"></a>

#### top\_cost

Cost of the topmost subtree block

<a id="slambuc.alg.tree.par.pseudo.SubParBTreePart.top_blk"></a>

#### top\_blk

Nodes of the topmost block

<a id="slambuc.alg.tree.par.pseudo.SubParBTreePart.barr"></a>

#### barr

Barrier/heading nodes of the given subtree partitioning

<a id="slambuc.alg.tree.par.pseudo.pseudo_par_btree_partitioning"></a>

#### pseudo\_par\_btree\_partitioning

```python
def pseudo_par_btree_partitioning(tree: nx.DiGraph,
                                  root: int = 1,
                                  M: int = math.inf,
                                  L: int = math.inf,
                                  N: int = 1,
                                  cp_end: int = None,
                                  delay: int = 1,
                                  bidirectional: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes, while
applying bottom-up tree traversal approach.

Block metrics are calculated based on parallelized execution platform model.

Provide suboptimal partitioning due to the inaccurate latency calculation that directly comes from the bottom-up
tree traversal approach.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `N`: available CPU core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `bidirectional`: use bidirectional subcase elimination (may introduce quadratic increase in the worst case)

**Returns**:

tuple of optimal partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.tree.par.pseudo.pseudo_par_ltree_partitioning"></a>

#### pseudo\_par\_ltree\_partitioning

```python
def pseudo_par_ltree_partitioning(tree: nx.DiGraph,
                                  root: int = 1,
                                  M: int = math.inf,
                                  L: int = math.inf,
                                  N: int = 1,
                                  cp_end: int = None,
                                  delay: int = 1,
                                  bidirectional: bool = True) -> T_RESULTS
```

Calculates minimal-cost partitioning of a service graph(tree) with respect to an upper bound **M** on the total

memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes, while
applying left-right tree traversal approach.

Block metrics are calculated based on parallelized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `N`: available CPU core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `bidirectional`: use bidirectional subcase elimination (may introduce quadratic increase in the worst case)

**Returns**:

tuple of optimal partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.tree.par.ilp"></a>

# slambuc.alg.tree.par.ilp

<a id="slambuc.alg.tree.par.ilp.ifeasible_par_greedy_subtrees"></a>

#### ifeasible\_par\_greedy\_subtrees

```python
def ifeasible_par_greedy_subtrees(
        tree: nx.DiGraph,
        root: int,
        M: int,
        N: int = 1) -> Generator[tuple[int, set[int]]]
```

Generate feasible subtrees in a combinatorial way, which meet the connectivity and memory constraint *M*.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks

**Returns**:

generator of subtree root and regarding subtree nodes

<a id="slambuc.alg.tree.par.ilp.ifeasible_par_subtrees"></a>

#### ifeasible\_par\_subtrees

```python
def ifeasible_par_subtrees(tree: nx.DiGraph,
                           root: int,
                           M: int,
                           N: int = 1) -> Generator[tuple[int, set[int]]]
```

Generate M-feasible(connected) subtrees and roots in a bottom-up way, which meet the memory constraint *M*.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `N`: upper CPU core bound of the partition blocks

**Returns**:

generator of subtree root and regarding subtree nodes

<a id="slambuc.alg.tree.par.ilp.build_par_tree_cfg_model"></a>

#### build\_par\_tree\_cfg\_model

```python
def build_par_tree_cfg_model(
    tree: nx.DiGraph,
    root: int = 1,
    M: int = math.inf,
    L: int = math.inf,
    N: int = 1,
    cpath: set[int] = frozenset(),
    delay: int = 1,
    isubtrees: iter = ifeasible_par_subtrees
) -> tuple[lp.LpProblem, dict[int, list[lp.LpVariable]]]
```

Generate the configuration ILP model using parallel metric calculation.

**Returns**:

tuple of the created model and list of decision variables

<a id="slambuc.alg.tree.par.ilp.tree_par_cfg_partitioning"></a>

#### tree\_par\_cfg\_partitioning

```python
def tree_par_cfg_partitioning(tree: nx.DiGraph,
                              root: int = 1,
                              M: int = math.inf,
                              L: int = math.inf,
                              N: int = 1,
                              cp_end: int = None,
                              delay: int = 1,
                              solver: lp.LpSolver = None,
                              timeout: int = None,
                              **lpargs) -> T_RESULTS
```

Calculate minimal-cost partitioning of a tree based on configuration LP formulation and greedy subcase

generation.

Block metrics are calculated based on parallelized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `N`: available CPU core count
- `delay`: invocation delay between blocks
- `solver`: specific solver class (default: COIN-OR CBC)
- `timeout`: time limit in sec
- `lpargs`: additional LP solver parameters

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.par.ilp.tree_par_hybrid_partitioning"></a>

#### tree\_par\_hybrid\_partitioning

```python
def tree_par_hybrid_partitioning(tree: nx.DiGraph,
                                 root: int = 1,
                                 M: int = math.inf,
                                 L: int = math.inf,
                                 N: int = 1,
                                 cp_end: int = None,
                                 delay: int = 1,
                                 solver: lp.LpSolver = None,
                                 timeout: int = None,
                                 **lpargs) -> T_RESULTS
```

Calculate minimal-cost partitioning of a tree based on configuration LP formulation and hybrid subcase

generation.

Block metrics are calculated based on parallelized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `N`: available CPU core count
- `delay`: invocation delay between blocks
- `solver`: specific solver class (default: COIN-OR CBC)
- `timeout`: time limit in sec
- `lpargs`: additional LP solver parameters

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.par.ilp.build_greedy_par_tree_mtx_model"></a>

#### build\_greedy\_par\_tree\_mtx\_model

```python
def build_greedy_par_tree_mtx_model(
    tree: nx.DiGraph,
    root: int = 1,
    M: int = math.inf,
    L: int = math.inf,
    N: int = 1,
    cpath: set[int] = frozenset(),
    delay: int = 1
) -> tuple[lp.LpProblem, dict[int, dict[int, lp.LpVariable]]]
```

Generate the matrix ILP model using greedy subcase building and parallel metric calculation.

**Returns**:

tuple of the created model and list of decision variables

<a id="slambuc.alg.tree.par.ilp.build_par_tree_mtx_model"></a>

#### build\_par\_tree\_mtx\_model

```python
def build_par_tree_mtx_model(
    tree: nx.DiGraph,
    root: int = 1,
    M: int = math.inf,
    L: int = math.inf,
    N: int = 1,
    cpath: set[int] = frozenset(),
    delay: int = 1
) -> tuple[lp.LpProblem, dict[int, dict[int, lp.LpVariable]]]
```

Generate the matrix ILP model based on parallel metric calculations.

**Returns**:

tuple of the created model and list of decision variables

<a id="slambuc.alg.tree.par.ilp.tree_par_mtx_partitioning"></a>

#### tree\_par\_mtx\_partitioning

```python
def tree_par_mtx_partitioning(tree: nx.DiGraph,
                              root: int = 1,
                              M: int = math.inf,
                              L: int = math.inf,
                              N: int = 1,
                              cp_end: int = None,
                              delay: int = 1,
                              solver: lp.LpSolver = None,
                              timeout: int = None,
                              **lpargs) -> T_RESULTS
```

Calculate minimal-cost partitioning of a tree based on matrix LP formulation.

Block metrics are calculated based on parallelized execution platform model.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `L`: latency limit defined on the critical path (in ms)
- `N`: available CPU  core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `delay`: invocation delay between blocks
- `solver`: specific solver class (default: COIN-OR CBC)
- `timeout`: time limit in sec
- `lpargs`: additional LP solver parameters

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.par.ilp.all_par_tree_mtx_partitioning"></a>

#### all\_par\_tree\_mtx\_partitioning

```python
def all_par_tree_mtx_partitioning(tree: nx.DiGraph,
                                  root: int = 1,
                                  M: int = math.inf,
                                  L: int = math.inf,
                                  N: int = 1,
                                  cp_end: int = None,
                                  delay: int = 1,
                                  solver: lp.LpSolver = None,
                                  timeout: int = None,
                                  **lpargs) -> list[T_RESULTS]
```

Calculate all minimal-cost partitioning variations of a tree based on matrix ILP formulation.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks (in MB)
- `L`: latency limit defined on the critical path (in ms)
- `N`: available CPU  core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `delay`: invocation delay between blocks
- `solver`: specific solver class (default: COIN-OR CBC)
- `timeout`: time limit in sec
- `lpargs`: additional LP solver parameters

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.tree.par"></a>

# slambuc.alg.tree.par

<a id="slambuc.alg.ext.greedy"></a>

# slambuc.alg.ext.greedy

<a id="slambuc.alg.ext.greedy.get_bounded_greedy_block"></a>

#### get\_bounded\_greedy\_block

```python
def get_bounded_greedy_block(
    tree: nx.DiGraph,
    root: int,
    M: int,
    N: int = 1,
    cp_end: int = None,
    cp_cuts: set[int] = frozenset()
) -> tuple[T_BLOCK, list[int]]
```

Calculate a partition block based on the memory limit *M* by iteratively merging edges with the largest weights

started from the given *root*.

Filter out mandatory cuts of *cp_cuts* on the cpath form merging, while merges other cpath edges.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), edge rate and edge data unit size
- `root`: root node of the tree
- `M`: upper memory bound of the partition blocks in MB
- `N`: available CPU core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `cp_cuts`: barrier nodes of mandatory cuts on the critical path

**Returns**:

calculated partition block and the separated neighbouring nodes

<a id="slambuc.alg.ext.greedy.min_weight_greedy_partitioning"></a>

#### min\_weight\_greedy\_partitioning

```python
def min_weight_greedy_partitioning(tree: nx.DiGraph,
                                   root: int = 1,
                                   M: int = math.inf,
                                   N: int = 1,
                                   delay: int = 1,
                                   metrics: bool = True,
                                   **kwargs) -> T_RESULTS
```

Calculates memory-bounded tree partitioning in a greedy manner without any latency limit.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), edge rate and edge data unit size
- `root`: root node of the tree
- `M`: upper memory bound of the partition blocks in MB
- `N`: available CPU core count
- `delay`: invocation delay between blocks
- `metrics`: return calculated sum cost and critical path latency

**Returns**:

tuple of derived partitioning, sum cost, and the latency on the critical path (root, cp_end)

<a id="slambuc.alg.ext.greedy.get_feasible_cpath_split"></a>

#### get\_feasible\_cpath\_split

```python
def get_feasible_cpath_split(tree: nx.DiGraph,
                             root: int,
                             cp_end: int,
                             M: int,
                             L: int,
                             N: int = 1,
                             delay: int = 1) -> set[int]
```

Calculate feasible splitting of the critical path that meets given memory *M* and latency *L* limits.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), edge rate and edge data unit size
- `root`: root node of the tree
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `N`: available CPU core count
- `delay`: invocation delay between blocks

**Returns**:

set of barrier nodes of calculated critical path blocks

<a id="slambuc.alg.ext.greedy.min_weight_partition_heuristic"></a>

#### min\_weight\_partition\_heuristic

```python
def min_weight_partition_heuristic(tree: nx.DiGraph,
                                   root: int = 1,
                                   M: int = math.inf,
                                   L: int = math.inf,
                                   N: int = 1,
                                   cp_end: int = None,
                                   delay: int = 1,
                                   metrics: bool = True) -> T_RESULTS
```

Greedy heuristic algorithm to calculate partitioning of the given *tree* regarding the given memory *M* and

latency *L* limits.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), edge rate and edge data unit size
- `root`: root node of the tree
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `N`: available CPU core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `metrics`: return calculated sum cost and critical path latency

**Returns**:

tuple of derived partitioning, sum cost, and the latency on the critical path (root, cp_end)

<a id="slambuc.alg.ext.baseline"></a>

# slambuc.alg.ext.baseline

<a id="slambuc.alg.ext.baseline.baseline_singleton_partitioning"></a>

#### baseline\_singleton\_partitioning

```python
def baseline_singleton_partitioning(tree: nx.DiGraph,
                                    root: int = 1,
                                    N: int = 1,
                                    cp_end: int = None,
                                    delay: int = 1,
                                    **kwargs) -> T_RESULTS
```

Derive the trivial partitioning of grouping all nodes into one single block.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rate and data
- `root`: root node of the graph
- `N`: available CPU core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks

**Returns**:

tuple of partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.ext.baseline.baseline_no_partitioning"></a>

#### baseline\_no\_partitioning

```python
def baseline_no_partitioning(tree: nx.DiGraph,
                             root: int = 1,
                             N: int = 1,
                             cp_end: int = None,
                             delay: int = 1,
                             **kwargs) -> T_RESULTS
```

Derive the trivial solution of not merging any of the given tree nodes.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rate and data
- `root`: root node of the graph
- `N`: available CPU core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks

**Returns**:

tuple of partitioning, reached sum cost and latency on the critical path

<a id="slambuc.alg.ext.min_cut"></a>

# slambuc.alg.ext.min\_cut

<a id="slambuc.alg.ext.min_cut.min_weight_subchain_split"></a>

#### min\_weight\_subchain\_split

```python
def min_weight_subchain_split(tree: nx.DiGraph, root: int) -> set[int]
```

Return chain-based edge cuts with the minimal edge weight (amount of transferred data).

The splitting marks the edge with the largest weight at each branching nodes to be a must-merge edge.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), edge rate and edge data unit size
- `root`: root node of the tree

**Returns**:

set of barrier nodes

<a id="slambuc.alg.ext.min_cut.min_weight_chain_decomposition"></a>

#### min\_weight\_chain\_decomposition

```python
def min_weight_chain_decomposition(tree: nx.DiGraph,
                                   root: int,
                                   N: int = 1,
                                   cp_end: int = None,
                                   delay: int = 1,
                                   metrics: bool = True,
                                   **kwargs) -> T_RESULTS
```

Minimal edge-weight chain-based tree partitioning (O(n)) without memory and latency constraints.

Although latency is not considered on the critical path the algorithm reports it with the sum cost.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms) and edge rate
- `root`: root node of the tree
- `N`: available CPU core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `metrics`: return calculated sum cost and critical path latency

**Returns**:

tuple of derived partitioning, sum cost, and the latency on the critical path (root, cp_end)

<a id="slambuc.alg.ext.min_cut.min_weight_ksplit"></a>

#### min\_weight\_ksplit

```python
def min_weight_ksplit(tree: nx.DiGraph, root: int, k: int) -> set[int]
```

Minimal data-transfer tree clustering into *k* clusters with k-1 cuts without memory and latency constraints.

The clustering algorithm is based on the maximum split clustering algorithm(O(n^3)) which ranks the edges (paths)
based on the amount of transferred data.

Details in: M. Maravalle et al.: “Clustering on trees,” Computational Statistics & Data Analysis, vol. 24, no. 2,
pp. 217–234, Apr. 1997, doi: 10.1016/S0167-9473(96)00062-X.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), edge rate and edge data unit size
- `root`: root node of the tree
- `k`: number of clusters

**Returns**:

set of barrier nodes

<a id="slambuc.alg.ext.min_cut.min_weight_ksplit_clustering"></a>

#### min\_weight\_ksplit\_clustering

```python
def min_weight_ksplit_clustering(tree: nx.DiGraph,
                                 root: int,
                                 k: int = None,
                                 N: int = 1,
                                 cp_end: int = None,
                                 delay: int = 1,
                                 metrics: bool = True,
                                 **kwargs) -> T_RESULTS
```

Minimal data-transfer tree clustering into *k* clusters (with k-1 cuts) without memory and latency constraints.

Although latency is not considered on the critical path the algorithm reports it along with the sum cost.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), edge rate and edge data unit size
- `root`: root node of the tree
- `k`: number of clusters
- `N`: available CPU core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `metrics`: return calculated sum cost and critical path latency

**Returns**:

tuple of derived partitioning, sum cost, and the latency on the critical path (root, cp_end)

<a id="slambuc.alg.ext.min_cut.min_weight_tree_clustering"></a>

#### min\_weight\_tree\_clustering

```python
def min_weight_tree_clustering(tree: nx.DiGraph,
                               root: int,
                               L: int = math.inf,
                               N: int = 1,
                               cp_end: int = None,
                               delay: int = 1,
                               metrics: bool = True,
                               **kwargs) -> T_RESULTS
```

Minimal data-transfer tree clustering into without memory constraints.

Iteratively calculates *k-1* different ksplit clustering in reverse order until an L-feasible solution is found.

Although latency is not considered on the critical path the algorithm reports it with the sum cost.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), edge rate and edge data unit size
- `root`: root node of the tree
- `L`: latency limit defined on the critical path in ms
- `N`: available CPU core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks
- `metrics`: return calculated sum cost and critical path latency

**Returns**:

tuple of derived partitioning, sum cost, and the latency on the critical path (root, cp_end)

<a id="slambuc.alg.ext.csp"></a>

# slambuc.alg.ext.csp

<a id="slambuc.alg.ext.csp.encode_state"></a>

#### encode\_state

```python
def encode_state(grp: T_BLOCK, flavor: Flavor) -> str
```

Encode DAG node name with flavor's memory as a unique str (hashable).

**Arguments**:

- `grp`: partition block
- `flavor`: assigned *flavor*

**Returns**:

encoded partition block

<a id="slambuc.alg.ext.csp.decode_state"></a>

#### decode\_state

```python
def decode_state(name: str) -> list[T_BLOCK, str]
```

Decode DAG node name from encoded str into partition block (list of int) and flavor's memory (mem).

**Arguments**:

- `name`: encoded partition block

**Returns**:

decoded block and assigned flavor

<a id="slambuc.alg.ext.csp.ibuild_gen_csp_dag"></a>

#### ibuild\_gen\_csp\_dag

```python
def ibuild_gen_csp_dag(
        tree: nx.DiGraph,
        root: int = 1,
        flavors: list[Flavor] = (Flavor(), ),
        exec_calc: Callable[[int, int, int], int] = lambda i, t, n: t,
        cpath: set[int] = frozenset(),
        delay: int = 1) -> Generator[nx.DiGraph, list[list[int]]]
```

Calculate all state-space DAGs of the given *tree* based on the alternative chain decompositions.

The given flavors as list of (memory, CPU, cost_factor) tuples define the available memory (and group upper limit),
available relative vCPU cores and relative cost multiplier.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rate
- `root`: root node of the graph
- `flavors`: list of flavors resources given by the tuple of available *(memory, relative CPU cores)*
- `exec_calc`: function that calculates the effective runtimes from reference runtime and available CPU cores
- `cpath`: critical path in the form of subchain[root -> cp_end]
- `delay`: invocation delay between blocks

**Returns**:

generated DAG graph and the related nodes of the flattened tree

<a id="slambuc.alg.ext.csp.csp_tree_partitioning"></a>

#### csp\_tree\_partitioning

```python
def csp_tree_partitioning(tree: nx.DiGraph,
                          root: int = 1,
                          M: int = math.inf,
                          L: int = math.inf,
                          N: int = 1,
                          cp_end: int = None,
                          delay: int = 1,
                          exhaustive: bool = True,
                          solver=cspy.BiDirectional,
                          timeout: int = None,
                          **cspargs) -> T_RESULTS
```

Calculate minimal-cost partitioning of a *tree* based on constrained shortest path (CSP) formalization

without considering flavor assignment.

Details in: T. Elgamal at al.: “Costless: Optimizing Cost of Serverless Computing through Function Fusion
and Placement,” in 2018 IEEE/ACM Symposium on Edge Computing (SEC), 2018, pp. 300–312. doi: 10.1109/SEC.2018.00029.

**Arguments**:

- `tree`: service tree annotated with node runtime(ms), memory(MB) and edge rate
- `root`: root node of the graph
- `M`: upper memory bound of the partition blocks in MB
- `L`: latency limit defined on the critical path in ms
- `N`: available CPU core count
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `delay`: invocation delay between blocks
- `exhaustive`: iterate over all topological ordering of the service tree or stop at first feasible solution
- `solver`: specific solver class (default: cspy.BiDirectional)
- `timeout`: time limit in sec
- `cspargs`: additional CSP solver parameters

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.ext.csp.csp_gen_tree_partitioning"></a>

#### csp\_gen\_tree\_partitioning

```python
def csp_gen_tree_partitioning(tree: nx.DiGraph,
                              root: int = 1,
                              flavors: list[tuple[int,
                                                  int]] = ((math.inf, 1), ),
                              exec_calc: collections.abc.Callable[
                                  [int, int], int] = lambda i, t, n: t,
                              L: int = math.inf,
                              cp_end: int = None,
                              delay: int = 1,
                              solver=cspy.BiDirectional,
                              timeout: int = None,
                              **cspargs) -> T_RESULTS
```

Calculate minimal-cost partitioning of a *tree* based on constrained shortest path (CSP) formalization with

incorporated flavor assignment.

Details in: T. Elgamal at al.: “Costless: Optimizing Cost of Serverless Computing through Function Fusion
and Placement,” in 2018 IEEE/ACM Symposium on Edge Computing (SEC), 2018, pp. 300–312. doi: 10.1109/SEC.2018.00029.

**Arguments**:

- `tree`: service graph annotated with node runtime(ms), memory(MB) and edge rate
- `root`: root node of the graph
- `flavors`: list of flavors resources given by the tuple of available *(memory, rel CPU cores, cost factor)*
- `exec_calc`: function that calculates the effective runtimes from reference runtime and available CPU cores
- `L`: latency limit defined on the critical path (in ms)
- `cp_end`: tail node of the critical path in the form of subchain[root -> c_pend]
- `delay`: invocation delay between blocks
- `solver`: specific solver class (default: cspy.BiDirectional)
- `timeout`: time limit in sec
- `cspargs`: additional CSP solver parameters

**Returns**:

tuple of list of best partitions, sum cost of the partitioning, and resulted latency

<a id="slambuc.alg.ext.csp.extract_grp_from_path"></a>

#### extract\_grp\_from\_path

```python
def extract_grp_from_path(path: list[str], flavors: bool = True) -> T_PART
```

Extract partitioning from *path* and recreate partition blocks.

**Arguments**:

- `path`: solution path of the CSP graph
- `flavors`: whether return flavors or not

**Returns**:

resulted partitioning blocks

<a id="slambuc.alg.ext"></a>

# slambuc.alg.ext

<a id="slambuc.alg"></a>

# slambuc.alg

<a id="slambuc.alg.T_BLOCK"></a>

#### T\_BLOCK

list of block nodes

<a id="slambuc.alg.T_PART"></a>

#### T\_PART

partitioning as list of blocks

<a id="slambuc.alg.T_RESULTS"></a>

#### T\_RESULTS

Partitioning, sum cost, sum latency

<a id="slambuc.alg.T_IBLOCK"></a>

#### T\_IBLOCK

Block interval start and end nodes

<a id="slambuc.alg.T_BARRS"></a>

#### T\_BARRS

list/set of barrier nodes

<a id="slambuc.alg.util"></a>

# slambuc.alg.util

<a id="slambuc.alg.util.verify_limits"></a>

#### verify\_limits

```python
def verify_limits(tree: nx.DiGraph, cpath: set[int], M: int | float,
                  L: int | float) -> tuple[bool, bool]
```

Verify that given limits *M*, *L*, and *N* based on the given *tree* allow feasible solution.

**Arguments**:

- `tree`: input tree
- `cpath`: nodes of critical path
- `M`: memory upper bound
- `L`: latency upper bound

**Returns**:

boolean values of satisfied limits M and L

<a id="slambuc.alg.util.ipostorder_dfs"></a>

#### ipostorder\_dfs

```python
def ipostorder_dfs(tree: nx.DiGraph,
                   source: int,
                   inclusive: bool = True) -> Generator[tuple[int, int]]
```

Return the existing predecessor and node tuple in a DFS traversal of the given *tree* in a post/reversed order.

**Arguments**:

- `tree`: input tree
- `source`: starting node
- `inclusive`: also return the source node

**Returns**:

generator of tree nodes

<a id="slambuc.alg.util.ipostorder_tabu_dfs"></a>

#### ipostorder\_tabu\_dfs

```python
def ipostorder_tabu_dfs(tree: nx.DiGraph,
                        source: int,
                        tabu: set = None,
                        inclusive: bool = True) -> Generator[tuple[int, int]]
```

Return nodes of *tree* in a postorder DFS traversal excluding descendants of nodes in *tabu* set.

**Arguments**:

- `tree`: input tree
- `source`: starting node
- `tabu`: tabu node set
- `inclusive`: also return the source node

**Returns**:

generator of tree nodes

<a id="slambuc.alg.util.ipostorder_edges"></a>

#### ipostorder\_edges

```python
def ipostorder_edges(tree: nx.DiGraph,
                     source: int,
                     data: bool = False) -> Generator[tuple[int, int]]
```

Return the edges (head, tail) in a DFS traversal of the given *tree* in a post/reversed order with edge data.

**Arguments**:

- `tree`: input tree
- `source`: starting node
- `data`: return edge data

**Returns**:

generator of edges

<a id="slambuc.alg.util.ileft_right_dfs"></a>

#### ileft\_right\_dfs

```python
def ileft_right_dfs(
        tree: nx.DiGraph, source: int
) -> Generator[tuple[tuple[int, int], int, tuple[int, int]]]
```

Return edges in left-right traversal along with the previously visited uncle and sibling edges.

**Arguments**:

- `tree`: input tree
- `source`: starting node

**Returns**:

generator of interested nodes

<a id="slambuc.alg.util.ileft_right_dfs_idx"></a>

#### ileft\_right\_dfs\_idx

```python
def ileft_right_dfs_idx(tree: nx.DiGraph,
                        source: int) -> Generator[tuple[int, int]]
```

Return nodes of the given *tree* in left-right traversal along with the index of the considered child node.

**Arguments**:

- `tree`: input tree
- `source`: starting node

**Returns**:

generator of interested node indices

<a id="slambuc.alg.util.ichain"></a>

#### ichain

```python
def ichain(tree: nx.DiGraph, start: int, leaf: int) -> Generator[int]
```

Generator over the nodes of the chain from *start* node to *leaf* node.

**Arguments**:

- `tree`: input tree
- `start`: first node
- `leaf`: last node

**Returns**:

generator of chain nodes

<a id="slambuc.alg.util.ibacktrack_chain"></a>

#### ibacktrack\_chain

```python
def ibacktrack_chain(tree: nx.DiGraph, start: int,
                     leaf: int) -> Generator[int]
```

Return the node of a chain in the *tree* in backward order from *leaf* to *start* node.

**Arguments**:

- `tree`: input tree
- `start`: first node
- `leaf`: last node

**Returns**:

generator of chain nodes

<a id="slambuc.alg.util.isubchains"></a>

#### isubchains

```python
def isubchains(
        tree: nx.DiGraph,
        start: int,
        leaf: int = None) -> Generator[tuple[list[int], list[int]], set[int]]
```

Generator over the subchains and its branches from *start* to all reachable leaf where the subchain is bisected

at the last node from which the specific *leaf* is still reachable.

**Arguments**:

- `tree`: input tree
- `start`: first node
- `leaf`: last node

**Returns**:

generator of chain node parts and branches

<a id="slambuc.alg.util.iflattened_tree"></a>

#### iflattened\_tree

```python
def iflattened_tree(tree: nx.DiGraph, root: int) -> Generator[list[int]]
```

Generate chain decomposition of the given *tree* started from node *root*.

**Arguments**:

- `tree`: input tree
- `root`: root node

**Returns**:

generator of decomposed chains

<a id="slambuc.alg.util.isubtree_bfs"></a>

#### isubtree\_bfs

```python
def isubtree_bfs(tree: nx.DiGraph, root: int) -> Generator[int]
```

Return nodes in BFS traversal of the given *tree* started from *root*.

**Arguments**:

- `tree`: input tree
- `root`: root node

**Returns**:

generator of tree nodes

<a id="slambuc.alg.util.isubtrees"></a>

#### isubtrees

```python
def isubtrees(tree: nx.DiGraph,
              barrs: T_BARRS) -> Generator[tuple[int, list[int]]]
```

Return the barrier nodes and subtrees of the given *tree* marked by the *barr* nodes.

**Arguments**:

- `tree`: input tree
- `barrs`: set of barrier nodes

**Returns**:

generator of barrier and regarding subtree nodes

<a id="slambuc.alg.util.itop_subtree_nodes"></a>

#### itop\_subtree\_nodes

```python
def itop_subtree_nodes(tree: nx.DiGraph, root: int,
                       barrs: T_BARRS) -> Generator[int]
```

Return the nodes of the top subtree with *root* of the given *tree* cut by the *barr* nodes.

**Arguments**:

- `tree`: input tree
- `root`: root node
- `barrs`: set of barrier nodes

**Returns**:

generator of topmost block's nodes

<a id="slambuc.alg.util.induced_subtrees"></a>

#### induced\_subtrees

```python
def induced_subtrees(
    tree: nx.DiGraph,
    root: int,
    only_nodes: bool = False
) -> Generator[tuple[tuple[int, int], list[int | tuple[int]]]]
```

Recursively generate the ingress edge of subtrees and all reachable edges / nodes in the given subtree.

**Arguments**:

- `tree`: input tree
- `root`: root node
- `only_nodes`: return only subtree nodes instead of edges

**Returns**:

generator of ingress and covered edges

<a id="slambuc.alg.util.ipowerset"></a>

#### ipowerset

```python
def ipowerset(data: list[int], start: int = 0) -> Generator[list[int]]
```

Generate the powerset of the given *data* beginning to count the sets from size *start*.

**Arguments**:

- `data`: list of data values
- `start`: lower bound of set size

**Returns**:

generator of subsets

<a id="slambuc.alg.util.iser_mul_factor"></a>

#### iser\_mul\_factor

```python
def iser_mul_factor(rate: list[int]) -> Generator[int]
```

Generator over the **pessimistic** number of function instances inside a block assuming serialized execution model.

**Arguments**:

- `rate`: list of rate values

**Returns**:

generator of accumulated function instance count

<a id="slambuc.alg.util.ipar_mul_factor"></a>

#### ipar\_mul\_factor

```python
def ipar_mul_factor(rate: list[int], N: int = 1) -> Generator[int]
```

Generator over the **pessimistic** number of function instances inside a block assuming parallelized execution model.

**Arguments**:

- `rate`: list of rate values
- `N`: CPU count

**Returns**:

generator of accumulated function instance count

<a id="slambuc.alg.util.igen_mul_factor"></a>

#### igen\_mul\_factor

```python
def igen_mul_factor(rate: list[int], ncores: list[int]) -> Generator[int]
```

Generator over the **pessimistic** number of function instances using separate relative CPU cores.

**Arguments**:

- `rate`: list of rate values
- `ncores`: list of CPU cores

<a id="slambuc.alg.util.leaf_label_nodes"></a>

#### leaf\_label\_nodes

```python
def leaf_label_nodes(tree: nx.DiGraph) -> nx.DiGraph
```

Label each node *n* with the set of leafs that can be reached from *n*.

**Arguments**:

- `tree`: input tree

**Returns**:

labeled tree

<a id="slambuc.alg.util.ith_child"></a>

#### ith\_child

```python
def ith_child(tree: nx.DiGraph, v: int, i: int) -> int
```

Returns the *i*-th child of the node *v* started to count from 1.

E.g.:
>>> v_i = ith_child(tree, v, i) # [v] -i-> [v_i]

**Arguments**:

- `tree`: input tree
- `v`: node ID
- `i`: number of given child

**Returns**:

i-th node

<a id="slambuc.alg.util.child_idx"></a>

#### child\_idx

```python
def child_idx(tree: nx.DiGraph, v: int) -> int
```

Returns the index of *v* among its sibling nodes or return 0.

E.g.:
>>> j = child_idx(tree, v) # [u] -j-> [v]

**Arguments**:

- `tree`: input tree
- `v`: node ID

**Returns**:

index of node *v*

<a id="slambuc.alg.util.top_subtree_block"></a>

#### top\_subtree\_block

```python
def top_subtree_block(tree: nx.DiGraph, barr: T_BARRS) -> nx.DiGraph
```

Return the first/top subtree of the given *tree* separated by the given *barr* nodes.

**Arguments**:

- `tree`: input tree
- `barr`: set of barrier nodes

**Returns**:

top subtree

<a id="slambuc.alg.util.path_blocks"></a>

#### path\_blocks

```python
def path_blocks(partition: T_PART, path: list[int]) -> T_PART
```

Calculate the blocks of separated critical path based on the original partitioning.

**Arguments**:

- `partition`: given tree partitioning
- `path`: path of specific nodes

**Returns**:

calculated path blocks

<a id="slambuc.alg.util.recreate_subchain_blocks"></a>

#### recreate\_subchain\_blocks

```python
def recreate_subchain_blocks(tree: nx.DiGraph, barr: T_BARRS) -> T_PART
```

Recreate chain blocks from barrier nodes of the given partitioning.

**Arguments**:

- `tree`: input tree
- `barr`: set of barrier nodes

**Returns**:

list of chain blocks

<a id="slambuc.alg.util.recreate_subtree_blocks"></a>

#### recreate\_subtree\_blocks

```python
def recreate_subtree_blocks(tree: nx.DiGraph, barr: T_BARRS) -> T_PART
```

Return the partition blocks of the given *tree* cut by the *barr* nodes.

**Arguments**:

- `tree`: input tree
- `barr`: set of barrier nodes

**Returns**:

list of partition blocks

<a id="slambuc.alg.util.split_chain"></a>

#### split\_chain

```python
def split_chain(barr: T_BARRS, n: int, full: bool = True) -> T_PART
```

Recreate partition blocks from barrier nodes for an *n*-size chain := [0, n-1].

**Arguments**:

- `barr`: set of barrier nodes
- `n`: chain size
- `full`: recreate all block nodes instead of just fist/last nodes

**Returns**:

created partitioning

<a id="slambuc.alg.util.split_path"></a>

#### split\_path

```python
def split_path(path: list[int], barr: T_BARRS) -> T_PART
```

Recreate partition blocks of a chain from barrier nodes for an *n*-size chain := [0, n-1].

**Arguments**:

- `path`: list of nodes
- `barr`: set of barrier nodes

**Returns**:

created partitioning

<a id="slambuc.alg.util.x_eval"></a>

#### x\_eval

```python
def x_eval(x: int | None | lp.LpVariable) -> bool
```

Evaluate *x* from a decision variable matrix based on its solution value.

**Arguments**:

- `x`: decision variable

**Returns**:

whether it is a solution or not

<a id="slambuc.alg.util.recalculate_ser_partitioning"></a>

#### recalculate\_ser\_partitioning

```python
def recalculate_ser_partitioning(tree: nx.DiGraph,
                                 partition: T_PART,
                                 root: int = 1,
                                 cp_end: int = None,
                                 delay: int = 1) -> tuple[int, int]
```

Calculate the sum cost and sum latency on the critical path based on the given *partition* assuming serialized

execution model.

**Arguments**:

- `tree`: input tree
- `partition`: given partitioning
- `root`: root node
- `cp_end`: end node of critical path
- `delay`: platform invocation delay

**Returns**:

sum cost nad latency of the given partitioning

<a id="slambuc.alg.util.recalculate_partitioning"></a>

#### recalculate\_partitioning

```python
def recalculate_partitioning(tree: nx.DiGraph,
                             partition: T_PART,
                             root: int = 1,
                             N: int = 1,
                             cp_end: int = None,
                             delay: int = 1) -> tuple[int, int]
```

Calculate sum cost and sum latency on the critical path based on the given *partition* assuming parallelized

execution model.

**Arguments**:

- `tree`: input tree
- `partition`: given partitioning
- `root`: root node
- `N`: CPU count
- `cp_end`: end node of critical path
- `delay`: platform invocation delay

**Returns**:

sum cost nad latency of the given partitioning

<a id="slambuc.alg.util.block_memory"></a>

#### block\_memory

```python
def block_memory(memory: list[int], b: int, w: int) -> int
```

Calculate cumulative memory of block [b, w].

**Arguments**:

- `memory`: list of memory values
- `b`: barrier node
- `w`: end node of block

**Returns**:

memory value

<a id="slambuc.alg.util.block_cpu"></a>

#### block\_cpu

```python
def block_cpu(rate: list[int], b: int, w: int) -> int
```

Calculate CPU core need of block [b, w] with multiprocessing.

**Arguments**:

- `rate`: list of rate values
- `b`: barrier node
- `w`: end node of block

**Returns**:

CPU count

<a id="slambuc.alg.util.block_cost"></a>

#### block\_cost

```python
def block_cost(runtime: list[int],
               rate: list[int],
               b: int,
               w: int,
               unit: int = 100) -> int
```

Calculate running time of block [b, w] with multiprocessing.

**Arguments**:

- `runtime`: list of runtime values
- `rate`: list of rate values
- `b`: barrier node
- `w`: end node of block
- `unit`: rounding unit

**Returns**:

calculated cost

<a id="slambuc.alg.util.block_latency"></a>

#### block\_latency

```python
def block_latency(runtime: list[int], b: int, w: int, delay: int, start: int,
                  end: int) -> int
```

Calculate relevant latency for block [b, w] with multiprocessing.

**Arguments**:

- `runtime`: list of runtime values
- `b`: barrier node
- `w`: end node of block
- `delay`: platform delay
- `start`: fist node to consider
- `end`: last node to consider

**Returns**:

calculated latency value

<a id="slambuc.alg.util.ser_block_memory"></a>

#### ser\_block\_memory

```python
def ser_block_memory(memory: list[int]) -> int
```

Calculate cumulative memory of block [b, w] with serialization.

**Arguments**:

- `memory`: list of memory values

**Returns**:

memory value

<a id="slambuc.alg.util.ser_block_memory_opt"></a>

#### ser\_block\_memory\_opt

```python
def ser_block_memory_opt(memory: list[int], rate: list[int], b: int,
                         w: int) -> int
```

Calculate memory of block [b, w] recursively based on the **optimistic** number of parallel function instances.

**Arguments**:

- `memory`: list of memory values
- `rate`: list of rate values
- `b`: barrier node
- `w`: end node of block

**Returns**:

calculated memory value

<a id="slambuc.alg.util.ser_block_memory_pes"></a>

#### ser\_block\_memory\_pes

```python
def ser_block_memory_pes(memory: list[int], rate: list[int], b: int,
                         w: int) -> int
```

Calculate memory of block [b, w] recursively based on the **pessimistic** number of parallel function instances.

**Arguments**:

- `memory`: list of memory values
- `rate`: list of rate values
- `b`: barrier node
- `w`: end node of block

**Returns**:

calculated memory value

<a id="slambuc.alg.util.ser_block_memory_pes2"></a>

#### ser\_block\_memory\_pes2

```python
def ser_block_memory_pes2(memory: list[int], rate: list[int], b: int,
                          w: int) -> int
```

Calculate memory of block [b, w] directly based on the **pessimistic** number of parallel function instances.

**Arguments**:

- `memory`: list of memory values
- `rate`: list of rate values
- `b`: barrier node
- `w`: end node of block

**Returns**:

calculated memory value

<a id="slambuc.alg.util.ser_block_cost"></a>

#### ser\_block\_cost

```python
def ser_block_cost(runtime: list[int], rate: list[int],
                   data: list[int]) -> int
```

Calculate running time of a subtree block with serialization.

**Arguments**:

- `runtime`: list of runtime values
- `rate`: list of rate values
- `data`: list of data values

**Returns**:

calculated cost

<a id="slambuc.alg.util.ser_block_latency"></a>

#### ser\_block\_latency

```python
def ser_block_latency(runtime: list[int], rate: list[int],
                      data: list[int]) -> int
```

Calculate relevant latency of a subtree block with serialization.

**Arguments**:

- `runtime`: list of runtime values
- `rate`: list of rate values
- `data`: list of data values

**Returns**:

calculated latency

<a id="slambuc.alg.util.ser_block_submemory"></a>

#### ser\_block\_submemory

```python
def ser_block_submemory(memory: list[int], b: int, w: int) -> int
```

Calculate cumulative memory of **chain block** [b, w] with serialization and data fetching/caching.

**Arguments**:

- `memory`: list of memory values
- `b`: barrier node
- `w`: end node of block

**Returns**:

calculated memory value

<a id="slambuc.alg.util.ser_block_subcost"></a>

#### ser\_block\_subcost

```python
def ser_block_subcost(runtime: list[int], rate: list[int], data: list[int],
                      b: int, w: int) -> int
```

Calculate running time of a **chain block** [b, w] with serialization and data fetching/caching.

**Arguments**:

- `runtime`: list of runtime values
- `rate`: list of rate values
- `data`: list of data values
- `b`: barrier node
- `w`: end node of block

**Returns**:

calculated cost

<a id="slambuc.alg.util.ser_block_sublatency"></a>

#### ser\_block\_sublatency

```python
def ser_block_sublatency(runtime: list[int], rate: list[int], data: list[int],
                         b: int, w: int, delay: int, start: int,
                         end: int) -> int
```

Calculate relevant latency for **chain block** [b,w] with serialization and data fetching/caching.

**Arguments**:

- `runtime`: list of runtime values
- `rate`: list of rate values
- `data`: list of data values
- `b`: barrier node
- `w`: end node of block
- `delay`: platform delay
- `start`: fist node to consider
- `end`: last node to consider

**Returns**:

calculated latency

<a id="slambuc.alg.util.ser_subtree_memory"></a>

#### ser\_subtree\_memory

```python
def ser_subtree_memory(tree: nx.DiGraph, nodes: set[int]) -> int
```

Calculate cumulative memory of a subtree.

**Arguments**:

- `tree`: input tree
- `nodes`: set of block nodes

**Returns**:

calculated memory

<a id="slambuc.alg.util.ser_subtree_cost"></a>

#### ser\_subtree\_cost

```python
def ser_subtree_cost(tree: nx.DiGraph, barr: int, nodes: set[int]) -> int
```

Calculate running time of a **subtree** with serialization and data fetching/caching.

**Arguments**:

- `tree`: input tree
- `barr`: barrier node
- `nodes`: set of block nodes

**Returns**:

calculated cost

<a id="slambuc.alg.util.ser_pes_subchain_latency"></a>

#### ser\_pes\_subchain\_latency

```python
def ser_pes_subchain_latency(tree: nx.DiGraph, barr: int, nodes: set[int],
                             cpath: set[int]) -> int
```

Calculate relevant latency of **chain** in group of **nodes** with serialization and **pessimistic** caching.

**Arguments**:

- `tree`: input tree
- `barr`: barrier node
- `nodes`: set of block nodes
- `cpath`: critical path nodes

**Returns**:

calculated latency

<a id="slambuc.alg.util.ser_subchain_latency"></a>

#### ser\_subchain\_latency

```python
def ser_subchain_latency(tree: nx.DiGraph, barr: int, nodes: set[int],
                         cpath: set[int]) -> int
```

Calculate relevant latency of **chain** in group of **nodes** with serialization and data fetching/caching.

**Arguments**:

- `tree`: input tree
- `barr`: barrier node
- `nodes`: set of block nodes
- `cpath`: critical path nodes

**Returns**:

calculated latency

<a id="slambuc.alg.util.par_inst_count"></a>

#### par\_inst\_count

```python
def par_inst_count(r_barr: int, r_v: int, N: int = 1) -> int
```

Calculate instance number of a function considering the function/barrier rates and CPU count *N*.

**Arguments**:

- `r_barr`: barrier node's ingress rate
- `r_v`: call rate of node v
- `N`: CPU count

**Returns**:

calculated instance count of node v

<a id="slambuc.alg.util.par_subtree_memory"></a>

#### par\_subtree\_memory

```python
def par_subtree_memory(tree: nx.DiGraph,
                       barr: int,
                       nodes: list[int] | set[int],
                       N: int = 1) -> int
```

Calculate memory demand of a subtree as the sum of cumulative and parallel execution components.

**Arguments**:

- `tree`: input tree
- `barr`: barrier node
- `nodes`: set of block nodes
- `N`: CPU count

**Returns**:

calculated memory value

<a id="slambuc.alg.util.par_subtree_cost"></a>

#### par\_subtree\_cost

```python
def par_subtree_cost(tree: nx.DiGraph,
                     barr: int,
                     nodes: set[int],
                     N: int = 1) -> int
```

Calculate running time of a **subtree** with multiprocessing and data fetching/caching.

**Arguments**:

- `tree`: input tree
- `barr`: barrier node
- `nodes`: set of block nodes
- `N`: CPU count

**Returns**:

calculated cost

<a id="slambuc.alg.util.par_subchain_latency"></a>

#### par\_subchain\_latency

```python
def par_subchain_latency(tree: nx.DiGraph,
                         barr: int,
                         nodes: set[int],
                         cpath: set[int],
                         N: int = 1) -> int
```

Calculate relevant latency of **chain** in group of **nodes** with serialization and data fetching/caching.

**Arguments**:

- `tree`: input tree
- `barr`: barrier node
- `nodes`: set of block nodes
- `cpath`: critical path nodes
- `N`: CPU count

**Returns**:

calculated latency

<a id="slambuc.alg.util.gen_subtree_memory"></a>

#### gen\_subtree\_memory

```python
def gen_subtree_memory(tree: nx.DiGraph,
                       barr: int,
                       nodes: set[int],
                       N: int = 1) -> int
```

Calculate memory demand of a subtree as the sum of cumulative and parallel execution components.

**Arguments**:

- `tree`: input tree
- `barr`: barrier node
- `nodes`: set of block nodes
- `N`: CPU count

**Returns**:

calculated memory value

<a id="slambuc.alg.util.gen_subtree_cost"></a>

#### gen\_subtree\_cost

```python
def gen_subtree_cost(
    tree: nx.DiGraph,
    barr: int,
    nodes: set[int],
    N: int = 1,
    exec_calc: collections.abc.Callable[[int, int, int],
                                        int] = lambda i, t, n: t
) -> int
```

Calculate running time of a **subtree** with multiprocessing and data fetching/caching while using *exec_calc*

callable to recalculate function execution time based on the function's id (i), reference runtime (t) and available
CPU cores (n).

**Arguments**:

- `tree`: input tree
- `barr`: barrier node
- `nodes`: set of block nodes
- `N`: CPU count
- `exec_calc`: calculator function

**Returns**:

calculated cost

<a id="slambuc.alg.util.gen_subchain_latency"></a>

#### gen\_subchain\_latency

```python
def gen_subchain_latency(
    tree: nx.DiGraph,
    barr: int,
    nodes: set[int],
    cpath: set[int],
    N: int = 1,
    exec_calc: collections.abc.Callable[[int, int, int],
                                        int] = lambda i, t, n: t
) -> int
```

Calculate relevant latency of **chain** in group of **nodes** with serialization and data fetching/caching while

using *exec_calc* callable to recalculate function execution time based on the function's id (i), reference runtime
(t) and available CPU cores (n).

**Arguments**:

- `tree`: input tree
- `barr`: barrier node
- `nodes`: set of block nodes
- `cpath`: critical path nodes
- `N`: CPU count
- `exec_calc`: calculator function

**Returns**:

calculated latency

<a id="slambuc.gen.cluster.job_tree"></a>

# slambuc.gen.cluster.job\_tree

<a id="slambuc.gen.cluster.job_tree.convert_tasks_to_dag"></a>

#### convert\_tasks\_to\_dag

```python
def convert_tasks_to_dag(job_name: str,
                         tasks: pd.DataFrame,
                         mem_max: int = DEF_MEM_MAX,
                         data_mean: int = None) -> tuple[nx.DiGraph, int]
```

Convert the task lines of given job *job_name* into a DAG and return it with the generated front-end root node.

**Arguments**:

- `job_name`: job name in the dataset
- `tasks`: tasks imported from the dataset
- `mem_max`: maximum memory to convert memory usage into MB
- `data_mean`: dataset overhead mean value for generating artificial values

**Returns**:

generated DAG and dispatcher node

<a id="slambuc.gen.cluster.job_tree.igenerate_job_tree"></a>

#### igenerate\_job\_tree

```python
def igenerate_job_tree(job_df: pd.DataFrame,
                       min_size: int = 0) -> Generator[nx.DiGraph]
```

Generate job service trees one-by-one from *min_size*.

**Arguments**:

- `job_df`: imported job dataset
- `min_size`: minimum tree size

**Returns**:

generator of job DAGs

<a id="slambuc.gen.cluster.job_tree.igenerate_syn_tree"></a>

#### igenerate\_syn\_tree

```python
def igenerate_syn_tree(n: int | tuple[int, int],
                       iteration: int = 1,
                       job_lb: int = 10) -> Generator[nx.DiGraph]
```

Generate random job service trees based on empirical distributions.

**Arguments**:

- `n`: tree size interval
- `iteration`: number of trees
- `job_lb`: minimum tree size

**Returns**:

generator of tree DAGs

<a id="slambuc.gen.cluster.job_tree.generate_all_job_trees"></a>

#### generate\_all\_job\_trees

```python
def generate_all_job_trees(data_dir: str,
                           task_file: str = DEF_TASK_CSV,
                           start: int = 10,
                           end: int = None,
                           step: int = 10,
                           tree_name: str = DEF_JOB_TREE_PREFIX)
```

Generate all job service trees with size interval between *start* and *end* and save them into separate files.

**Arguments**:

- `data_dir`: data directory
- `task_file`: task file name
- `start`: lower bound of size intervals
- `end`: upper bound of size intervals
- `step`: step size of intervals
- `tree_name`: prefix name of tree files

<a id="slambuc.gen.cluster.job_tree.generate_syn_job_trees"></a>

#### generate\_syn\_job\_trees

```python
def generate_syn_job_trees(data_dir: str,
                           iteration: int = 100,
                           start: int = 10,
                           end: int = 100,
                           step: int = 10,
                           tree_name: str = DEF_JOB_TREE_PREFIX)
```

Generate synthetic job service trees with size interval between *start* and *end* and save to separate files

using extracted empirical distributions.

**Arguments**:

- `data_dir`: data directory
- `iteration`: number of generated trees
- `start`: lower bound of size intervals
- `end`: upper bound of size intervals
- `step`: step size of intervals
- `tree_name`: prefix name of tree files

<a id="slambuc.gen.cluster.job_tree.generate_mixed_job_trees"></a>

#### generate\_mixed\_job\_trees

```python
def generate_mixed_job_trees(data_dir: str,
                             task_file: str = DEF_TASK_CSV,
                             iteration: int = 100,
                             start: int = 10,
                             end: int = 100,
                             step: int = 10,
                             tree_name: str = DEF_JOB_TREE_PREFIX)
```

Generate job trees from sample data and extend it with synthetic trees if necessary.

**Arguments**:

- `data_dir`: data directory
- `task_file`: task file name
- `iteration`: number of generated trees
- `start`: minimum of size intervals
- `end`: maximum of size intervals
- `step`: step size of intervals
- `tree_name`: prefix name of tree files

<a id="slambuc.gen.cluster"></a>

# slambuc.gen.cluster

<a id="slambuc.gen.cluster.syn_job"></a>

# slambuc.gen.cluster.syn\_job

<a id="slambuc.gen.cluster.syn_job.draw"></a>

#### draw

```python
def draw(hist_name: str,
         num: int = 1,
         path: list = tuple(),
         ndigits: int = 2,
         positive: bool = True,
         output_integer: bool = False,
         seed: int = None) -> list[int | float]
```

Draw random samples from a given distribution.

Random job generation source code is moved from package *spar* with adaptations to newer versions of Python3.11
and Scipy 1.10.  See also: https://github.com/All-less/trace-generator/blob/master/spar/generate.py

<a id="slambuc.gen.microservice.power_ba_graph"></a>

# slambuc.gen.microservice.power\_ba\_graph

<a id="slambuc.gen.microservice.power_ba_graph.wrand_sample"></a>

#### wrand\_sample

```python
def wrand_sample(population: list[int | float],
                 weights: list[int],
                 k: int = 1) -> list[int | float]
```

Provide an *k*-size weighted random sample from *population* without replacement according to the given *weights*.

See more: https://stackoverflow.com/questions/43549515/weighted-random-sample-without-replacement-in-python

**Arguments**:

- `population`: list of items
- `weights`: list of item weights
- `k`: sample size (default: 1)

**Returns**:

sample list

<a id="slambuc.gen.microservice.power_ba_graph.generate_power_ba_graph"></a>

#### generate\_power\_ba\_graph

```python
def generate_power_ba_graph(n: int,
                            m: int,
                            Alpha: float = 1.0,
                            a: float = 0.0,
                            root: int = 0,
                            create_using: nx.Graph = None) -> nx.Graph
```

Generate Barabasi-Albert (BA) graph where the probability of choosing a vertex *v* for connecting to another node

follows a Power law distribution as *P(v) = deg(v)^Alpha + a*.

Thus, choosing *Alpha = 1.0* and *a = 0.0* falls back to standard BA graph generation.

Choosing *m = 1* ensures the output to be a tree by default.

See also: https://networkx.org/documentation/stable/_modules/networkx/generators/random_graphs.html#barabasi_albert_graph
and the related paper: https://dl.acm.org/doi/abs/10.5555/3432601.3432616.

**Arguments**:

- `n`: number of nodes
- `m`: number of existing nodes (or new edges) attached to the new node in each step
- `Alpha`: power of preferential attachment (default: 1.0)
- `a`: attractiveness of vertices with no edges (default: 0.0)
- `root`: initial node ID that is increased in each attachment step (default: 0)
- `create_using`: graph type to construct (default: undirected, use `nx.DiGraph` to get a directed graph)

**Returns**:

created graph

<a id="slambuc.gen.microservice.power_ba_graph.generate_power_ba_tree"></a>

#### generate\_power\_ba\_tree

Generate power BA trees using m=1.

<a id="slambuc.gen.microservice.faas_tree"></a>

# slambuc.gen.microservice.faas\_tree

<a id="slambuc.gen.microservice.faas_tree.ifunc_attributes"></a>

#### ifunc\_attributes

```python
def ifunc_attributes(n: int,
                     dist: scipy.stats.rv_continuous,
                     transform=np.round) -> Generator[int]
```

Generate attribute values of the given size *n* base on the given distribution *dist*.

**Arguments**:

- `n`: number of attributes
- `dist`: build distribution object
- `transform`: transform function applied on every attribute value

**Returns**:

generator of attributes

<a id="slambuc.gen.microservice.faas_tree.get_faas_tree"></a>

#### get\_faas\_tree

```python
def get_faas_tree(n: int, Alpha: float, a: float) -> nx.DiGraph
```

Generate service tree with attributes drawn from the predefined distributions.

**Arguments**:

- `n`: number of nodes
- `Alpha`: power of preferential attachment (default: 1.0)
- `a`: attractiveness of vertices with no edges (default: 0.0)

**Returns**:

generated tree

<a id="slambuc.gen.microservice.faas_tree.verify_faas_tree"></a>

#### verify\_faas\_tree

```python
def verify_faas_tree(n: int = 10)
```

Plot random generated serverless tree.

**Arguments**:

- `n`: tree size

<a id="slambuc.gen.microservice.faas_tree.generate_all_faas_trees"></a>

#### generate\_all\_faas\_trees

```python
def generate_all_faas_trees(data_dir: str,
                            Alpha: float = PREF_ATT_HIGH,
                            a: float = LEAF_ATTR_HIGH,
                            iteration: int = 100,
                            start: int = 10,
                            end: int = 100,
                            step: int = 10,
                            tree_name: str = DEF_FAAS_TREE_PREFIX)
```

Generate Serverless/Faas service trees with attributes from predefined and extracted distributions.

**Arguments**:

- `data_dir`: directory of saved trees
- `Alpha`: power of preferential attachment (default: 1.0)
- `a`: attractiveness of vertices with no edges (default: 0.0)
- `iteration`: number of generated trees
- `start`: minimum of size intervals
- `end`: maximum of size intervals
- `step`: step size of intervals
- `tree_name`: prefix name of tree files

<a id="slambuc.gen.microservice"></a>

# slambuc.gen.microservice

<a id="slambuc.gen.io"></a>

# slambuc.gen.io

<a id="slambuc.gen.io.encode_service_tree"></a>

#### encode\_service\_tree

```python
def encode_service_tree(tree: nx.DiGraph,
                        root: int = 0,
                        pad_size: int = 0) -> np.ndarray[np.int64]
```

Encode the given service *tree* into an array with size of **5*n** where n is the size of the tree.

The tree must have the tree structure where the root is PLATFORM and the node IDs are increasing integers from *1*
to *n*. The array's structure is *[r, S_(n-1), R_n, D_n, T_n, M_n]*, where
    - *r* is the root node of the tree (default is PLATFORM that is converted to node *0*),
    - *S_(n-1) is the Prufer sequence of the tree extended with root node PLATFORM,
    - *D_n, R_n* are the ingress edge attributes (DATA, RATE) and
    - *T_n, M_n* are the node attributes (RUNTIME, MEMORY) of the tree nodes in increasing order from *1* to *n*.

**Arguments**:

- `tree`: service tree
- `root`: root node
- `pad_size`: padding size for uniform length

**Returns**:

encoded tree as value arrays

<a id="slambuc.gen.io.decode_service_tree"></a>

#### decode\_service\_tree

```python
def decode_service_tree(tdata: np.ndarray[np.int64]) -> nx.DiGraph
```

Decode and rebuild service tree from value arrays.

Inverse method of :func:`encode_service_tree`.

**Arguments**:

- `tdata`: array values

**Returns**:

service tree

<a id="slambuc.gen.io.save_trees_to_file"></a>

#### save\_trees\_to\_file

```python
def save_trees_to_file(trees: list[nx.DiGraph],
                       file_name: str = "test_trees.npy",
                       padding: int = 0)
```

Convert trees into a compact format and save them in a single file.

**Arguments**:

- `trees`: list of trees
- `file_name`: output file name
- `padding`: padding size

<a id="slambuc.gen.io.get_tree_from_file"></a>

#### get\_tree\_from\_file

```python
def get_tree_from_file(file_name: str, tree_num: int) -> nx.DiGraph
```

Load and decode a service tree from the given *file_name* with specific ID *tree_num*.

**Arguments**:

- `file_name`: file name
- `tree_num`: tree ID

**Returns**:

loaded tree

<a id="slambuc.gen.io.iload_trees_from_file"></a>

#### iload\_trees\_from\_file

```python
def iload_trees_from_file(file_name: str) -> Generator[nx.DiGraph]
```

Generator of service trees loaded from given *file_name*.

**Arguments**:

- `file_name`: tree file

**Returns**:

generator of trees

<a id="slambuc.gen.io.load_hist_params"></a>

#### load\_hist\_params

```python
def load_hist_params(
        hist_dir: str | pathlib.Path,
        hist_name: str) -> tuple[list[int | float], list[int | float]]
```

Load pickled attributes from given file.

**Arguments**:

- `hist_dir`: directory of histogram attributes
- `hist_name`: name of the histogram

**Returns**:

loaded histogram attributes

<a id="slambuc.gen"></a>

# slambuc.gen

<a id="slambuc.gen.transform"></a>

# slambuc.gen.transform

<a id="slambuc.gen.transform.faasify_dag_by_duplication"></a>

#### faasify\_dag\_by\_duplication

```python
def faasify_dag_by_duplication(dag: nx.DiGraph, root: int) -> nx.DiGraph
```

One-way transformation of a DAG of modules/components into a tree by iteratively duplicating sub-graphs

related to nodes with multiple predecessors.

The algorithm requires that the input DAG must have only one source node.

**Arguments**:

- `dag`: input DAG
- `root`: root node

**Returns**:

generated tree

<a id="slambuc.gen.transform.transform_autonomous_caching"></a>

#### transform\_autonomous\_caching

```python
def transform_autonomous_caching(tree: nx.DiGraph,
                                 root: int,
                                 copy: bool = False) -> nx.DiGraph
```

Transform given *tree* by adding fetching and out-caching overheads to function execution times.

**Arguments**:

- `tree`: input tree
- `root`: root node
- `copy`: use a deep copy of the input instead of modifying the original

**Returns**:

transformed tree

<a id="slambuc.gen.random.random_tree"></a>

# slambuc.gen.random.random\_tree

<a id="slambuc.gen.random.random_tree.RUNTIME"></a>

#### RUNTIME

Overall running time in ms

<a id="slambuc.gen.random.random_tree.MEMORY"></a>

#### MEMORY

Peak memory demand in MB

<a id="slambuc.gen.random.random_tree.DATA"></a>

#### DATA

Read/write overhead in ms

<a id="slambuc.gen.random.random_tree.RATE"></a>

#### RATE

Invocations rate in 1/s

<a id="slambuc.gen.random.random_tree.generate_random_trees"></a>

#### generate\_random\_trees

```python
def generate_random_trees(n: int,
                          data_dir: str,
                          iteration: int = 1000,
                          file_prefix: str = DEF_RAND_TREE_PREFIX)
```

Generate random trees with attributes uniformly drawn form intervals.

**Arguments**:

- `n`: tree size
- `data_dir`: directory of saved trees
- `iteration`: number of generated trees
- `file_prefix`: prefix name of tree files

<a id="slambuc.gen.random.random_tree.generate_all_random_trees"></a>

#### generate\_all\_random\_trees

```python
def generate_all_random_trees(data_dir: str,
                              iteration: int = 100,
                              start: int = 10,
                              end: int = 100,
                              step: int = 10,
                              file_prefix: str = DEF_RAND_TREE_PREFIX)
```

Generate random service trees with random sizes from given intervals.

**Arguments**:

- `data_dir`: directory of saved trees
- `iteration`: number of generated trees
- `start`: minimum of size intervals
- `end`: maximum of size intervals
- `step`: step size of intervals
- `file_prefix`: prefix name of tree files

<a id="slambuc.gen.random"></a>

# slambuc.gen.random

<a id="slambuc.misc.generator"></a>

# slambuc.misc.generator

<a id="slambuc.misc.generator.get_random_chain_data"></a>

#### get\_random\_chain\_data

```python
def get_random_chain_data(
    nodes: int = 10,
    runtime: tuple[int, int] = (1, 100),
    memory: tuple[int, int] = (1, 3),
    rate: tuple[int, int] = (1, 3),
    data: tuple[int, int] = (1, 20)
) -> list[list[int]]
```

Generate random chain(path graph) data with properties from given intervals.

**Arguments**:

- `nodes`: number of nodes
- `runtime`: interval of runtime values
- `memory`: interval of memory values
- `rate`: interval of rate values
- `data`: interval of data values

**Returns**:

generated chain data

<a id="slambuc.misc.generator.get_random_chain"></a>

#### get\_random\_chain

```python
def get_random_chain(
    nodes: int = 10,
    runtime: tuple[int, int] = (1, 100),
    memory: tuple[int, int] = (1, 3),
    rate: tuple[int, int] = (1, 3),
    data: tuple[int, int] = (1, 20)
) -> nx.DiGraph
```

Generate random chain(path graph) with properties from given intervals.

**Arguments**:

- `nodes`: number of nodes
- `runtime`: interval of runtime values
- `memory`: interval of memory values
- `rate`: interval of rate values
- `data`: interval of data values

**Returns**:

generated random chain

<a id="slambuc.misc.generator.get_random_tree"></a>

#### get\_random\_tree

```python
def get_random_tree(nodes: int = 20,
                    runtime: tuple[int, int] = (1, 100),
                    memory: tuple[int, int] = (1, 3),
                    rate: tuple[int, int] = (1, 3),
                    data: tuple[int, int] = (1, 20),
                    name: str = None) -> nx.DiGraph
```

Generate random tree from Prufer sequence with properties from given intervals.

**Arguments**:

- `nodes`: number of nodes
- `runtime`: interval of runtime values
- `memory`: interval of memory values
- `rate`: interval of rate values
- `data`: interval of data values
- `name`: tree name suffix

**Returns**:

generated random tree

<a id="slambuc.misc.plot"></a>

# slambuc.misc.plot

<a id="slambuc.misc.plot.draw_tree"></a>

#### draw\_tree

```python
def draw_tree(tree: nx.DiGraph,
              partition: list = None,
              cuts: list = None,
              draw_weights=False,
              draw_blocks=False,
              figsize=None,
              ax=None,
              **kwargs)
```

Draw tree with given partitioning in a top-down topological structure.

**Arguments**:

- `tree`: service tree
- `partition`: calculated partitioning (optional)
- `cuts`: calculated cuts (optional)
- `draw_weights`: draw node/edge weights instead of IDs
- `draw_blocks`: draw surrounding blocks
- `figsize`: figure dimensions (optional)
- `ax`: matplotlib axis (optional)

<a id="slambuc.misc.plot.draw_state_dag"></a>

#### draw\_state\_dag

```python
def draw_state_dag(dag: nx.DiGraph,
                   chains: list[list[int]],
                   draw_weights: bool = False)
```

Draw state-space DAG in a vertically-ordered multipartite layout.

**Arguments**:

- `dag`: input DAG
- `chains`: chain decomposition of the given tree
- `draw_weights`: draw node/edge weights instead of IDs

<a id="slambuc.misc"></a>

# slambuc.misc

<a id="slambuc.misc.util"></a>

# slambuc.misc.util

<a id="slambuc.misc.util.get_cplex_path"></a>

#### get\_cplex\_path

```python
def get_cplex_path() -> str
```

Return local CPLEX path.

**Returns**:

path

<a id="slambuc.misc.util.get_cpo_path"></a>

#### get\_cpo\_path

```python
def get_cpo_path() -> str
```

Return local CPO path.

**Returns**:

path

<a id="slambuc.misc.util.is_compatible"></a>

#### is\_compatible

```python
def is_compatible(tree1: nx.DiGraph, tree2: nx.DiGraph) -> bool
```

Return true if given second *tree2* has the same structure and edge/node attributes as the first *tree1*.

**Arguments**:

- `tree1`: first tree
- `tree2`: second tree

**Returns**:

similarity result

<a id="slambuc.misc.util.get_chain_k_min"></a>

#### get\_chain\_k\_min

```python
def get_chain_k_min(memory: list[int],
                    M: int,
                    rate: list[int],
                    N: int,
                    start: int = 0,
                    end: int = None) -> int
```

Return minimal number of blocks due to constraints *M* and *N*.

**Arguments**:

- `memory`: list of memory values
- `M`: memory upper bound
- `rate`: list of rate values
- `N`: CPU count
- `start`: fist node to consider
- `end`: last node to consider

**Returns**:

minimal number of blocks

<a id="slambuc.misc.util.get_chain_c_min"></a>

#### get\_chain\_c\_min

```python
def get_chain_c_min(memory: list[int],
                    M: int,
                    rate: list[int],
                    N: int,
                    start: int = 0,
                    end: int = None) -> int
```

Return minimal number of cuts due to constraints *M* and *N*.

**Arguments**:

- `memory`: list of memory values
- `M`: memory upper bound
- `rate`: list of rate values
- `N`: CPU count
- `start`: fist node to consider
- `end`: last node to consider

**Returns**:

minimal number of cuts

<a id="slambuc.misc.util.get_chain_c_max"></a>

#### get\_chain\_c\_max

```python
def get_chain_c_max(runtime: list[int],
                    L: int,
                    b: int,
                    w: int,
                    delay: int,
                    start: int = 0,
                    end: int = None) -> int
```

Return maximal number of cuts due to constraint *L*.

**Arguments**:

- `runtime`: list of runtime values
- `L`: upper latency limit
- `b`: barrier node
- `w`: end node of chain block
- `delay`: platform delay
- `start`: fist node to consider
- `end`: last node to consider

**Returns**:

maximum number of cuts

<a id="slambuc.misc.util.get_chain_k_max"></a>

#### get\_chain\_k\_max

```python
def get_chain_k_max(runtime: list[int],
                    L: int,
                    b: int,
                    w: int,
                    delay: int,
                    start: int = 0,
                    end: int = None) -> int
```

Return maximal number of blocks due to constraint *L*.

**Arguments**:

- `runtime`: list of runtime values
- `L`: upper latency limit
- `b`: barrier node
- `w`: end node of chain block
- `delay`: platform delay
- `start`: fist node to consider
- `end`: last node to consider

**Returns**:

maximum number of blocks

<a id="slambuc.misc.util.get_chain_k_opt"></a>

#### get\_chain\_k\_opt

```python
def get_chain_k_opt(partition: T_PART, start: int = 0, end: int = None) -> int
```

Return the number of blocks included by the [*start*, *end*] interval in partitioning.

**Arguments**:

- `partition`: chain partitioning
- `start`: fist node to consider
- `end`: last node to consider

**Returns**:

number of blocks

<a id="slambuc.misc.util.get_chain_c_opt"></a>

#### get\_chain\_c\_opt

```python
def get_chain_c_opt(partition: T_PART, start: int = 0, end: int = None) -> int
```

Return the number of cuts included by the [*start*, *end*] interval in partitioning.

**Arguments**:

- `partition`: chain partitioning
- `start`: fist node to consider
- `end`: last node to consider

**Returns**:

number of cuts

<a id="slambuc.misc.util.prune_chain"></a>

#### prune\_chain

```python
def prune_chain(tree: nx.DiGraph, node: int,
                leaf: int) -> tuple[list[int], list[int]]
```

Return the nodes of chain [*node*, *leaf*] and the branching nodes.

**Arguments**:

- `tree`: service tree
- `node`: chain's barrier node
- `leaf`: end node of chain

**Returns**:

nodes of the chain and its branches

<a id="slambuc.misc.util.print_chain_summary"></a>

#### print\_chain\_summary

```python
def print_chain_summary(runtime: list[int], memory: list[int],
                        rate: list[int])
```

Print chain summary.

**Arguments**:

- `runtime`: list of runtime values
- `memory`: list of memory values
- `rate`: list of rate values

<a id="slambuc.misc.util.evaluate_chain_partitioning"></a>

#### evaluate\_chain\_partitioning

```python
def evaluate_chain_partitioning(partition: T_PART,
                                opt_cost: int,
                                opt_lat: int,
                                runtime: list,
                                memory: list,
                                rate: list,
                                M: int = math.inf,
                                N: int = math.inf,
                                L: int = math.inf,
                                start: int = 0,
                                end: int = None,
                                delay: int = 1,
                                unit: int = 100)
```

Evaluate chain partitioning and print its characteristics.

**Arguments**:

- `partition`: chain partitioning
- `opt_cost`: optimal cost of the partitioning
- `opt_lat`: latency of the partitioning
- `runtime`: list of runtime values
- `memory`: list of memory values
- `rate`: list of rate values
- `M`: memory upper bound
- `N`: CPU count
- `L`: upper latency limit
- `start`: fist node to consider
- `end`: last node to consider
- `delay`: platform delay
- `unit`: rounding unit

<a id="slambuc.misc.util.print_block_stat"></a>

#### print\_block\_stat

```python
def print_block_stat(partition: T_PART,
                     runtime: list[int],
                     memory: list[int],
                     rate: list[int],
                     delay: float,
                     start: int = 0,
                     end: int = None,
                     unit: int = 100)
```

Print block statistics.

**Arguments**:

- `partition`: chain partitioning
- `runtime`: list of runtime values
- `memory`: list of memory values
- `rate`: list of rate values
- `start`: fist node to consider
- `end`: last node to consider
- `delay`: platform delay
- `unit`: rounding unit

<a id="slambuc.misc.util.print_chain_partition_result"></a>

#### print\_chain\_partition\_result

```python
def print_chain_partition_result(barr: T_BARRS, cost: int, lat: int)
```

Decode and print chain partitioning result.

**Arguments**:

- `barr`: barrier nodes
- `cost`: optimal cost
- `lat`: latency values

<a id="slambuc.misc.util.print_tree_summary"></a>

#### print\_tree\_summary

```python
def print_tree_summary(tree: nx.DiGraph)
```

Print summary of service graphs.

**Arguments**:

- `tree`: input tree

<a id="slambuc.misc.util.print_tree_block_stat"></a>

#### print\_tree\_block\_stat

```python
def print_tree_block_stat(tree: nx.DiGraph,
                          partition: T_PART,
                          unit: int = 100)
```

Print cost memory and latency values of partition blocks in tabulated format.

**Arguments**:

- `tree`: input tree
- `partition`: given partitioning
- `unit`: rounding unit

<a id="slambuc.misc.util.print_cpath_stat"></a>

#### print\_cpath\_stat

```python
def print_cpath_stat(tree: nx.DiGraph,
                     partition: T_PART,
                     cpath: list[int] = None,
                     delay: int = 10)
```

Print the related block of the critical path.

**Arguments**:

- `tree`: input tree
- `partition`: given partitioning
- `cpath`: critical path
- `delay`: platform delay value

<a id="slambuc.misc.util.evaluate_tree_partitioning"></a>

#### evaluate\_tree\_partitioning

```python
def evaluate_tree_partitioning(tree: nx.DiGraph, partition: T_PART,
                               opt_cost: int, root: int, cp_end: int, M: int,
                               N: int, L: int, delay: int, unit: int)
```

Evaluate tree partitioning and print its characteristics.

**Arguments**:

- `tree`: input tree
- `partition`: given partitioning
- `opt_cost`: optimal partitioning cost
- `root`: root node
- `cp_end`: end node of critical path
- `M`: upper memory limit
- `N`: CPU count
- `L`: latency limit
- `delay`: platform invocation delay
- `unit`: rounding unit

<a id="slambuc.misc.util.print_ser_tree_block_stat"></a>

#### print\_ser\_tree\_block\_stat

```python
def print_ser_tree_block_stat(tree: nx.DiGraph, partition: T_PART,
                              cpath: list[int])
```

Print cost memory and latency values of partition blocks in tabulated format.

**Arguments**:

- `tree`: input tree
- `partition`: given partitioning
- `cpath`: critical path

<a id="slambuc.misc.util.print_ser_cpath_stat"></a>

#### print\_ser\_cpath\_stat

```python
def print_ser_cpath_stat(tree: nx.DiGraph,
                         partition: T_PART,
                         cpath: list[int] = None,
                         delay: int = 10)
```

Print the related block of the critical path.

**Arguments**:

- `tree`: input tree
- `partition`: given partitioning
- `cpath`: critical path
- `delay`: platform delay value

<a id="slambuc.misc.util.evaluate_ser_tree_partitioning"></a>

#### evaluate\_ser\_tree\_partitioning

```python
def evaluate_ser_tree_partitioning(tree: nx.DiGraph,
                                   partition: T_PART,
                                   opt_cost: int,
                                   opt_lat: int,
                                   root: int,
                                   cp_end: int,
                                   M: int,
                                   L: int,
                                   delay: int,
                                   draw: bool = True)
```

Evaluate tree partitioning and print its characteristics assuming serialized platform execution model.

**Arguments**:

- `tree`: input tree
- `partition`: given partitioning
- `opt_cost`: optimal partitioning cost
- `opt_lat`: latency value of the partitioning
- `root`: root node
- `cp_end`: end node of critical path
- `M`: upper memory limit
- `L`: latency limit
- `delay`: platform invocation delay
- `draw`: draw tree

<a id="slambuc.misc.util.print_par_tree_block_stat"></a>

#### print\_par\_tree\_block\_stat

```python
def print_par_tree_block_stat(tree: nx.DiGraph,
                              partition: T_PART,
                              cpath: list[int],
                              N: int = 1)
```

Print cost memory and latency values of partition blocks in tabulated format  assuming parallelized execution model.

**Arguments**:

- `tree`: input tree
- `partition`: given partitioning
- `cpath`: critical path
- `N`: CPU count

<a id="slambuc.misc.util.print_par_cpath_stat"></a>

#### print\_par\_cpath\_stat

```python
def print_par_cpath_stat(tree: nx.DiGraph,
                         partition: T_PART,
                         cpath: list[int] = None,
                         delay: int = 10,
                         N: int = 1)
```

Print the related block of the critical path assuming parallelized execution model.

**Arguments**:

- `tree`: input tree
- `partition`: given partitioning
- `cpath`: critical path
- `delay`: platform invocation delay
- `N`: CPU count

<a id="slambuc.misc.util.evaluate_par_tree_partitioning"></a>

#### evaluate\_par\_tree\_partitioning

```python
def evaluate_par_tree_partitioning(tree: nx.DiGraph,
                                   partition: T_PART,
                                   opt_cost: int,
                                   opt_lat: int,
                                   root: int,
                                   cp_end: int,
                                   M: int,
                                   L: int,
                                   N: int,
                                   delay: int,
                                   draw: bool = True)
```

Evaluate tree partitioning and print its characteristics assuming parallelized platform execution model.

**Arguments**:

- `tree`: input tree
- `partition`: given partitioning
- `opt_cost`: optimal partitioning cost
- `opt_lat`: latency value of the partitioning
- `root`: root node
- `cp_end`: end node of critical path
- `M`: upper memory limit
- `L`: latency limit
- `N`: CPU count
- `delay`: platform invocation delay
- `draw`: draw tree

<a id="slambuc.misc.util.evaluate_gen_tree_partitioning"></a>

#### evaluate\_gen\_tree\_partitioning

```python
def evaluate_gen_tree_partitioning(tree: nx.DiGraph,
                                   partition: T_PART,
                                   opt_cost: int,
                                   opt_lat: int,
                                   root: int,
                                   flavors: list,
                                   cp_end: int,
                                   L: int,
                                   delay: int,
                                   draw: bool = True)
```

Evaluate tree partitioning and print its characteristics assuming parallelized platform execution model.

**Arguments**:

- `tree`: input tree
- `partition`: given partitioning
- `opt_cost`: optimal partitioning cost
- `opt_lat`: latency value of the partitioning
- `root`: root node
- `flavors`: list of flavors
- `cp_end`: end node of critical path
- `L`: latency limit
- `delay`: platform invocation delay
- `draw`: draw tree

<a id="slambuc.misc.util.print_ser_chain_summary"></a>

#### print\_ser\_chain\_summary

```python
def print_ser_chain_summary(runtime: list[int], memory: list[int],
                            rate: list[int], data: list[int])
```

Print chain summary assuming serialized execution model.

**Arguments**:

- `runtime`: list of runtime values
- `memory`: list of memory values
- `rate`: list of rate values
- `data`: list of data values

<a id="slambuc.misc.util.print_ser_block_stat"></a>

#### print\_ser\_block\_stat

```python
def print_ser_block_stat(partition: T_PART,
                         runtime: list[int],
                         memory: list[int],
                         rate: list[int],
                         data: list[int],
                         delay: float,
                         start: int = 0,
                         end: int = None)
```

Print block stats of a chain partitioning assuming serialized execution model.

**Arguments**:

- `partition`: given partitioning
- `runtime`: list of runtime values
- `memory`: list of memory values
- `rate`: list of rate values
- `data`: list of data values
- `delay`: platform delay
- `start`: fist node to consider
- `end`: last node to consider

<a id="slambuc.misc.util.evaluate_ser_chain_partitioning"></a>

#### evaluate\_ser\_chain\_partitioning

```python
def evaluate_ser_chain_partitioning(partition: T_PART,
                                    opt_cost: int,
                                    opt_lat: int,
                                    runtime: list[int],
                                    memory: list[int],
                                    rate: list[int],
                                    data: list[int],
                                    M: int = math.inf,
                                    L: int = math.inf,
                                    start: int = 0,
                                    end: int = None,
                                    delay: int = 1)
```

Evaluate chain partitioning and print its characteristics assuming serialized execution model.

**Arguments**:

- `partition`: given partitioning
- `opt_cost`: optimal partitioning cost
- `opt_lat`: latency value of the partitioning
- `runtime`: list of runtime values
- `memory`: list of memory values
- `rate`: list of rate values
- `data`: list of data values
- `M`: upper memory limit
- `L`: latency limit
- `start`: fist node to consider
- `end`: last node to consider
- `delay`: platform delay

<a id="slambuc.misc.util.print_lp_desc"></a>

#### print\_lp\_desc

```python
def print_lp_desc(model: pulp.LpProblem)
```

Print the lp format of the model.

**Arguments**:

- `model`: PuLP model object

<a id="slambuc.misc.util.convert_var_dict"></a>

#### convert\_var\_dict

```python
def convert_var_dict(X: dict[int, dict[int]]) -> list[list[pulp.LpVariable]]
```

Convert dict-of-dict variable matrix into list-of-list format.

**Arguments**:

- `X`: specific structure of decision variables

**Returns**:

converted format of decision variables

<a id="slambuc.misc.util.print_var_matrix"></a>

#### print\_var\_matrix

```python
def print_var_matrix(X: list[list[pulp.LpVariable]])
```

Print matrix of decision variables names in tabular format.

**Arguments**:

- `X`: specific structure of decision variables

<a id="slambuc.misc.util.print_pulp_matrix_values"></a>

#### print\_pulp\_matrix\_values

```python
def print_pulp_matrix_values(X: list[list[pulp.LpVariable]])
```

Print matrix of decision variables values in tabular format.

**Arguments**:

- `X`: specific structure of decision variables

<a id="slambuc.misc.util.print_cplex_matrix_values"></a>

#### print\_cplex\_matrix\_values

```python
def print_cplex_matrix_values(X: list[list[pulp.LpVariable]])
```

Print matrix of decision variables values in tabular format.

**Arguments**:

- `X`: specific structure of decision variables

<a id="slambuc.misc.util.print_cost_coeffs"></a>

#### print\_cost\_coeffs

```python
def print_cost_coeffs(model: pulp.LpProblem, X: list[list[pulp.LpVariable]])
```

Print cost coefficients of the given LP *model*.

**Arguments**:

- `model`: model object
- `X`: specific structure of decision variables

<a id="slambuc.misc.util.print_lat_coeffs"></a>

#### print\_lat\_coeffs

```python
def print_lat_coeffs(model: pulp.LpProblem, X: list[list[pulp.LpVariable]])
```

Print latency coefficients of the given LP *model*.

**Arguments**:

- `model`: model object
- `X`: specific structure of decision variables


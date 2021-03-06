# Copyright (c) The University of Edinburgh 2014
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dispel4py.new.mpi_process import process
from dispel4py.workflow_graph import WorkflowGraph
from dispel4py.examples.graph_testing.testing_PEs import TestProducer, TestOneInOneOut

from mpi4py import MPI
        
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

prod = TestProducer()
cons1 = TestOneInOneOut()
cons2 = TestOneInOneOut()
    
graph = WorkflowGraph()
graph.connect(prod, 'output', cons1, 'input')
graph.connect(cons1, 'output', cons2, 'input')

process(graph, { prod : [ {}, {}, {} ] } )

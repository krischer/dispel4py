.. .. documentation master file, created by
   sphinx-quickstart on Mon Aug 11 11:22:11 2014.

Dispel4Py API documentation
===========================

.. rubric:: Core modules

.. autosummary::
   :nosignatures:
   :toctree: .
   
   dispel4py.core
   dispel4py.base
   dispel4py.utils
   dispel4py.visualisation
   dispel4py.workflow_graph
   
.. rubric:: Enactment platforms

.. autosummary::
   :nosignatures:
   :toctree: .

   dispel4py.new.simple_process
   dispel4py.new.multi_process
   dispel4py.new.mpi_process
   dispel4py.new.processor
   dispel4py.storm.storm_submission
   dispel4py.storm.topology

.. rubric:: Examples and tests

.. autosummary::
    :nosignatures:
    :toctree: .
    
    dispel4py.examples.graph_testing.pipeline_test
    dispel4py.examples.graph_testing.split_merge
    dispel4py.examples.graph_testing.teecopy
    dispel4py.examples.graph_testing.group_by
    dispel4py.examples.graph_testing.grouping_alltoone
    dispel4py.examples.graph_testing.grouping_onetoall
    dispel4py.examples.graph_testing.grouping_split_merge
    dispel4py.examples.graph_testing.parallel_pipeline
    dispel4py.examples.graph_testing.partition_parallel_pipeline
    dispel4py.examples.graph_testing.pipeline_composite
    dispel4py.examples.graph_testing.word_count
    dispel4py.examples.graph_testing.word_count_filter
    dispel4py.examples.graph_testing.testing_PEs
    dispel4py.new.simple_process_test
    dispel4py.new.multi_process_test
    dispel4py.new.aggregate
    

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


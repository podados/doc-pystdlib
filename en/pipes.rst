






The pipes module
=================




(Unix only). This module contains support functions to create
“conversion pipelines” . You can create a pipeline consisting of a
number of external utilities, and use it on one or more files.


**Example: Using the pipes module**

.. sourcecode:: python

    
    # File: `pipes-example-1.py <pipes-example-1.py>`__
    
    import pipes
    
    t = pipes.Template()
    
    # create a pipeline
    t.append("sort", "--")
    t.append("uniq", "--")
    
    # filter some text
    t.copy("samples/sample.txt", "")
    


.. sourcecode:: python

    
    Alan Jones (sensible party)
    Kevin Phillips-Bong (slightly silly)
    Tarquin Fin-tim-lin-bin-whin-bim-lin-bus-stop-F'tang-F'tang-Olé-Biscuitbarrel



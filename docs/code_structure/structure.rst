Code Structure
==============

TrussPy's code structure is organized in an object-oriented approach, hence it uses classes, attributes, methods and functions. The main idea is to seperate the code in single files (in Python called (sub-)modules) which are grouped in subfolders (again, so-called (sub-)packages). A basic overview of the essential classes is given in the following figure. It all starts with the **Model** class - it is basically the main container in TrussPy. On the next meta-level so-called **Handler** classes are managing the low-level **Core** classes of TrussPy: **Node**, **Element**, **Boundary**, **Analysis** and **Result**.

.. figure:: code_structure.png
   :align: center
   :width: 90%
   :alt: TrussPy's essential code structure
   
   TrussPy's essential code structure
   
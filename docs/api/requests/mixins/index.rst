Request Mixins
==============
Request Mixins are classes that define the functionality of each ``Request`` subclass. All subclasses inherit from the ``BaseRequest``, which define the constructor and basic helpers to build the request.


BaseRequest
-----------
.. automodule:: cerami.request.mixins.base_request
    :members:


Filterable
----------
.. autoclass:: cerami.request.mixins.Filterable
    :members:


Keyable
-------
.. autoclass:: cerami.request.mixins.Keyable
    :members:

Limitable
---------
.. autoclass:: cerami.request.mixins.Limitable
    :members:

Pageable
--------
.. autoclass:: cerami.request.mixins.Pageable
    :members:

Projectable
-----------
.. autoclass:: cerami.request.mixins.Projectable
    :members:

Returnable
----------
.. autoclass:: cerami.request.mixins.Returnable
    :members:

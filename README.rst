riot_apiv0.0.14
================

You can find this project on GitHub at: https://github.com/Alex-Weatherhead/riot_api

You can find this project on PyPi at: https://pypi.org/manage/project/Riot-API/releases/

Making API Calls
-----------------

Each API call returns a dictionary object containing useful information for managing the control flow of the client program.

If a request is successful, then the dictionary simply contains a flag and the jsonified body of the response.

.. code:: python

    {
        "successful": True,
        "body": response.json()
    }

However, if a request is not successful, the dictionary contains information about the error encountered, as well as whether the request should be retried, and if so, how long after the initial request the client program should wait before retrying.

.. code:: python

    {
        "successful": False,
        "error": {
            "status_code": status_code,
            "reason": reason
        },
        "retry": False,
        "delay": delay   # If retry is True, this is the amount of time the client program should wait before retrying the request.
    }
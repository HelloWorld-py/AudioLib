Using the Module
================
To start you must install the module. It is available on PyPi

.. code-block:: bat

    pip install AudioLib

.. tip::

    If you don't have admin access, you can install modules to a virtual environment.
    Learn more about that here_

.. _here: `Trouble Shooting`_


After the module has installed you can then import it to your project.
Next, you create a *Stream* object. This takes a **file name** as a string as it's first argument.
Your stream is now set up and you can now play it.

.. code-block:: python

    import AudioLib

    stream = AudioLib.Stream("test.wav")
    stream.play()

    while stream.isPlaying:
        pass

.. Admonition:: Threads

   This project uses the threading module to allow other operations to be done while
   the stream is playing. It plays in a *Daemon* thread which means that it will close when
   the main thread stops.

That's it! That's all it takes to start using this library. In the next section, the API will be explained
in depth.

Trouble Shooting
================

There are a few errors that may arise when trying to install this module. If you do not have  administrator privileges
(on a network for example) you may not be able to use the pip command in the command prompt.
Here are two ways to install the module to a |venv|.

Installing using Pycharm
^^^^^^^^^^^^^^^^^^^^^^^^
1) In the Pycharm IDE, go to

    | File > Settings > Project: [Project Name] > Project interpreter

    If you have not set the project interpreter to your virtual environment, you can do that through this window.

2) Once the |venv| is set up, double click on '**pip**' in the packages section.

#) Go to the search bar and type "*AudioLib*"

#) Click on AudioLib and then click install package (lower left-hand corner)

#) try to run the example code, if it works then the package successfully installed


.. |venv| replace:: virtual environment


Installing using the source
^^^^^^^^^^^^^^^^^^^^^^^^^^^
#) Download AudioLib from Github_ or Pypi_.

#) Unzip the file to a folder

#) Inside of that folder, navigate to "*AudioLib*" (this will have a setup.py file inside)

#) Inside of that folder, there is another folder named "*AudioLib*". Move that folder
   into the project's |venv| at `./venv/Lib/site-packages/`

#) try to run the example code, if it works then the package successfully installed

.. _Github: https://github.com/HelloWorld-py/AudioLib
.. _Pypi: https://pypi.org/project/AudioLib/



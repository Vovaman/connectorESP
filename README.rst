connectorESP
============
Typical connector running on ESP32 for work with Peresvet.

config.json
===========
Файл `config.json` имеет вид:

.. code-block:: JSON
   :linenos:
   {
      "id": ""

   }


start
=====
При запуске коннектор 

prsTagSource
============
Константа:
{
    "type": "const",
    "id": "const_name"
}

Датчик температуры DS18B20:
{
    "type": "ds18B20",
    "id": [1, 2, 3, 4, 6, 7, 8]
    "pin": 15
}

Обычный вход/выход 
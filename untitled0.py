{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMIiZzjV/cJWBz7blB70ZKd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Elvnazyomnova/project_1/blob/main/untitled0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WmFwJ9wTB9M6",
        "outputId": "f3180e65-07ed-4178-9279-369f794a9e85"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "введите количество символов9\n",
            "Пароль: Dl5XBY0xO\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "from random import sample\n",
        "sim = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'\n",
        "try:\n",
        "   dlina = int(input('введите количество символов'))\n",
        "except TypeError:\n",
        "   print('Ошибка ввода длины пароля')\n",
        "parol = sample(sim, dlina)\n",
        "print('Пароль:', ''.join(parol))\n",
        "\n"
      ]
    }
  ]
}
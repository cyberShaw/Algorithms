{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "binarySearch.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/cyberShaw/Algorithms/blob/master/binarySearch.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QXXiVa6VmYnJ",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "841f42ec-bd58-4447-91cc-f6f1aa07fbde"
      },
      "source": [
        "def binarySearch(A,l,r,x):\n",
        "  if (r >= l):\n",
        "    mid = int((l + (r-1))/2)\n",
        "    if (A[mid] == x):\n",
        "      return mid\n",
        "    elif (A[mid] > x):\n",
        "      r = mid - 1\n",
        "      return binarySearch(A,l,r,x)\n",
        "    else:\n",
        "      l = mid + 1\n",
        "      return binarySearch(A,l,r,x)\n",
        "\n",
        "A = [1,2,3,4,5,6,7,8,9]\n",
        "print(binarySearch(A,0,len(A)-1,8))\n"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "7\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G819L76BrT2H",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}
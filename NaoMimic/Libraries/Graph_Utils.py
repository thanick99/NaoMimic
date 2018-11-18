"""
Supports the visualization of data for development.
"""

# Imports
import matplotlib.pyplot as plt
import os
import time
from os.path import dirname, abspath

# Project libraries
from Libraries import Error_Utils as error

# ----------------------------------------------------------------------------------------------------------------------

def plotCompareSameAxis(referenceAxis, compareAxis1, refLabel = "Reference Axis", axisLabel1 = "Compare Axis 1",
                        compareAxis2 = None,  axisLabel2 = "Compare Axis 2", saveImage = False, filePath = "Default/",
                        showPlot = True):
    """
    This function is used to plot the data sets from a reference axis and up to 2 comparison axes. The plotted image can
    be store as a PNG file.

    :param referenceAxis: Data set to take as reference.
    :param refLabel: Label of the reference data set.
    :param compareAxis1: First data set to compare.
    :param axisLabel1: Label of compareAxis1.
    :param compareAxis2: Second data set to compare.
    :param axisLabel2: Label of compareAxis2.
    :param saveImage: True to save the plot as a PNG file.
    :param filePath: Path and name of the file to store.
    :param showPlot: False to prevent plot to pop out.
    :return: void
    """

    # Load data
    plt.plot(referenceAxis, label=refLabel)
    plt.plot(compareAxis1, label=axisLabel1)
    if compareAxis2 is not None:
        plt.plot(compareAxis2, label=axisLabel2)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

    if showPlot:
        plt.show()

    # Save graph as PNG file
    if saveImage:
        rootDir = dirname(dirname(abspath(__file__)))
        fileDir = os.path.join(rootDir, "Comparisons/")
        fileDir = os.path.join(fileDir, filePath)
        if filePath == "Default/":
            fileDir += time.strftime("%Y-%m-%d_%H-%M-%S")
        fileDir += ".png"
        try:
            plt.savefig(fileDir, bbox_inches='tight')
        except FileExistsError:
            print("File name already exists, saving file with time and date on Default directory.")
            try:
                newDir =  os.path.join(rootDir, "Comparisons/Default/%Y-%m-%d_%H-%M-%S")
                print("Plot image saved as: " + newDir)
            except Exception:
                error.abort("Failed to save plot image", None, Exception)

# ----------------------------------------------------------------------------------------------------------------------

def plotAxes(axesDataSet, labels = ["X axis", "Y axis", "Z axis", "WX axis", "WY axis", "WZ axis"],
                saveImage = False, filePath = "Default/"):
    """
    This function is used to plot a single data set to show all included axes. The plot can be saved into a PNG file.

    :param axesDataSet: The data set to plot. Its size will define the amount of axes shown.
    :param labels: Label of the axes included.
    :param saveImage: True to save plot as PNG file.
    :param filePath: Path and name of image to save.
    :return: void
    """

    # Load data
    if len(labels) > 1:
        for axis in range(len(labels)):
            plt.plot(axesDataSet[axis], label=labels[axis])
    else:
        plt.plot(axesDataSet, label=labels)

    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

    if showPlot:
        plt.show()

    # Save graph as PNG file
    if saveImage:
        rootDir = dirname(dirname(abspath(__file__)))
        fileDir = os.path.join(rootDir, "Comparisons/")
        fileDir = os.path.join(fileDir, filePath)
        if filePath == "Default/":
            fileDir += time.strftime("%Y-%m-%d_%H-%M-%S")
        fileDir += ".png"
        try:
            plt.savefig(fileDir, bbox_inches='tight')
        except FileExistsError:
            print("File name already exists, saving file with time and date on Default directory.")
            try:
                newDir = os.path.join(rootDir, "Comparisons/Default/%Y-%m-%d_%H-%M-%S")
                print("Plot image saved as: " + newDir)
            except Exception:
                error.abort("Failed to save plot image", None, Exception)
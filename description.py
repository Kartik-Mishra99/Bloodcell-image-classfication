"""
https://www.kaggle.com/paultimothymooney/blood-cells

Problem Description----
Each image has multiple blood cells in it. On average it would probably be 10 cells per image.
The cell-of-interest is colored purple while other cells are colored skin-red.
One cell-of-interest per image
Goal: Identify the cell-type of cell-of-interest

Manual Identification----
Limphocyte: looks like well rounded purple colored potato. These are the easiest to identify.

Monocyte: The cell shape lookes roundish with skin-red color with some purple stuff inside. However the purple 
color is never fully covering the cell surface. Also, the purple colored portion of the cell is always in one 
continuous piece.

Neutrophil: The cell shape lookes roundish with skin-red color with some purple stuff inside. However the cell contains 
purple colored multiple whole-groundnuts inside it. The groundnuts could be disjointed within the cell.

Eosinophil: They look like Neutrophils. Alas! See the confusion matrix published by paultimothymooney. In his kernel,
 most of the failures happen when predictor falsly thinks that Eosinophils are Neutrophils.
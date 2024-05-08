This repo contains the code for the SegMine task.

### Installation

To install the required packages, run the following command:
''' python
pip install -r requirements.txt
'''

### Pipeline

To run the pipeline execute the following command:
''' python
python3
'''
The pipeline is currently set to run on a sample of 5 images. To run the pipeline on the entire dataset, remove the counter in the for loop.

Below an overview of the workflow & parts still to be completed.

### Workflow:

1. Exploratory analysis of the images => stats & pixel distribution.
2. Data preprocessing => normalization & formatting.
3. Cell segmentation & mask generation => Cellpose.
4. Segmentation evaluation => original image & mask comparison.
5. Mask post-processing => binarization.
6. Binary mask evaluation => original image & masks comparison.
7. Cell morphology analysis => cell features extraction (cell number,area & perimeter).
8. Evaluation of segmentation results & labelled regions => visulization of single labelled regions & check if corresponding to single cells.
9. Adjustment of cell mask => remove small regions & fill holes - skimage functions.
10. Extract cell coordinates for each image.
11. Save cell morphology data & coordinates in a csv file.

### TODO:

- [ ] Improve cell segmentation - not all cells are segmented well.
- [ ] Extract single - cell masks from the binary masks => loop through labelled regions.
- [ ] Update draft for cell intensities analysis.
- [ ] Mine profiles for each cell with DeepProfiler | issues with DeepProfiler installation.
- [ ] Group data by 'well' & 'site' columns & calulate mean or median for each group => use groupby() method.
- [ ] Dimensionality reduction & clustering => UMAP || T-SNE & K-means.
- [ ] Compatibility with \*nix systems => Alternative 1) investigate available packages for compatibility. Alternative 2) convert into executables.
- [ ] Improve point 11 => save data in a database.

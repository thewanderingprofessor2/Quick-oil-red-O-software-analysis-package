This code and software has been developed as a simple and free package to analyse organisms (C. elegans in our case) stained for total lipids with Quick Oil Red O. 
For a detailed description of the staining methods please see Wahlby et al 2014 (http://dx.doi.org/10.1016/j.ymeth.2014.04.017). We will also be submitting this work to micropublication.org 
for publication.
Workflow for a typical staining project:
1) grow animals
2) stain with Quick Oil Red O (see Wahlby)
3) Image with appropriate microscope (compound scope with x20 objective under brightfield for C. elegans)
4) Remove background using Magic Select function in Paint3D (will be described in Micropub)
5) Run images through Biopython analysis software (this package) to generate average pixel intensity per animal.

To use this package you need to install Biopython on either Windows or Mac (see relevant instruction guide), then modify the worm.py script to suit your computer and images, followed
by adding your images to the folder you describe in the worm.py script and hitting go. It's really simple at that point. If you have any issues installing the software or suggestions about
how to improve the guides, please let me know at crookm@wofford.edu

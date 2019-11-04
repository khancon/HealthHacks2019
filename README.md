# HealthHacks2019

Our team met Saturday morning at VCU; and thought up several possible problems to tackle.

A big issue in healthcare is that there is little to efficient follow up for patients on a daily basis post surgery. To solve this issue, our team came up with creating a simple form that patients can fill out on a daily basis recording how they feel and such. We built the form using Django (in Python), which automatically saves the data in "Models" (can be thought of as tables in a relational database). We then added code that will help to export the data in these back-end models into csv files, which will be put through an end-to-end machine learning pipeline to help analyze the data.

This will most likely be an online learning pipeline as data will continuously be coming in daily. To test the robustness of the pipeline, we tested it on sample patient data obtained from kaggle.com. While we didn't have enough time to finish the project to completion, our main point of joining the hackathon was to learn, but we still managed to have the form working, saving, and exporting data continuously to the pipeline (in the .ipynb file) locally.

Furthermore, our team was inspired to try to explore medical image classification. We sought to use an SVM style from our ML projects on cell image data of malaria infected cells and healthy cells to be able to mass identify infection of cells. This project was met with difficults of trying to integrate very large size memory instances.
